---
title: ModData
tags: [factorio-api, prototype]
---
# ModData

> **Parent:** [[Prototype]] · **Type name:** `mod-data`

Block of arbitrary data set by mods in prototype stage.

During runtime stage, this arbitrary data can be accessed through [[LuaPrototypes#mod_data|LuaPrototypes::mod_data]].

## Properties

### data_type
- **Type:** [[string (type)]]
- **Optional**
Arbitrary string that mods can use to declare type of data. Can be used for mod compatibility when one mod declares block of data that is expected to be discovered by another mod.
**Examples:**

```
data_type = "my-mod.my_structure"
```

### data
- **Type:** dictionary<[[string (type)]] → [[AnyBasic (type)]]>

## Example

```
{
  type = "mod-data",
  name = "my-own-great-mod-data",
  data_type = "my-mod.my-data-type",
  data =
  {
    a_string = "a string",
    a_number = 6.7,
    a_table = {x=2, y=3, z="yes"},
    a_bool = true,
  }
}
```
