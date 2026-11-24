---
title: SimpleEntityWithOwnerPrototype
tags: [factorio-api, prototype]
---
# SimpleEntityWithOwnerPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `simple-entity-with-owner`

Has a force, but unlike [[SimpleEntityWithForcePrototype]] it is only attacked if the biters get stuck on it (or if [[EntityWithOwnerPrototype#is_military_target|EntityWithOwnerPrototype::is_military_target]] set to true to make the two entity types equivalent).

Can be rotated in 4 directions. `picture` can be used to specify different graphics per direction.

## Properties

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### secondary_draw_order
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `0`
Used to determine render order for entities with the same `render_layer` in the same position. Entities with a higher `secondary_draw_order` are drawn on top.

### random_animation_offset
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### random_variation_on_create
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether a random graphics variation is chosen when placing the entity/creating it via script/creating it via map generation. If this is false, the entity will use the first variation instead of a random one.

### pictures
- **Type:** [[SpriteVariations]]
- **Optional**
Takes priority over `picture` and `animations`.

### picture
- **Type:** [[Sprite4Way]]
- **Optional**
Takes priority over `animations`.

### animations
- **Type:** [[AnimationVariations]]
- **Optional**

### lower_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"lower-object"`

### lower_pictures
- **Type:** [[SpriteVariations]]
- **Optional**
Loaded and drawn with all `pictures`, `picture` and `animations`. If graphics variation is larger than number of `lower_pictures` variations this layer is not drawn.

### stateless_visualisation_variations
- **Type:** array<[[StatelessVisualisation]] | array<[[StatelessVisualisation]]>>
- **Optional**

### force_visibility
- **Type:** [[ForceCondition (type)]]
- **Optional**
- **Default:** `"all"`
If the entity is not visible to a player, the player cannot select it.
