---
title: DestroyDecorativesTriggerEffectItem
tags: [factorio-api, prototype, type]
---
# DestroyDecorativesTriggerEffectItem

> **Parent:** [[TriggerEffectItem (type)]]

## Properties

### type
- **Type:** `"destroy-decoratives"`

### radius
- **Type:** [[float (type)]]

### from_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** first layer

### to_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** last layer

### include_soft_decoratives
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Soft decoratives are those where [[DecorativePrototype#grows_through_rail_path|DecorativePrototype::grows_through_rail_path]] is `true`.

### include_decals
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### invoke_decorative_trigger
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### decoratives_with_trigger_only
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `true`, only decoratives with a [[DecorativePrototype#trigger_effect|DecorativePrototype::trigger_effect]] will be destroyed.
