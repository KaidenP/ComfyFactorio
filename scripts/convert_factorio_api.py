#!/usr/bin/env python3
"""
Convert the Factorio lua-api documentation into an Obsidian-style markdown vault.

Inputs (from an unpacked lua-api archive's `files/` directory):
  - runtime-api.json
  - prototype-api.json
  - auxiliary/*.html
  - static/images/*, static/*.png, static/*.svg

Output: an Obsidian vault folder with YAML frontmatter, `[[wikilinks]]`, MOC
index notes, and a Home note.

Usage:
    python3 scripts/convert_factorio_api.py [INPUT_DIR] [OUTPUT_DIR]

Defaults:
    INPUT_DIR  = /tmp/factorio_archive/files
    OUTPUT_DIR = docs/factorio_api
"""
import collections
import json
import os
import re
import shutil
import subprocess
import sys


def eprint(*a):
    print(*a, file=sys.stderr)


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
INPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/tmp/factorio_archive/files"
OUTPUT_DIR = sys.argv[2] if len(sys.argv) > 2 else "docs/factorio_api"


def load_json(name):
    with open(os.path.join(INPUT_DIR, name), encoding="utf-8") as f:
        return json.load(f)


rt = load_json("runtime-api.json")
pt = load_json("prototype-api.json")

VERSION = rt.get("application_version", "")

# Auxiliary (guide) page names, known up front so links in JSON descriptions resolve.
AUX_DIR = os.path.join(INPUT_DIR, "auxiliary")
GUIDE_NAMES = (
    {f[:-5] for f in os.listdir(AUX_DIR) if f.endswith(".html")}
    if os.path.isdir(AUX_DIR)
    else set()
)

# ---------------------------------------------------------------------------
# Entity registry & file naming (with disambiguation)
# ---------------------------------------------------------------------------
# category -> (folder, filename_prefix, tag)
CAT_DEFS = {
    "class":     ("Runtime/Classes",     "",         "class"),
    "event":     ("Runtime/Events",      "",         "event"),
    "concept":   ("Runtime/Concepts",    "",         "concept"),
    "define":    ("Runtime/Defines",     "defines.", "define"),
    "object":    ("Runtime/Objects",     "",         "global-object"),
    "function":  ("Runtime/Functions",   "",         "global-function"),
    "prototype": ("Prototype/Prototypes", "",        "prototype"),
    "type":      ("Prototype/Types",     "",         "type"),
}

# Ordered category names for contextual type-name resolution.
RUNTIME_CATS = ["class", "concept", "event", "object", "function"]
PROTOTYPE_CATS = ["type", "prototype"]

entries = []  # list of dicts {category, name, data}


def add(cat, name, data):
    entries.append({"category": cat, "name": name, "data": data})


for c in rt["classes"]:
    add("class", c["name"], c)
for e in rt["events"]:
    add("event", e["name"], e)
for c in rt["concepts"]:
    add("concept", c["name"], c)
for d in rt["defines"]:
    add("define", d["name"], d)
for o in rt["global_objects"]:
    add("object", o["name"], o)
for f in rt["global_functions"]:
    add("function", f["name"], f)
for p in pt["prototypes"]:
    add("prototype", p["name"], p)
for t in pt["types"]:
    add("type", t["name"], t)

concept_names = {e["name"] for e in entries if e["category"] == "concept"}


def basename_for(e):
    n = e["name"]
    cat = e["category"]
    if cat == "type" and n in concept_names:
        return n + " (type)"
    if cat == "prototype" and n in concept_names:
        return n + " (prototype)"
    return n


registry = collections.defaultdict(dict)  # category -> name -> (relpath, base)
by_basename = {}                          # base -> relpath
lookup_runtime = {}                       # name -> base   (runtime namespace)
lookup_prototype = {}                     # name -> base   (prototype namespace)

for e in entries:
    cat = e["category"]
    folder, prefix, tag = CAT_DEFS[cat]
    base = prefix + basename_for(e)
    relpath = f"{folder}/{base}.md"
    registry[cat][e["name"]] = (relpath, base)
    by_basename[base] = relpath
    if cat in RUNTIME_CATS:
        lookup_runtime[e["name"]] = base
    if cat == "define":
        lookup_runtime["defines." + e["name"]] = base
        lookup_runtime[e["name"]] = base
    if cat in PROTOTYPE_CATS:
        lookup_prototype[e["name"]] = base
    if cat == "define":
        lookup_prototype["defines." + e["name"]] = base

