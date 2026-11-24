---
title: table_size
tags: [factorio-api, runtime, global-function]
---
# table_size

Factorio provides the `table_size()` function as a simple way to determine the size of tables with non-continuous keys, as the standard `#` operator does not work correctly for these. The function is a C++ implementation of the following Lua code, which is faster than doing the same in Lua:

```
local function size(t)
  local count = 0
  for k,v in pairs(t) do
    count = count + 1
  end
  return count
end
```

Note that `table_size()` does not work correctly for [[LuaCustomTable]], their size has to be determined with [[LuaCustomTable#length_operator|LuaCustomTable::length_operator]] instead.

**Parameters:**
- **`table`** — [[table]]

**Returns:**
- [[uint32]]
