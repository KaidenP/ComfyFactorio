---
title: HighlightBoxEntityPrototype
tags: [factorio-api, prototype]
---
# HighlightBoxEntityPrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `highlight-box`

Used to attach graphics for [[CursorBoxType|cursor boxes]] to entities during runtime. HighlightBoxEntity can also be independent from entities so it is simply drawn somewhere in the world. See [[LuaSurface#create_entity|LuaSurface::create_entity]] for the available options for type "highlight-box".

The [[EntityPrototype#collision_box|collision_box]] of the highlight box prototype is ignored during runtime, instead the "bounding_box" given in create_entity() or the selection box of the target entity is used.

## Properties

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
