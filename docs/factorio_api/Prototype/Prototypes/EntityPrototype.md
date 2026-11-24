---
title: EntityPrototype
tags: [factorio-api, prototype]
---
# EntityPrototype

> **Parent:** [[Prototype]] · **Abstract**

Abstract base of all entities in the game. Entity is nearly everything that can be on the map (except tiles).

For in game script access to entity, take a look at [[LuaEntity]].

## Properties

### icons
- **Type:** array<[[IconData]]>
- **Optional**
This will be used in the electric network statistics, editor building selection, and the bonus gui. Can't be an empty array.

Either this or `icon` is mandatory for entities that have at least one of these flags active: `"placeable-neutral"`, `"placeable-player`", `"placeable-enemy"`.

### icon
- **Type:** [[FileName]]
- **Optional**
Path to the icon file.

Either this or `icons` is mandatory for entities that have at least one of these flags active: `"placeable-neutral"`, `"placeable-player`", `"placeable-enemy"`.

Only loaded if `icons` is not defined.
**Examples:**

```
icon = "__base__/graphics/icons/wooden-chest.png"
```

### icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

Only loaded if `icons` is not defined.

### collision_box
- **Type:** [[BoundingBox (type)]]
- **Optional**
- **Default:** Empty = `{{0, 0}, {0, 0}}`
Specification of the entity collision boundaries. Empty collision box means no collision and is used for smoke, projectiles, particles, explosions etc.

The `{0,0}` coordinate in the collision box will match the entity position. It should be near the center of the collision box, to keep correct entity drawing order. The bounding box must include the `{0,0}` coordinate.

Note, that for buildings, it is customary to leave 0.1 wide border between the edge of the tile and the edge of the building, this lets the player move between the building and electric poles/inserters etc.
**Examples:**

```
collision_box = {{-0.4, -0.4}, {0.4, 0.4}}
```

