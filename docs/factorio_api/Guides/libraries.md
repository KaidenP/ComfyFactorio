---
title: libraries
tags: [factorio-api, guide]
---
## Libraries and functions

Factorio adds several functions and libraries to the Lua environment that cannot be found in standard . Furthermore, it modifies several functions to be deterministic, notably `pairs()` and `math.random()`.

------------------------------------------------------------------------

### Libraries

#### • serpent

Factorio provides the as a global variable named `serpent` for all mods to use. Its purpose is to allow for easy printing of Lua tables (using `serpent.block()` for example), which can be useful when debugging. It can't pretty-print LuaObjects such as [[LuaEntity]] however.

The serpent library was modified for determinism, e.g. comments are turned off by default to avoid returning table addresses. Furthermore, two options were added: `refcomment` (true/false/maxlevel) and `tablecomment` (true/false/maxlevel), which allow to separately control the self-reference and table value output of the `comment` option.

#### • string

The `string` library has the functions `pack`, `packsize` and `unpack` backported from for handling .

------------------------------------------------------------------------

### New functions

#### • log(LocalisedString)

`log()` can print [[LocalisedString|LocalisedStrings]] to the Factorio . This, in combination with the serpent library, makes debugging in the data stage easier because it allows the inspection of entire prototype tables. For example, printing all properties of the sulfur item prototype can be done like so: `log(serpent.block(data.raw["item"]["sulfur"]))`

#### • localised_print(LocalisedString)

`localised_print()` allows printing [[LocalisedString]] to stdout without polluting the Factorio . This is primarily useful when communicating with external tools that launch Factorio as a child process.

#### • table_size(table) → uint32

Factorio provides the `table_size()` function as a simple way to determine the size of tables with non-continuous keys, as the standard `#` operator does not work correctly for these. The function is a C++ implementation of the following Lua code, which is faster than doing the same in Lua:

<div class="codehilite" style="background: #263238">

```
local function size(t)
  local count = 0
  for k,v in pairs(t) do
    count = count + 1
  end
  return count
end
```

</div>

Note that `table_size()` does not work correctly for [[LuaCustomTable]], their size has to be determined with [[LuaCustomTable#length_operator|LuaCustomTable::length_operator]] instead.

------------------------------------------------------------------------

### Modified functions

Some modules that are part of standard Lua are not accessible in Factorio's Lua environment, mostly to ensure determinism. These inaccessible modules are: `loadfile()`, `dofile()`, `coroutine`, `io` and `os`. Factorio provides its own versions of `package` and `debug`.

#### • pairs() / next()

In standard Lua, the order of iteration when using `pairs()` is arbitrary. Because Factorio has to be deterministic, this was changed in Factorio's version of Lua. Factorio's iteration order when using `next()` (which `pairs()` uses for iteration) depends on the insertion order: Keys inserted first are iterated first.

Factorio however also guarantees that the first 1024 numbered keys are iterated from 1 to 1024, regardless of insertion order. This means that for common uses, `pairs()` does not have any drawbacks compared to `ipairs()`.

#### • require()

Due to the changes to `package`, the functionality of `require()` changes. When using absolute paths, the path starts at the mod root. Additionally, `..` and `.` are disabled as path variables. This means that it is not possible to load arbitrary files from outside the mod directory.

Factorio does however provide two ways to load files from other mods:

- The "lualib" directory of the core mod is included in the paths to be checked for files, so it is possible to require files directly from there, such as the "util" file by using `require("util")`.
- Furthermore, it is possible to require files from other mods by using `require("__mod-name__.file")`.

`require()` can not be used in the console, in event listeners or during a `remote.call()`. The function expects any file to end with the `.lua` extension.

#### • print()

`print()` outputs to stdout. For Factorio, this means that it does not end up in the log file, so it can only be read when starting Factorio from the command line. Because of this, it is often easier to use `log()` or [[LuaGameScript#print|LuaGameScript::print]] for debugging.

#### • math.random()

`math.random()` is reimplemented within Factorio to be deterministic, both in the data stage and during runtime.

In the data stage, it is seeded with a constant number. During runtime, it uses the map's global random generator which is seeded with the map seed. The map's global random generator is shared between all mods and the core game, which all affect the random number that is generated. If this behaviour is not desired, [[LuaRandomGenerator]] can be used to create a random generator that is completely separate from the core game and other mods.

This method can't be used outside of events or during loading. Calling it with non-integer arguments will floor them instead of resulting in an error.

#### • math.randomseed()

Using `math.randomseed()` in Factorio has no effect on the random generator, the function does nothing. If custom seeding or re-seeding is desired, [[LuaRandomGenerator]] can be used instead of `math.random()`.

#### • load()

`load()` will not load binary chunks; the `mode` argument has no effect.

#### • debug

In the `debug` module, only `debug.getinfo()` and `debug.traceback()` are available by default. For advanced debug use, access to the potentially unsafe functions in the rest of the standard Lua debug module can be re-enabled with a command line option.

#### • debug.getinfo()

`debug.getinfo()` supports an additional flag `p` which fills in `currentpc` with the index of the current instruction within the function at the given stack level, or `-1` for functions not on the call stack. All standard fields are also supported.

#### • Mathematical functions

All trigonometric, hyperbolic, exponential and logarithmic Lua functions have been replaced by custom implementations to ensure determinism across platforms. For standard uses, they behave equivalently.