# Guarantee vault-wide unique note names.
if len(by_basename) != len(entries):
    counts = collections.Counter(
        registry[e["category"]][e["name"]][1] for e in entries
    )
    for base, n in counts.items():
        if n > 1:
            eprint(f"DUPLICATE basename: {base} (x{n})")
    eprint("ERROR: non-unique note names; aborting")
    sys.exit(1)

eprint(f"Entities: {len(entries)}  Unique note names: {len(by_basename)}")


# ---------------------------------------------------------------------------
# Link resolution helpers
# ---------------------------------------------------------------------------
MOC_NAMES = {
    "Classes", "Concepts", "Events", "Defines", "Objects",
    "Functions", "Prototypes", "Types", "Guides",
}
IDX_RUNTIME = {
    "classes": "Classes", "concepts": "Concepts", "events": "Events",
    "defines": "Defines", "types": "Types", "objects": "Objects",
    "functions": "Functions",
}
IDX_PROTOTYPE = {"prototypes": "Prototypes", "types": "Types", "defines": "Defines"}


def base_of(cat, name):
    r = registry[cat].get(name)
    return r[1] if r else None


def resolve_define_path(path):
    """Resolve a `defines.`-prefixed dotted path -> (base, anchor)."""
    parts = path.split(".")
    dname = parts[0]
    r = registry["define"].get(dname)
    if not r:
        return None
    anchor = parts[-1] if len(parts) > 1 else None
    return (r[1], anchor)


def wikilink(base, anchor=None, alias=None):
    target = base if not anchor else f"{base}#{anchor}"
    if alias and alias != base:
        return f"[[{target}|{alias}]]"
    return f"[[{target}]]"


def resolve(target):
    """Resolve a link target string -> (base, anchor) or None."""
    if target.startswith("runtime:"):
        rest = target[len("runtime:"):]
        if rest in IDX_RUNTIME:
            return (IDX_RUNTIME[rest], None)
        if rest == "prototypes":
            r = registry["object"].get("prototypes")
            return (r[1], None) if r else None
        if rest.startswith("defines."):
            return resolve_define_path(rest[len("defines."):])
        if "::" in rest:
            parent, member = rest.split("::", 1)
            b = lookup_runtime.get(parent)
            return (b, member) if b else None
        b = lookup_runtime.get(rest)
        return (b, None) if b else None

    if target.startswith("prototype:"):
        rest = target[len("prototype:"):]
        if rest in IDX_PROTOTYPE:
            return (IDX_PROTOTYPE[rest], None)
        if rest.startswith("defines."):
            return resolve_define_path(rest[len("defines."):])
        if "::" in rest:
            parent, member = rest.split("::", 1)
            b = lookup_prototype.get(parent)
            return (b, member) if b else None
        b = lookup_prototype.get(rest)
        return (b, None) if b else None

    if target.startswith("auxiliary:"):
        name = target[len("auxiliary:"):]
        if name in GUIDE_NAMES:
            return (name, None)
        return None

    if target.endswith(".html"):
        t = target[:-5]
        anchor = None
        if "#" in t:
            t, anchor = t.split("#", 1)
        base = t.rstrip("/").split("/")[-1]
        html_moc = {
            "classes": "Classes", "concepts": "Concepts", "events": "Events",
            "defines": "Defines", "types": "Types", "prototypes": "Prototypes",
            "index": "Factorio API", "index-runtime": "Factorio API",
            "index-prototype": "Factorio API", "index-auxiliary": "Factorio API",
        }
        if base in html_moc:
            return (html_moc[base], anchor)
        if base in GUIDE_NAMES:
            return (base, anchor)
        if base in by_basename:
            return (base, anchor)
        return None

    return None


_ALIAS_OK = re.compile(r"[\w .:'\-\"()]+$")


def convert_links(text, ctx):
    """Replace [text](target) markdown links with Obsidian wikilinks."""
    if not text:
        return text

    def repl(m):
        txt, target = m.group(1), m.group(2)
        if target.startswith(("http://", "https://", "mailto:", "ftp://", "//")):
            return m.group(0)
        if target.startswith("#"):
            return m.group(0)
        r = resolve(target)
        if not r:
            return m.group(0)
        base, anchor = r
        alias = txt.strip().replace("`", "").strip()
        if (not alias or alias == base or "[" in alias
                or "]" in alias or "#" in alias or "|" in alias
                or not _ALIAS_OK.match(alias)):
            alias = None
        return wikilink(base, anchor, alias)

    return re.sub(r"\[([^\]]*)\]\(([^)]+)\)", repl, text)