### collision_mask
- **Type:** [[CollisionMaskConnector]]
- **Optional**
Defaults to the mask from [[UtilityConstants (prototype)#default_collision_masks|UtilityConstants::default_collision_masks]] when indexed by the entity type.

### map_generator_bounding_box
- **Type:** [[BoundingBox (type)]]
- **Optional**
- **Default:** The value of collision_box.
Used instead of the collision box during map generation. Allows space entities differently during map generation, for example if the box is bigger, the entities will be placed farther apart.

### selection_box
- **Type:** [[BoundingBox (type)]]
- **Optional**
- **Default:** Empty = `{{0, 0}, {0, 0}}`
Specification of the entity selection area. When empty the entity will have no selection area (and thus is not selectable).

The selection box is usually a little bit bigger than the collision box. For tileable entities (like buildings) it should match the tile size of the building.
**Examples:**

```
selection_box = {{-0.5, -0.5}, {0.5, 0.5}}
```

### drawing_box_vertical_extension
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.0`
Specification of extra vertical space needed to see the whole entity in GUIs. This is used to calculate the correct zoom and positioning in the entity info gui, for example in the entity tooltip.
**Examples:**

```
drawing_box_vertical_extension = 0.5
```

### sticker_box
- **Type:** [[BoundingBox (type)]]
- **Optional**
- **Default:** The value of collision_box.
Used to specify the area where the [[StickerPrototype|sticker]] animation can appear for entities that can have stickers on them.
**Examples:**

```
sticker_box = {{-0.5, -0.5}, {0.5, 0.5}}
```

### hit_visualization_box
- **Type:** [[BoundingBox (type)]]
- **Optional**
- **Default:** Empty = `{{0, 0}, {0, 0}}`
Where beams should hit the entity. Useful if the bounding box only covers part of the entity (e.g. feet of the character) and beams only hitting there would look weird.

### trigger_target_mask
- **Type:** [[TriggerTargetMask (type)]]
- **Optional**
Defaults to the mask from [[UtilityConstants (prototype)#default_trigger_target_mask_by_type|UtilityConstants::default_trigger_target_mask_by_type]].

### flags
- **Type:** [[EntityPrototypeFlags (type)]]
- **Optional**

### tile_buildability_rules
- **Type:** array<[[TileBuildabilityRule (type)]]>
- **Optional**

### minable
- **Type:** [[MinableProperties]]
- **Optional**
- **Default:** not minable
The item given to the player when they mine the entity and other properties relevant to mining this entity.
**Examples:**

```
minable = {mining_time = 0.2, result = "boiler"}
```

### surface_conditions
- **Type:** array<[[SurfaceCondition (type)]]>
- **Optional**
- **Requires:** `space_age`

### deconstruction_alternative
- **Type:** [[EntityID (type)]]
- **Optional**
Used to merge multiple entities into one entry in the deconstruction planner.

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `50`
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.

### build_grid_size
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `1`
Supported values are 1 (for 1x1 grid) and 2 (for 2x2 grid, like rails).

Internally forced to be `2` for [[RailPrototype]], [[RailRemnantsPrototype]], [[TrainStopPrototype]], [[RailSupportPrototype]] and [[CargoBayPrototype]].

Internally forced to be `256` for [[SpacePlatformHubPrototype]].

### remove_decoratives
- **Type:** `"automatic"` | `"true"` | `"false"`
- **Optional**
- **Default:** `"automatic"`
Whether this entity should remove decoratives that collide with it when this entity is built. When set to "automatic", if the entity type is considered [[LuaEntityPrototype#is_building|a building]] (e.g. an assembling machine or a wall) it will remove decoratives.

### emissions_per_second
- **Type:** dictionary<[[AirbornePollutantID]] → [[double (type)]]>
- **Optional**
Amount of emissions created (positive number) or cleaned (negative number) every second by the entity. This is passive and currently used just for trees and fires. This is independent of the [[BaseEnergySource#emissions_per_minute|emissions of energy sources]] used by machines, which are created actively depending on the power consumption.

### shooting_cursor_size
- **Type:** [[double (type)]]
- **Optional**
The cursor size used when shooting at this entity.

### created_smoke
- **Type:** [[CreateTrivialSmokeEffectItem]]
- **Optional**
- **Default:** The "smoke-building"-smoke
The smoke that is shown when the entity is placed.

### working_sound
- **Type:** [[WorkingSound]]
- **Optional**
Will also work on entities that don't actually do work.

### created_effect
- **Type:** [[Trigger]]
- **Optional**
The effect/trigger that happens when the entity is placed.

### build_sound
- **Type:** [[Sound]]
- **Optional**

### mined_sound
- **Type:** [[Sound]]
- **Optional**

### mining_sound
- **Type:** [[Sound]]
- **Optional**

### rotated_sound
- **Type:** [[Sound]]
- **Optional**

### ghost_build_sound
- **Type:** [[Sound]]
- **Optional**

### impact_category
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `"default"`
Name of a [[ImpactCategory]].

### open_sound
- **Type:** [[Sound]]
- **Optional**

### close_sound
- **Type:** [[Sound]]
- **Optional**

### placeable_position_visualization
- **Type:** [[Sprite]]
- **Optional**

### radius_visualisation_specification
- **Type:** [[RadiusVisualisationSpecification (type)]]
- **Optional**
**Examples:**

```
radius_visualisation_specification =
{
  sprite =
  {
    filename = "__base__/graphics/entity/electric-mining-drill/electric-mining-drill-radius-visualization.png",
    size = 10
  },
  distance = 6
}
```

### stateless_visualisation
- **Type:** [[StatelessVisualisation]] | array<[[StatelessVisualisation]]>
- **Optional**

### draw_stateless_visualisations_in_ghost
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### alert_icon_shift
- **Type:** [[Vector (type)]]
- **Optional**

### alert_icon_scale
- **Type:** [[float (type)]]
- **Optional**

### fast_replaceable_group
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `""`
This allows you to replace an entity that's already placed, with a different one in your inventory. For example, replacing a burner inserter with a fast inserter. The replacement entity can be a different rotation to the replaced entity and you can replace an entity with the same type.

This is simply a string, so any string can be used here. The entity that should be replaced simply has to use the same string here.

Entities with the same fast replaceable group can be configured as upgrades for each other in the upgrade planner. Refer to the [[UpgradeItemPrototype|upgrade planner prototype's page]] the full requirements for entities to be shown in the upgrade planner.

### next_upgrade
- **Type:** [[EntityID (type)]]
- **Optional**
Name of the entity that will be automatically selected as the upgrade of this entity when using the [[UpgradeItemPrototype|upgrade planner]] without configuration.

This entity may not have "not-upgradable" flag set and must be minable. This entity mining result must not contain item product with [[ItemPrototype#hidden|hidden]] set to `true`. Mining results with no item products are allowed. This entity may not be a [[RollingStockPrototype]].

The upgrade target entity needs to have the same bounding box, collision mask, and fast replaceable group as this entity. The upgrade target entity must have least 1 item that builds it that isn't hidden.
**Examples:**

```
next_upgrade = "fast-inserter"
```

### protected_from_tile_building
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
When this is true, this entity prototype should be included during tile collision checks with tiles that have [[TilePrototype#check_collision_with_entities|TilePrototype::check_collision_with_entities]] set to true.

### tall
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When this is true, this entity prototype will be translucent and unselectable when "Hide tall entities" mode is active.

Rail signals are always treated as 'tall' when built attached to elevated rails.

### show_fluid_visualization_when_in_cursor
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When this is true, fluid pipelines will be visualized when this entity is held in the cursor.

### heating_energy
- **Type:** [[Energy]]
- **Optional**
- **Default:** `"0W"`
- **Requires:** `space_age`
This entity can freeze if heating_energy is larger than zero.

### allow_copy_paste
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### selectable_in_game
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### placeable_by
- **Type:** [[ItemToPlace (type)]] | array<[[ItemToPlace (type)]]>
- **Optional**
Item that when placed creates this entity. Determines which item is picked when "Q" (smart pipette) is used on this entity. Determines which item and item amount is needed in a blueprint of this entity and to revive a ghost of this entity.

The item count specified here can't be larger than the stack size of that item.
**Examples:**

```
placeable_by = {item = "rail", count = 4}
```

### remains_when_mined
- **Type:** [[EntityID (type)]] | array<[[EntityID (type)]]>
- **Optional**
The entity that remains when this one is mined, deconstructed or fast-replaced. The entity wont actually be spawned if it would collide with the entity that is in the process of being mined.

### additional_pastable_entities
- **Type:** array<[[EntityID (type)]]>
- **Optional**
Names of the entity prototypes this entity prototype can be pasted on to in addition to the standard supported types.

This is used to allow copying between types that aren't compatible on the C++ code side, by allowing mods to receive the [[on_entity_settings_pasted]] event for the given entity and do the setting pasting via script.
**Examples:**

```
additional_pastable_entities = {"steel-chest", "iron-chest"}
```

### tile_width
- **Type:** [[int32 (type)]]
- **Optional**
- **Default:** calculated by the collision box width rounded up.
Used to determine how the center of the entity should be positioned when building (unless the off-grid [[EntityPrototypeFlags (type)|flag]] is specified).

When the tile width is odd, the center will be in the center of the tile, when it is even, the center is on the tile transition.

### tile_height
- **Type:** [[int32 (type)]]
- **Optional**
- **Default:** calculated by the collision box height rounded up.

### diagonal_tile_grid_size
- **Type:** [[TilePosition (type)]]
- **Optional**

### autoplace
- **Type:** [[AutoplaceSpecification (type)]]
- **Optional**
- **Default:** nil (entity is not autoplacable)
Used to specify the rules for placing this entity during map generation.

### map_color
- **Type:** [[Color (type)]]
- **Optional**

### friendly_map_color
- **Type:** [[Color (type)]]
- **Optional**

### enemy_map_color
- **Type:** [[Color (type)]]
- **Optional**

### water_reflection
- **Type:** [[WaterReflectionDefinition]]
- **Optional**
May also be defined inside `graphics_set` instead of directly in the entity prototype. This is useful for entities that use a `graphics_set` property to define their graphics, because then all graphics can be defined in one place.

[Currently only renders](https://forums.factorio.com/100703) for [[EntityWithHealthPrototype]] and [[CorpsePrototype]].

### ambient_sounds_group
- **Type:** [[EntityID (type)]]
- **Optional**

### ambient_sounds
- **Type:** [[WorldAmbientSoundDefinition]] | array<[[WorldAmbientSoundDefinition]]>
- **Optional**

### icon_draw_specification
- **Type:** [[IconDrawSpecification (type)]]
- **Optional**
Used to specify where and how the alt-mode icons should be drawn.
**Examples:**

```
icon_draw_specification = {shift = {0, 0.5}, scale = 0.75, scale_for_many = 0.5, render_layer = "entity-info-icon"}
```

### icons_positioning
- **Type:** array<[[IconSequencePositioning (type)]]>
- **Optional**
**Examples:**

```
icons_positioning =
{
  {inventory_index = defines.inventory.lab_modules, shift = {0, 0.9}},
  {inventory_index = defines.inventory.lab_input, shift = {0, 0.0}, max_icons_per_row = 6, separation_multiplier = 0.9}
}
```

### order
- **Type:** [[Order]]
- **Optional**
- **Overrides parent**
Used to order prototypes in inventory, recipes and GUIs. May not exceed a length of 200 characters.

The order string is taken from the items in `placeable_by` if they exist, or from an item that has its [[ItemPrototype#place_result|place_result]] set to this entity.

## Example

```
{
  type = "container",
  name = "wooden-chest",
  icon = "__base__/graphics/icons/wooden-chest.png",
  flags = { "placeable-neutral", "player-creation" },
  minable = { mining_time = 1, result = "wooden-chest" },
  max_health = 100,
  corpse = "small-remnants",
  collision_box = { {-0.35, -0.35}, {0.35, 0.35} },
  fast_replaceable_group = "container",
  selection_box = { {-0.5, -0.5}, {0.5, 0.5} },
  inventory_size = 16,
  open_sound = { filename = "__base__/sound/wooden-chest-open.ogg" },
  close_sound = { filename = "__base__/sound/wooden-chest-close.ogg" },
  picture =
  {
    filename = "__base__/graphics/entity/wooden-chest/wooden-chest.png",
    priority = "extra-high",
    width = 46,
    height = 33,
    shift = {0.25, 0.015625}
  }
}
```
