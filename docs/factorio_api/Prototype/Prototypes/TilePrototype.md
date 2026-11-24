---
title: TilePrototype
tags: [factorio-api, prototype]
---
# TilePrototype

> **Parent:** [[Prototype]] · **Type name:** `tile` · **Instance limit:** 65535

A [tile](https://wiki.factorio.com/Tile).

## Properties

### collision_mask
- **Type:** [[TileCollisionMaskConnector]]

### layer
- **Type:** [[uint8 (type)]]
Specifies transition drawing priority. This represents the positive offset from this tile's `layer_group`. Internally, the final layer is computed as `layer_group + layer` (a [[uint16 (type)|uint16]]), wrapping back to `"zero"` after the `"top"` layer.

### layer_group
- **Type:** [[TileRenderLayer]]
- **Optional**
- **Default:** `"ground-natural"`
The base group of render layers this tile belongs to. It can be moved up inside this group using the `layer` property. See the [[TileRenderLayer]] page to see the sizes of all layer groups.

### build_animations
- **Type:** [[Animation4Way]]
- **Optional**
The build animation used when this tile is built on a space platform.

### build_animations_background
- **Type:** [[Animation4Way]]
- **Optional**

### built_animation_frame
- **Type:** [[uint32 (type)]]
- **Optional**
When the build_animations frame reaches this point the tile is built.

Mandatory if `build_animations` is defined.

### variants
- **Type:** [[TileTransitionsVariants]]
Graphics for this tile.

### map_color
- **Type:** [[Color (type)]]

### icons
- **Type:** array<[[IconData]]>
- **Optional**
Can't be an empty array. If this and `icon` is not set, the `material_background` in `variants` is used as the icon.

### icon
- **Type:** [[FileName]]
- **Optional**
Path to the icon file. If this and `icons` is not set, the `material_background` in `variants` is used as the icon.

Only loaded if `icons` is not defined.

### icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

Only loaded if `icons` is not defined.

### lowland_fog
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
For surfaces that use [[SurfaceRenderParameters (type)#fog|fog effect]] of type `gleba`, this property determines whether given tile should contribute to fog intensity on a chunk or not.

### transition_overlay_layer_offset
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `0`

### sprite_usage_surface
- **Type:** [[SpriteUsageSurfaceHint]]
- **Optional**
- **Default:** `"any"`

### transition_merges_with_tile
- **Type:** [[TileID (type)]]
- **Optional**

### effect_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{r=1, g=1, b=1, a=1} (white)`

### tint
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{r=1, g=1, b=1, a=1} (white)`

### particle_tints
- **Type:** [[TileBasedParticleTints]]
- **Optional**

### walking_sound
- **Type:** [[Sound]]
- **Optional**

### landing_steps_sound
- **Type:** [[Sound]]
- **Optional**

### driving_sound
- **Type:** [[InterruptibleSound]]
- **Optional**

### build_sound
- **Type:** [[Sound]] | [[TileBuildSound]]
- **Optional**
If this is loaded as one Sound, it is loaded as the "small" build sound.

### mined_sound
- **Type:** [[Sound]]
- **Optional**

### walking_speed_modifier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`

### vehicle_friction_modifier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`

### decorative_removal_probability
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`

### allowed_neighbors
- **Type:** array<[[TileID (type)]]>
- **Optional**
- **Default:** All tiles
Array of tile names that are allowed next to this one.

### needs_correction
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether the tile needs tile correction logic applied when it's generated in the world, to prevent graphical artifacts. The tile correction logic disallows 1-wide stripes of the tile, see [Friday Facts #346](https://factorio.com/blog/post/fff-346).

### minable
- **Type:** [[MinableProperties]]
- **Optional**
If you want the tile to not be mineable, don't specify the minable property. Only non-mineable tiles become hidden tiles when placing mineable tiles on top of them.

### fluid
- **Type:** [[FluidID (type)]]
- **Optional**

### next_direction
- **Type:** [[TileID (type)]]
- **Optional**

### can_be_part_of_blueprint
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### is_foundation
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### destroys_dropped_items
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If items dropped on this tile are destroyed.

### allows_being_covered
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### searchable
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### max_health
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Must be equal to or greater than 0.

### weight
- **Type:** [[Weight (type)]]
- **Optional**
- **Default:** `0`
Mass which this tile adds to total space platform mass when placed.

### dying_explosion
- **Type:** [[ExplosionDefinition (type)]] | array<[[ExplosionDefinition (type)]]>
- **Optional**
Triggers when a foundation tile is destroyed by an asteroid.

### absorptions_per_second
- **Type:** dictionary<[[AirbornePollutantID]] → [[double (type)]]>
- **Optional**

### default_cover_tile
- **Type:** [[TileID (type)]]
- **Optional**

### frozen_variant
- **Type:** [[TileID (type)]]
- **Optional**

### thawed_variant
- **Type:** [[TileID (type)]]
- **Optional**

### effect
- **Type:** [[TileEffectDefinitionID]]
- **Optional**

### trigger_effect
- **Type:** [[TriggerEffect]]
- **Optional**
Called by [[InvokeTileEffectTriggerEffectItem]].

### default_destroyed_dropped_item_trigger
- **Type:** [[Trigger]]
- **Optional**
The effect/trigger that runs when an item is destroyed by being dropped on this tile.

If the item defines [[ItemPrototype#destroyed_by_dropping_trigger|its own trigger]] it will override this.

If this is defined, `destroys_dropped_items` must be `true`.

### scorch_mark_color
- **Type:** [[Color (type)]]
- **Optional**

### check_collision_with_entities
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If set to true, the game will check for collisions with entities before building or mining the tile. If entities are in the way it is not possible to mine/build the tile.

### effect_color_secondary
- **Type:** [[Color (type)]]
- **Optional**
Used by the [pollution](https://wiki.factorio.com/Pollution) shader.

### effect_is_opaque
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** true if `effect_color` alpha equals 1

### transitions
- **Type:** array<[[TileTransitionsToTiles]]>
- **Optional**
Extra transitions.

### transitions_between_transitions
- **Type:** array<[[TileTransitionsBetweenTransitions]]>
- **Optional**

### autoplace
- **Type:** [[AutoplaceSpecification (type)]]
- **Optional**

### placeable_by
- **Type:** [[ItemToPlace (type)]] | array<[[ItemToPlace (type)]]>
- **Optional**

### bound_decoratives
- **Type:** [[DecorativeID (type)]] | array<[[DecorativeID (type)]]>
- **Optional**

### ambient_sounds_group
- **Type:** [[TileID (type)]]
- **Optional**

### ambient_sounds
- **Type:** [[WorldAmbientSoundDefinition]] | array<[[WorldAmbientSoundDefinition]]>
- **Optional**