def fmt_typename(name, ctx):
    """Render a type-position name as a wikilink (or inline code fallback)."""
    if not isinstance(name, str):
        return type_str(name, ctx)
    if name.startswith("defines."):
        r = resolve_define_path(name[len("defines."):])
        if r:
            return wikilink(r[0], r[1])
        return f"`{name}`"
    order = RUNTIME_CATS + PROTOTYPE_CATS if ctx == "runtime" else PROTOTYPE_CATS + RUNTIME_CATS
    for cat in order:
        r = registry[cat].get(name)
        if r:
            return wikilink(r[1])
    return f"`{name}`"


def type_str(t, ctx):
    """Render a type node (string or complex_type dict) as markdown."""
    if isinstance(t, str):
        return fmt_typename(t, ctx)
    if isinstance(t, list):
        return ", ".join(type_str(x, ctx) for x in t)
    if isinstance(t, dict):
        ct = t.get("complex_type")
        if ct == "literal":
            v = t.get("value")
            if isinstance(v, str):
                return "`" + json.dumps(v) + "`"
            if isinstance(v, bool):
                return "`" + str(v).lower() + "`"
            return "`" + str(v) + "`"
        if ct == "array":
            return "array<" + type_str(t.get("value"), ctx) + ">"
        if ct == "dictionary":
            return ("dictionary<" + type_str(t.get("key"), ctx) + " → "
                    + type_str(t.get("value"), ctx) + ">")
        if ct == "LuaCustomTable":
            return ("LuaCustomTable<" + type_str(t.get("key"), ctx) + " → "
                    + type_str(t.get("value"), ctx) + ">")
        if ct == "LuaLazyLoadedValue":
            return "LuaLazyLoadedValue<" + type_str(t.get("value"), ctx) + ">"
        if ct == "union":
            return " | ".join(type_str(o, ctx) for o in t.get("options", []))
        if ct == "tuple":
            return "(" + ", ".join(type_str(v, ctx) for v in t.get("values", [])) + ")"
        if ct == "function":
            return "function(" + ", ".join(type_str(p, ctx) for p in t.get("parameters", [])) + ")"
        if ct == "type":
            s = type_str(t.get("value"), ctx)
            d = t.get("description")
            if d:
                s += " — " + d
            return s
        if ct == "builtin":
            return "builtin"
        if ct == "table":
            return "table"
        if ct == "struct":
            return "struct"
        if ct == "LuaStruct":
            return "struct"
        return "`" + json.dumps(t) + "`"
    if t is None:
        return "`nil`"
    return "`" + str(t) + "`"


def one_line(s):
    return " ".join((s or "").split())


# ---------------------------------------------------------------------------
# Rendering primitives
# ---------------------------------------------------------------------------
def code_block(ex):
    ex = (ex or "").strip()
    if ex.startswith("```"):
        return ex
    return "```lua\n" + ex + "\n```"


def member_heading(p, ctx, depth=3):
    h = "#" * depth
    out = [f"{h} {p['name']}"]
    lines = []
    if "type" in p:
        lines.append(f"- **Type:** {type_str(p['type'], ctx)}")
    else:
        if "read_type" in p:
            lines.append(f"- **Type:** {type_str(p['read_type'], ctx)}")
        if "write_type" in p:
            lines.append(f"- **Writable:** {type_str(p['write_type'], ctx)}")
    if p.get("optional"):
        lines.append("- **Optional**")
    if "default" in p:
        dv = p["default"]
        if isinstance(dv, str):
            lines.append(f"- **Default:** {dv}")
        else:
            lines.append(f"- **Default:** {type_str(dv, ctx)}")
    if p.get("override"):
        lines.append("- **Overrides parent**")
    if p.get("visibility"):
        lines.append("- **Requires:** " + ", ".join(f"`{v}`" for v in p["visibility"]))
    out.extend(lines)
    if p.get("description"):
        out.append(convert_links(p["description"], ctx))
    if p.get("lists"):
        for it in p["lists"]:
            out.append(convert_links(it, ctx))
    if p.get("examples"):
        out.append("**Examples:**")
        for ex in p["examples"]:
            out.append("")
            out.append(code_block(ex))
    if p.get("images"):
        for img in p["images"]:
            out.append("")
            out.append(f"![[{img['filename']}]]")
            if img.get("caption"):
                out.append(f"*{img['caption']}*")
    return out


