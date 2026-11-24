---
title: ItemPrototype
tags: [factorio-api, prototype]
---
# ItemPrototype

> **Parent:** [[Prototype]] · **Type name:** `item`

Possible configuration for all items.

## Properties

### stack_size
- **Type:** [[ItemCountType (type)]]
Count of items of the same name that can be stored in one inventory slot. Must be 1 when the `"not-stackable"` flag is set.
**Examples:**

```
stack_size = 64
```

### icons
- **Type:** array<[[IconData]]>
- **Optional**
Can't be an empty array.

### icon
- **Type:** [[FileName]]
- **Optional**
Path to the icon file.

Only loaded, and mandatory if `icons` is not defined.

### icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

Only loaded if `icons` is not defined.

### dark_background_icons
- **Type:** array<[[IconData]]>
- **Optional**
Can't be an empty array.

### dark_background_icon
- **Type:** [[FileName]]
- **Optional**
If this is set, it is used to show items in alt-mode instead of the normal item icon. This can be useful to increase the contrast of the icon with the dark alt-mode [[UtilityConstants (prototype)#item_outline_color|icon outline]].

Path to the icon file.

Only loaded if `dark_background_icons` is not defined.

### dark_background_icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

Only loaded if `dark_background_icons` is not defined.

### place_result
- **Type:** [[EntityID (type)]]
- **Optional**
- **Default:** `""`
Name of the [[EntityPrototype]] that can be built using this item. If this item should be the one that construction bots use to build the specified `place_result`, set the `"primary-place-result"` [[ItemPrototypeFlags (type)|item flag]].

The localised name of the entity will be used as the in-game item name. This behavior can be overwritten by specifying `localised_name` on this item, it will be used instead.
**Examples:**

```
place_result = "wooden-chest"
```

### place_as_equipment_result
- **Type:** [[EquipmentID (type)]]
- **Optional**
- **Default:** `""`

### fuel_categories
- **Type:** array<[[FuelCategoryID]]>
- **Optional**
Mandatory with at least one fuel category when a nonzero fuel_value is defined.

### burnt_result
- **Type:** [[ItemID (type)]]
- **Optional**
- **Default:** `""`
The item that is the result when this item gets burned as fuel.

### spoil_result
- **Type:** [[ItemID (type)]]
- **Optional**
- **Requires:** `space_age`
Only loaded if `spoil_ticks` is larger than 0.

### spoil_quality_min
- **Type:** [[QualityID (type)]]
- **Optional**
- **Requires:** `space_age`
Only loaded if `spoil_ticks` is larger than 0.

The minimum quality level that can be reached when [[ItemPrototype#spoil_quality_change|spoil_quality_change]] is used.

### spoil_quality_max
- **Type:** [[QualityID (type)]]
- **Optional**
- **Requires:** `space_age`
Only loaded if `spoil_ticks` is larger than 0.

The maximum quality level that can be reached when [[ItemPrototype#spoil_quality_change|spoil_quality_change]] is used.

### spoil_quality_change
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `0`
- **Requires:** `space_age`
Only loaded if `spoil_ticks` is larger than 0.

Defines how many levels the item's quality will go up (positive integer) or down (negative integer) when spoiling.

### plant_result
- **Type:** [[EntityID (type)]]
- **Optional**

### place_as_tile
- **Type:** [[PlaceAsTile]]
- **Optional**

### pictures
- **Type:** [[SpriteVariations]]
- **Optional**
Used to give the item multiple different icons so that they look less uniform on belts. For inventory icons and similar, `icon/icons` will be used. Maximum number of variations is 16.

When using sprites of size `64` (same as base game icons), the `scale` should be set to 0.5.

### flags
- **Type:** [[ItemPrototypeFlags (type)]]
- **Optional**
Specifies some properties of the item.
**Examples:**

```
flags = { "hide-from-bonus-gui" }
```

### spoil_ticks
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
- **Requires:** `space_age`

### quality_affects_spoil_ticks
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Requires:** `space_age`
Only loaded if `spoil_ticks` is larger than 0.

If set, [[QualityPrototype#spoil_ticks_multiplier|QualityPrototype::spoil_ticks_multiplier]] will be applied to spoil_tick value.

### fuel_value
- **Type:** [[Energy]]
- **Optional**
- **Default:** `"0J"`
Amount of energy the item gives when used as fuel.

Mandatory if `fuel_acceleration_multiplier`, `fuel_top_speed_multiplier` or `fuel_emissions_multiplier` or `fuel_glow_color` are used.
**Examples:**

```
fuel_value = "12MJ"
```

### fuel_acceleration_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1.0`
Must be 0 or positive.

### fuel_top_speed_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1.0`
Must be 0 or positive.

### fuel_emissions_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1.0`

### fuel_acceleration_multiplier_quality_bonus
- **Type:** [[double (type)]]
- **Optional**
Additional fuel acceleration multiplier per quality level. Defaults to 30% of `fuel_acceleration_multiplier - 1` if `fuel_acceleration_multiplier` is larger than 1. Otherwise defaults to 0.

Must be 0 or positive.

### fuel_top_speed_multiplier_quality_bonus
- **Type:** [[double (type)]]
- **Optional**
Additional fuel top speed multiplier per quality level. Defaults to 30% of `fuel_top_speed_multiplier - 1` if `fuel_top_speed_multiplier` is larger than 1. Otherwise defaults to 0.

Must be 0 or positive.

### weight
- **Type:** [[Weight (type)]]
- **Optional**
The default weight is calculated automatically from recipes and falls back to [[UtilityConstants (prototype)#default_item_weight|UtilityConstants::default_item_weight]].

More information on how item weight is determined can be found on its [[item-weight|auxiliary page]].

### ingredient_to_weight_coefficient
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.5`

### space_platform_request_priority
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Used by space platforms to prioritize item requests and make sure there is enough space for priority items before requesting the rest.

### fuel_glow_color
- **Type:** [[Color (type)]]
- **Optional**
Colors the glow of the burner energy source when this fuel is burned. Can also be used to color the glow of reactors burning the fuel, see [[ReactorPrototype#use_fuel_glow_color|ReactorPrototype::use_fuel_glow_color]].

### open_sound
- **Type:** [[Sound]]
- **Optional**

### close_sound
- **Type:** [[Sound]]
- **Optional**

### pick_sound
- **Type:** [[Sound]]
- **Optional**

### drop_sound
- **Type:** [[Sound]]
- **Optional**

### inventory_move_sound
- **Type:** [[Sound]]
- **Optional**

### default_import_location
- **Type:** [[SpaceLocationID (type)]]
- **Optional**
- **Default:** `"nauvis"`

### color_hint
- **Type:** [[ColorHintSpecification (type)]]
- **Optional**
Only used by hidden setting, support may be limited.

### has_random_tint
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### spoil_to_trigger_result
- **Type:** [[SpoilToTriggerResult (type)]]
- **Optional**
- **Requires:** `space_age`
Only loaded if `spoil_ticks` is larger than 0.

### destroyed_by_dropping_trigger
- **Type:** [[Trigger]]
- **Optional**
The effect/trigger that happens when an item is destroyed by being dropped on a [[TilePrototype]] marked as destroying dropped items.

This overrides the [[TilePrototype#default_destroyed_dropped_item_trigger|TilePrototype::default_destroyed_dropped_item_trigger]] from the tile.

### rocket_launch_products
- **Type:** array<[[ItemProductPrototype]]>
- **Optional**

### send_to_orbit_mode
- **Type:** [[SendToOrbitMode]]
- **Optional**
- **Default:** `"not-sendable"`
The way this item works when we try to send it to the orbit on its own.

When "manual" is set, it can only be launched by pressing the launch button in the rocket silo.

When "automated" is set, it will force the existence of "launch to orbit automatically" checkbox in the rocket silo which will then force the silo to automatically send the item to orbit when present.

### moved_to_hub_when_building
- **Type:** [[boolean (type)]]
- **Optional**
Whether this item should be moved to the hub when space platform performs building, upgrade or deconstruction and is left with this item. The following items are considered valuable and moved to hub by default: [[ModulePrototype|Modules]], [[ItemPrototype#place_result|items that build entities]], [[ItemPrototype#place_as_tile|items that build tiles]] and items [[AsteroidChunkPrototype#minable|not obtainable from asteroid chunks]] that have [[PrototypeBase#subgroup|subgroup]] from a [[ItemSubGroup#group|group]] other than `"intermediate-products"`.

### random_tint_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** Value of UtilityConstants::item_default_random_tint_strength
Randomly tints item instances on belts and in the world. 0 no tinting. 1 full tint.

### spoil_level
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
Used by Inserters with spoil priority. Item with higher spoil level is considered more spoiled than item with lower spoil level regardless of progress of spoiling.

### auto_recycle
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the item should be included in the self-recycling recipes automatically generated by the quality mod.

This property is not read by the game engine itself, but the quality mod's data-updates.lua file. This means it is discarded by the game engine after loading finishes.

### hidden
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Overrides parent**
Item will not appear in lists of all items such as those for logistics requests, filters, etc.

### lab_ignores_spoil_percent
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### science_capacity
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
Used by labs. Not relevant for [[ToolPrototype|tools]] where [[ToolPrototype#durability|durability]] is used.

Must be >= 0.01.
