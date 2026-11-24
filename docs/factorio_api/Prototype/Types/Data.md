---
title: Data
tags: [factorio-api, prototype, type]
---
# Data

> **Abstract**

The data table is read by the game to load all prototypes.

At the end of the prototype stage, the data table is loaded by the game engine and the format of the prototypes is validated. Any extra properties are ignored. See [[data-lifecycle|Data Lifecycle]] for more information.

The data table and its properties are defined in Lua, so their source code can be viewed in [dataloader.lua](https://github.com/wube/factorio-data/blob/master/core/lualib/dataloader.lua).

## Properties

### raw
- **Type:** dictionary<[[string (type)]] → dictionary<[[string (type)]] → [[AnyPrototype]]>>
A dictionary of prototype types to values that themselves are dictionaries of prototype names to specific prototypes.

This means that individual prototypes can be accessed with `local prototype = data.raw["prototype-type"]["internal-name"]`.
**Examples:**

```
-- set the stack size of coal to be 1000
data.raw["item"]["coal"].stack_size = 1000
```

```
-- get the max health of the wooden chest
local health = data.raw["container"]["wooden-chest"].max_health
```

### extend
- **Type:** [[DataExtendMethod]]
The primary way to add prototypes to the data table.
**Examples:**

```
local not_coal =
{
  type = "item",
  name = "a-thing",
  icon = "__base__/graphics/icons/coal.png",
  icon_size = 64,
  stack_size = 2
}
local proto2 =
{
  type = "fuel-category",
  name = "best-fuel"
}
data:extend({not_coal, proto2})
```

### is_demo
- **Type:** [[boolean (type)]]
Set by the game based on whether the demo or retail version is running. Should not be used by mods.