def param_line(p, ctx):
    name = p.get("name", "?")
    opt = " *(optional)*" if p.get("optional") else ""
    s = f"- **`{name}`** — {type_str(p.get('type'), ctx)}{opt}"
    d = p.get("description")
    if d:
        s += ": " + convert_links(one_line(d), ctx)
    return s


def ret_line(r, ctx):
    opt = " *(optional)*" if r.get("optional") else ""
    s = f"- {type_str(r.get('type'), ctx)}{opt}"
    d = r.get("description")
    if d:
        s += ": " + convert_links(one_line(d), ctx)
    return s


def subclasses_line(items, cat):
    links = [wikilink(base_of(cat, s)) for s in items if base_of(cat, s)]
    if not links:
        links = [f"`{s}`" for s in items]
    return "*Only available on:* " + ", ".join(links)


def raises_block(raises, ctx):
    out = ["**Raises:**"]
    for r in raises:
        ev = r["name"]
        link = wikilink(base_of("event", ev)) if base_of("event", ev) else f"`{ev}`"
        s = f"- {link}"
        tf = r.get("timeframe")
        if tf:
            s += f" *(timeframe: {tf})*"
        d = r.get("description")
        if d:
            s += ": " + convert_links(one_line(d), ctx)
        out.append(s)
    return out


def examples_block(examples):
    out = []
    for ex in examples:
        out.append(code_block(ex))
    return out


# ---------------------------------------------------------------------------
# Note renderers
# ---------------------------------------------------------------------------
def frontmatter(title, tags):
    tag_yaml = ", ".join(tags)
    return f"---\ntitle: {title}\ntags: [{tag_yaml}]\n---\n"


def h1_for(e, base):
    if base != e["name"]:
        return f"# {e['name']}\n\n*Note: `{base}`.*\n"
    return f"# {e['name']}\n"


def render_class(c):
    ctx = "runtime"
    e = entries_by_cat_name[("class", c["name"])]
    out = [h1_for(e, registry["class"][c["name"]][1])]
    if c.get("abstract"):
        out.append("\n> **Abstract class** — not directly instantiable.")
    if c.get("parent"):
        p = base_of("class", c["parent"])
        out.append(f"\n> **Extends:** {wikilink(p) if p else '`' + c['parent'] + '`'}")
    if c.get("description"):
        out.append("\n" + convert_links(c["description"], ctx))

    attrs = sorted(c.get("attributes", []), key=lambda x: x.get("order", 0))
    if attrs:
        out.append("\n\n## Attributes")
        for a in attrs:
            out.append("")
            out.extend(member_heading(a, ctx, 3))

    methods = sorted(c.get("methods", []), key=lambda x: x.get("order", 0))
    if methods:
        out.append("\n\n## Methods")
        for m in methods:
            out.append("")
            out.extend(render_method(m, ctx, 3))

    ops = sorted(c.get("operators", []), key=lambda x: x.get("order", 0))
    if ops:
        out.append("\n\n## Operators")
        for m in ops:
            out.append("")
            out.extend(render_method(m, ctx, 3))

    if c.get("examples"):
        out.append("\n\n## Examples")
        for ex in c["examples"]:
            out.append("")
            out.append(code_block(ex))

    return "\n".join(out) + "\n"


def render_method(m, ctx, depth=3):
    h = "#" * depth
    out = [f"{h} {m['name']}"]
    if m.get("description"):
        out.append(convert_links(m["description"], ctx))
    if m.get("lists"):
        for it in m["lists"]:
            out.append(convert_links(it, ctx))
    if m.get("subclasses"):
        out.append(subclasses_line(m["subclasses"], "class"))

    params = list(m.get("parameters", []))
    if m.get("variadic_parameter"):
        params.append(m["variadic_parameter"])
    if params:
        takes_table = m.get("format", {}).get("takes_table")
        if takes_table:
            out.append("\nTakes a table with the following fields:")
        else:
            out.append("\n**Parameters:**")
        for p in sorted(params, key=lambda x: x.get("order", 0)):
            out.append(param_line(p, ctx))

    if m.get("variant_parameter_groups"):
        if m.get("variant_parameter_description"):
            out.append("\n" + convert_links(m["variant_parameter_description"], ctx))
        for g in m["variant_parameter_groups"]:
            out.append(f"\n**Variant `{g['name']}`:**")
            if g.get("description"):
                out.append(convert_links(g["description"], ctx))
            for p in sorted(g.get("parameters", []), key=lambda x: x.get("order", 0)):
                out.append("  " + param_line(p, ctx))

    rv = m.get("return_values", [])
    if rv:
        out.append("\n**Returns:**")
        for r in sorted(rv, key=lambda x: x.get("order", 0)):
            out.append(ret_line(r, ctx))

    if m.get("raises"):
        out.append("")
        out.extend(raises_block(m["raises"], ctx))

    if m.get("examples"):
        out.append("\n**Examples:**")
        for ex in m["examples"]:
            out.append("")
            out.append(code_block(ex))
    return out


