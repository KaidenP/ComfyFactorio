---
title: DebugVariablesFilter
tags: [factorio-api, runtime, concept]
---
# DebugVariablesFilter

## Fields

### filter
- **Type:** `"indexed"` | `"named"` | `"all"`
- **Optional**
The kind of filter applied to this request. Default "all".

### start
- **Type:** [[int32]]
- **Optional**
When `filter` is "indexed", the index to start at.

### count
- **Type:** [[int32]]
- **Optional**
When `filter` is "indexed", the size of the requested page.
