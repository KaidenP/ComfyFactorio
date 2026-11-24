---
title: SimpleEntityPrototype
tags: [factorio-api, prototype]
---
# SimpleEntityPrototype

> **Parent:** [[EntityWithHealthPrototype]] · **Type name:** `simple-entity`

An extremely basic entity with no special functionality. Used for minable rocks. Cannot be rotated.

## Properties

### count_as_rock_for_filtered_deconstruction
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether this entity should be treated as a rock for the purpose of deconstruction and for [[CarPrototype#immune_to_rock_impacts|CarPrototype::immune_to_rock_impacts]].

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
Whether a random graphics variation is chosen when placing the entity/creating it via script/creating it via map generation. If this is `false`, the entity will use the first variation instead of a random one.

### shuffled_variation_on_chunk_generated
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If true, map generator will shuffle graphics variations for each chunk and pick the next one in sequence instead of making it purely position-based. This prevents identical entity variations from being too close to each other. This property overrides random_variation_on_create.

### pictures
- **Type:** [[SpriteVariations]]
- **Optional**
Takes priority over `picture` and `animations`.

### picture
- **Type:** [[Sprite4Way]]
- **Optional**
Takes priority over `animations`. Only the `north` sprite is used because this entity cannot be rotated.

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

### stateless_visualisation_variations
- **Type:** array<[[StatelessVisualisation]] | array<[[StatelessVisualisation]]>>
- **Optional**
Loaded and drawn with all `pictures`, `picture` and `animations`. If graphics variation is larger than number of `lower_pictures` variations this layer is not drawn.