def render_event(e):
    ctx = "runtime"
    ent = entries_by_cat_name[("event", e["name"])]
    out = [h1_for(ent, registry["event"][e["name"]][1])]
    if e.get("description"):
        out.append(convert_links(e["description"], ctx))
    if e.get("filter"):
        f = base_of("concept", e["filter"])
        flink = wikilink(f) if f else f"`{e['filter']}`"
        out.append(f"\n## Filter\n\n- **Type:** {flink}")

    data = sorted(e.get("data", []), key=lambda x: x.get("order", 0))
    if data:
        out.append("\n\n## Data")
        for d in data:
            out.append("")
            out.extend(member_heading(d, ctx, 3))

    if e.get("examples"):
        out.append("\n\n## Examples")
        for ex in e["examples"]:
            out.append("")
            out.append(code_block(ex))
    return "\n".join(out) + "\n"


def render_concept(c):
    ctx = "runtime"
    ent = entries_by_cat_name[("concept", c["name"])]
    out = [h1_for(ent, registry["concept"][c["name"]][1])]
    if c.get("description"):
        out.append(convert_links(c["description"], ctx))

    t = c.get("type")
    if isinstance(t, dict) and t.get("complex_type") in ("table", "struct", "LuaStruct"):
        members = t.get("parameters") or t.get("attributes") or []
        if members:
            out.append("\n## Fields")
            for p in sorted(members, key=lambda x: x.get("order", 0)):
                out.append("")
                out.extend(member_heading(p, ctx, 3))
    else:
        out.append("\n## Type\n\n" + type_str(t, ctx))

    if c.get("lists"):
        for it in c["lists"]:
            out.append("\n" + convert_links(it, ctx))
    if c.get("examples"):
        out.append("\n\n## Examples")
        for ex in c["examples"]:
            out.append("")
            out.append(code_block(ex))
    return "\n".join(out) + "\n"


def render_define(d):
    ent = entries_by_cat_name[("define", d["name"])]
    base = registry["define"][d["name"]][1]
    out = [h1_for(ent, base)]
    if d.get("description"):
        out.append(convert_links(d["description"], "runtime"))
    values = sorted(d.get("values", []), key=lambda x: x.get("order", 0))
    subkeys = sorted(d.get("subkeys", []), key=lambda x: x.get("order", 0))
    if values:
        out.append("\n## Values")
        for v in values:
            out.append("")
            out.append(f"### {v['name']}")
            if v.get("description"):
                out.append(convert_links(v["description"], "runtime"))
    if subkeys:
        out.append("\n## Subkeys")
        out.extend(render_subkeys(subkeys, 3))
    return "\n".join(out) + "\n"


def render_subkeys(items, depth):
    out = []
    for it in items:
        h = "#" * depth
        out.append(f"\n{h} {it['name']}")
        if it.get("description"):
            out.append(convert_links(it["description"], "runtime"))
        for v in sorted(it.get("values", []), key=lambda x: x.get("order", 0)):
            out.append(f"\n{'#' * (depth + 1)} {v['name']}")
            if v.get("description"):
                out.append(convert_links(v["description"], "runtime"))
        if it.get("subkeys"):
            out.extend(render_subkeys(it["subkeys"], depth + 1))
    return out


def render_object(o):
    ent = entries_by_cat_name[("object", o["name"])]
    out = [h1_for(ent, registry["object"][o["name"]][1])]
    if o.get("description"):
        out.append(convert_links(o["description"], "runtime"))
    t = o.get("type")
    if t:
        out.append("\n## Type\n\n" + fmt_typename(t, "runtime"))
    return "\n".join(out) + "\n"


