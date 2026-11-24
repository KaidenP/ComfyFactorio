---
title: ToolPrototype
tags: [factorio-api, prototype]
---
# ToolPrototype

> **Parent:** [[ItemPrototype]] · **Type name:** `tool`

Items with a "durability".

## Properties

### durability
- **Type:** [[double (type)]]
- **Optional**
The durability of this tool. Must be positive. Mandatory if `infinite` is false. Ignored if <code>infinite</code> is true.

### durability_description_key
- **Type:** [[string (type)]]
- **Optional**
May not be longer than 200 characters.

### durability_description_value
- **Type:** [[string (type)]]
- **Optional**
May not be longer than 200 characters.

In-game, the game provides the locale with three [parameters](https://wiki.factorio.com/Tutorial:Localisation#Localising_with_parameters):

`__1__`: remaining durability

`__2__`: total durability

`__3__`: durability as a percentage

So when a locale key that has the following translation

`Remaining durability is __1__ out of __2__ which is __3__ %`

is applied to a tool with 2 remaining durability out of 8 it will be displayed as

`Remaining durability is 2 out of 8 which is 25 %`

### infinite
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether this tool has infinite durability. If this is false, `durability` must be specified.
