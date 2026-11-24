---
title: CharacterCorpsePrototype
tags: [factorio-api, prototype]
---
# CharacterCorpsePrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `character-corpse`

The corpse of a [[CharacterPrototype]].

## Properties

### time_to_live
- **Type:** [[uint32 (type)]]
In ticks. 0 for infinite.

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### pictures
- **Type:** [[AnimationVariations]]
- **Optional**
Mandatory if `picture` is not defined.

### picture
- **Type:** [[Animation]]
- **Optional**
Only loaded, and mandatory if `pictures` is not defined.

### armor_picture_mapping
- **Type:** dictionary<[[ItemID (type)]] → [[int32 (type)]]>
- **Optional**
A mapping of [[ArmorPrototype]] name to a number. The number is the Animation that is associated with the armor, e.g. using `1` will associate the armor with the first Animation in the `pictures` table.

This mapping can be empty to have no sprite changes based on armor.