def render_function(f):
    ent = entries_by_cat_name[("function", f["name"])]
    out = [h1_for(ent, registry["function"][f["name"]][1])]
    # `render_method` handles description/parameters/returns/examples; the
    # heading it emits is sliced off (the H1 already exists).
    out.extend(render_method(f, "runtime", 2)[1:])
    return "\n".join(out) + "\n"


def render_prototype(p):
    ctx = "prototype"
    ent = entries_by_cat_name[("prototype", p["name"])]
    out = [h1_for(ent, registry["prototype"][p["name"]][1])]

    meta = []
    if p.get("parent"):
        b = base_of("prototype", p["parent"]) or base_of("type", p["parent"])
        meta.append(f"**Parent:** {wikilink(b) if b else '`' + p['parent'] + '`'}")
    if p.get("typename"):
        meta.append(f"**Type name:** `{p['typename']}`")
    if p.get("abstract"):
        meta.append("**Abstract**")
    if p.get("deprecated"):
        meta.append("**Deprecated**")
    if p.get("instance_limit") is not None:
        meta.append(f"**Instance limit:** {p['instance_limit']}")
    if p.get("visibility"):
        meta.append("**Requires:** " + ", ".join(f"`{v}`" for v in p["visibility"]))
    if meta:
        out.append("\n> " + " · ".join(meta))

    if p.get("description"):
        out.append("\n" + convert_links(p["description"], ctx))

    props = sorted(p.get("properties", []), key=lambda x: x.get("order", 0))
    if props:
        out.append("\n\n## Properties")
        for pr in props:
            out.append("")
            out.extend(member_heading(pr, ctx, 3))

    cp = p.get("custom_properties")
    if cp:
        out.append("\n\n## Custom properties")
        if cp.get("description"):
            out.append(convert_links(cp["description"], ctx))
        for it in cp.get("lists", []):
            out.append(convert_links(it, ctx))

    if p.get("examples"):
        out.append("\n\n## Example")
        for ex in p["examples"]:
            out.append("")
            out.append(code_block(ex))
    return "\n".join(out) + "\n"


def render_type(t):
    ctx = "prototype"
    ent = entries_by_cat_name[("type", t["name"])]
    out = [h1_for(ent, registry["type"][t["name"]][1])]

    meta = []
    if t.get("parent"):
        b = base_of("type", t["parent"])
        meta.append(f"**Parent:** {wikilink(b) if b else '`' + t['parent'] + '`'}")
    if t.get("abstract"):
        meta.append("**Abstract**")
    if t.get("inline"):
        meta.append("**Inline**")
    if meta:
        out.append("\n> " + " · ".join(meta))

    if t.get("description"):
        out.append("\n" + convert_links(t["description"], ctx))

    ty = t.get("type")
    props = t.get("properties", [])
    if isinstance(ty, dict) and ty.get("complex_type") == "struct" and props:
        out.append("\n## Properties")
        for pr in sorted(props, key=lambda x: x.get("order", 0)):
            out.append("")
            out.extend(member_heading(pr, ctx, 3))
    else:
        out.append("\n## Type\n\n" + type_str(ty, ctx))
        if props:
            out.append("\n\n## Properties")
            for pr in sorted(props, key=lambda x: x.get("order", 0)):
                out.append("")
                out.extend(member_heading(pr, ctx, 3))

    if t.get("images"):
        out.append("\n\n## Images")
        for img in t["images"]:
            out.append("")
            out.append(f"![[{img['filename']}]]")
            if img.get("caption"):
                out.append(f"*{img['caption']}*")

    if t.get("examples"):
        out.append("\n\n## Examples")
        for ex in t["examples"]:
            out.append("")
            out.append(code_block(ex))
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# MOC / index renderers
# ---------------------------------------------------------------------------
def render_moc(title, tag, items):
    out = [f"# {title}\n", f"> {len(items)} notes."]
    for base in sorted(items):
        out.append(f"- [[{base}]]")
    body = "\n".join(out)
    return frontmatter(title, ["factorio-api", "moc", tag]) + body + "\n"


def render_home():
    lines = [
        "# Factorio API",
        "",
        f"> Factorio modding API reference (runtime + prototype), converted to Obsidian markdown. Source version **{VERSION}**.",
        "",
        "## Runtime",
        "",
        "- [[Classes]] — Lua classes",
        "- [[Events]] — script events",
        "- [[Concepts]] — types & concepts",
        "- [[Defines]] — `defines.*` constants",
        "- [[Objects]] — global objects",
        "- [[Functions]] — global functions",
        "",
        "## Prototype",
        "",
        "- [[Prototypes]] — prototype definitions",
        "- [[Types]] — data-stage types",
        "",
        "## Guides",
        "",
        "- [[Guides]] — auxiliary documentation",
    ]
    return frontmatter("Factorio API", ["factorio-api"]) + "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Write output
# ---------------------------------------------------------------------------
def write_note(relpath, content):
    full = os.path.join(OUTPUT_DIR, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    # Collapse excessive blank lines for cleaner source.
    content = re.sub(r"\n{3,}", "\n\n", content)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


entries_by_cat_name = {(e["category"], e["name"]): e for e in entries}


def tags_for(cat):
    tags = ["factorio-api"]
    if cat in RUNTIME_CATS:
        tags.append("runtime")
    elif cat in PROTOTYPE_CATS:
        tags.append("prototype")
    tags.append(CAT_DEFS[cat][2])
    # Dedupe while preserving order.
    seen = set()
    out = []
    for t in tags:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def generate_json_notes():
    renderers = {
        "class": (rt["classes"], render_class, "runtime"),
        "event": (rt["events"], render_event, "runtime"),
        "concept": (rt["concepts"], render_concept, "runtime"),
        "define": (rt["defines"], render_define, None),
        "object": (rt["global_objects"], render_object, "runtime"),
        "function": (rt["global_functions"], render_function, "runtime"),
        "prototype": (pt["prototypes"], render_prototype, "prototype"),
        "type": (pt["types"], render_type, "prototype"),
    }
    n = 0
    for cat, (items, renderer, tag) in renderers.items():
        folder, prefix, default_tag = CAT_DEFS[cat]
        for item in items:
            base = registry[cat][item["name"]][1]
            relpath = f"{folder}/{base}.md"
            content = frontmatter(item["name"], tags_for(cat)) + renderer(item)
            write_note(relpath, content)
            n += 1
    return n


def generate_mocs():
    for cat, (folder, prefix, tag) in CAT_DEFS.items():
        items = [registry[cat][name][1] for name in registry[cat]]
        if not items:
            continue
        title = {
            "class": "Classes", "event": "Events", "concept": "Concepts",
            "define": "Defines", "object": "Objects", "function": "Functions",
            "prototype": "Prototypes", "type": "Types",
        }[cat]
        # MOC files live next to their folder.
        moc_rel = {
            "class": "Runtime/Classes.md", "event": "Runtime/Events.md",
            "concept": "Runtime/Concepts.md", "define": "Runtime/Defines.md",
            "object": "Runtime/Objects.md", "function": "Runtime/Functions.md",
            "prototype": "Prototype/Prototypes.md", "type": "Prototype/Types.md",
        }[cat]
        write_note(moc_rel, render_moc(title, cat, items))
    # Guides MOC (guide notes are generated separately).
    if GUIDE_NAMES:
        write_note("Guides.md", render_moc("Guides", "guide", GUIDE_NAMES))


# ---------------------------------------------------------------------------
# Auxiliary HTML -> markdown
# ---------------------------------------------------------------------------

def convert_auxiliary():
    aux_dir = AUX_DIR
    if not os.path.isdir(aux_dir):
        eprint("No auxiliary dir found; skipping guides.")
        return
    files = sorted(f for f in os.listdir(aux_dir) if f.endswith(".html"))

    for f in files:
        name = f[:-5]
        with open(os.path.join(aux_dir, f), encoding="utf-8") as fh:
            html = fh.read()
        m = re.search(r"<main[^>]*>(.*?)</main>", html, re.S)
        if m:
            content = m.group(1)
        else:
            m = re.search(r"<body[^>]*>(.*?)</body>", html, re.S)
            content = m.group(1) if m else html
        # Drop the little self-link icons next to headings.
        content = re.sub(r'<a[^>]*class="[^"]*\blink\b[^"]*"[^>]*>.*?</a>', "", content, flags=re.S)
        # Normalize code language classes for pandoc.
        content = re.sub(r'class="language-(\w+)"', r'class="\1"', content)
        content = re.sub(r'<pre class="highlight">', "<pre>", content)

        md = subprocess.run(
            ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
            input=content, capture_output=True, text=True,
        ).stdout
        md = postprocess_aux(md)
        write_note(f"Guides/{name}.md", frontmatter(name, ["factorio-api", "guide"]) + md.lstrip() + "\n")


def aux_target(href):
    """Map an auxiliary-page href to (base, anchor), or None if not a known note."""
    if href.startswith(("http://", "https://", "mailto:", "ftp://", "//")):
        return None
    if href.startswith("#"):
        return None
    t = href
    anchor = None
    if "#" in t:
        t, anchor = t.split("#", 1)
    t = t.replace(".html", "")
    parts = [p for p in t.split("/") if p and p not in ("..",)]
    base = parts[-1] if parts else ""
    if not base:
        return None
    if base in ("index", "index-runtime", "index-prototype", "index-auxiliary"):
        base = "Factorio API"
    elif base in ("classes", "concepts", "events", "defines", "types", "prototypes"):
        base = base.capitalize()
    if (base not in by_basename and base not in GUIDE_NAMES
            and base not in MOC_NAMES and base != "Factorio API"):
        return None
    return (base, anchor)


def _wikilink_from(base, anchor, text):
    w = base + (("#" + anchor) if anchor else "")
    alias = (text or "").strip().replace("`", "").strip()
    if (alias and alias != base and "[" not in alias and "]" not in alias
            and "#" not in alias and "|" not in alias
            and re.fullmatch(r"[\w .:'\-\"()]+", alias)):
        return f"[[{w}|{alias}]]"
    return f"[[{w}]]"


def postprocess_aux(md):
    # 1) Markdown-style images -> Obsidian embeds.
    def img(m):
        src = m.group(2)
        base = src.rstrip("/").split("/")[-1]
        return f"![[{base}]]"
    md = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", img, md)

    # 2) Raw <img> tags -> Obsidian embeds.
    def raw_img(m):
        src = re.search(r'src="([^"]+)"', m.group(0))
        if not src:
            return m.group(0)
        base = src.group(1).rstrip("/").split("/")[-1]
        return f"![[{base}]]"
    md = re.sub(r"<img\b[^>]*>", raw_img, md)

    # 3) Raw <a href> tags -> wikilinks.
    def raw_a(m):
        href = re.search(r'href="([^"]+)"', m.group(0))
        if not href:
            return m.group(0)
        r = aux_target(href.group(1))
        if not r:
            return m.group(0)
        inner = re.sub(r"<[^>]+>", "", re.sub(r"^<a\b[^>]*>", "", m.group(0)))
        inner = inner.replace("</a>", "")
        return _wikilink_from(r[0], r[1], inner)
    md = re.sub(r"<a\b[^>]*>.*?</a>", raw_a, md, flags=re.S)

    # 4) Markdown links -> wikilinks.
    def link(m):
        txt, target = m.group(1), m.group(2)
        if target.startswith(("http://", "https://", "mailto:", "ftp://", "//")):
            return m.group(0)
        if target.startswith("#"):
            return m.group(0)
        r = aux_target(target)
        if not r:
            return m.group(0)
        return _wikilink_from(r[0], r[1], txt)
    md = re.sub(r"\[([^\]]*)\]\(([^)]+)\)", link, md)
    return md


def copy_images():
    dst = os.path.join(OUTPUT_DIR, "attachments")
    os.makedirs(dst, exist_ok=True)
    copied = 0
    for sub in ("static/images", "static"):
        src_dir = os.path.join(INPUT_DIR, sub)
        if not os.path.isdir(src_dir):
            continue
        for fn in os.listdir(src_dir):
            if fn.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")):
                shutil.copy2(os.path.join(src_dir, fn), os.path.join(dst, fn))
                copied += 1
    eprint(f"Copied {copied} images to attachments/")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Guard against MOC / Home / guide note names colliding with entity names.
    reserved = MOC_NAMES | {"Factorio API"} | GUIDE_NAMES
    clash = reserved & set(by_basename)
    if clash:
        eprint(f"ERROR: reserved note names collide with entities: {sorted(clash)}")
        sys.exit(1)
    n = generate_json_notes()
    eprint(f"Wrote {n} entity notes")
    generate_mocs()
    eprint("Wrote MOC index notes")
    write_note("Factorio API.md", render_home())
    eprint("Wrote Home note")
    convert_auxiliary()
    eprint(f"Wrote {len(GUIDE_NAMES)} guide notes")
    copy_images()
    total = sum(len(fs) for _, _, fs in os.walk(OUTPUT_DIR))
    eprint(f"Total files written: {total}")


if __name__ == "__main__":
    main()
