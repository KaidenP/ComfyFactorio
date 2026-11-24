---
title: LuaRecord
tags: [factorio-api, runtime, class]
---
# LuaRecord

A reference to a record in the blueprint library. Records in the "my blueprints" shelf are read-only, but records in the "game blueprints" shelf are read/write.

## Attributes

### valid_for_write
- **Type:** [[boolean]]
Is this record valid for writing? A record is invalid for write if it is a BlueprintRecord preview or if it is in the "My blueprints" shelf.

### prototype
- **Type:** [[LuaItemPrototype]]

### name
- **Type:** [[string]]

### type
- **Type:** `"blueprint"` | `"blueprint-book"` | `"deconstruction-planner"` | `"upgrade-planner"`
The type of this blueprint record.

### shelf_index
- **Type:** [[uint32]]
Identifier of the shelf this record is in. May correspond to a player index or be a special value when in game blueprints.

### record_id
- **Type:** [[uint32]]
Identifier of the record within its shelf.

### preview_icons
- **Type:** array<[[BlueprintSignalIcon]]>
- **Writable:** array<[[BlueprintSignalIcon]]>
The preview icons for this record.

### is_preview
- **Type:** [[boolean]]
Checks if this record is in a preview state.

### blueprint_snap_to_grid
- **Type:** [[TilePosition]]
- **Writable:** [[TilePosition]]
- **Optional**
The snapping grid size in this blueprint. `nil` if snapping is not enabled.

### blueprint_position_relative_to_grid
- **Type:** [[TilePosition]]
- **Writable:** [[TilePosition]]
- **Optional**
The offset from the absolute grid. `nil` if absolute snapping is not enabled.

### blueprint_absolute_snapping
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If absolute snapping is enabled on this blueprint.

### blueprint_description
- **Type:** [[string]]
- **Writable:** [[string]]
The description for this blueprint or blueprint book.

### cost_to_build
- **Type:** array<[[ItemWithQualityCount]]>
List of raw materials required to build this blueprint.

### default_icons
- **Type:** array<[[BlueprintSignalIcon]]>
The default icons for a blueprint blueprint.

### contents
- **Type:** dictionary<[[ItemStackIndex]] → [[LuaRecord]]>
The contents of this BlueprintBookRecord. This is sparse array - it may have gaps, so using `#` will not be reliable. Use [[LuaRecord#contents_size|LuaRecord::contents_size]] or `pairs()` to iterate this table.

### contents_size
- **Type:** [[ItemStackIndex]]
The highest populated index in the contents of this BlueprintBookRecord.

### entity_filters
- **Type:** array<[[ItemFilter]]>
- **Writable:** array<[[ItemFilter]]>
The entity filters for this deconstruction planner. The attribute is a sparse array with the keys representing the index of the filter. All prototypes in this array must not have the `"not-deconstructable"` flag set and are either a `cliff` or marked as `minable`.

### tile_filters
- **Type:** array<[[TileID]]>
- **Writable:** array<[[TileID]]>
The tile filters for this deconstruction planner. The attribute is a sparse array with the keys representing the index of the filter. Reading filters always returns an array of strings which are the tile prototype names.

### entity_filter_mode
- **Type:** [[defines.deconstruction_item#entity_filter_mode]]
- **Writable:** [[defines.deconstruction_item#entity_filter_mode]]
The blacklist/whitelist entity filter mode for this deconstruction planner.

### tile_filter_mode
- **Type:** [[defines.deconstruction_item#tile_filter_mode]]
- **Writable:** [[defines.deconstruction_item#tile_filter_mode]]
The blacklist/whitelist tile filter mode for this deconstruction planner.

### tile_selection_mode
- **Type:** [[defines.deconstruction_item#tile_selection_mode]]
- **Writable:** [[defines.deconstruction_item#tile_selection_mode]]
The tile selection mode for this deconstruction planner.

### trees_and_rocks_only
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this deconstruction planner, is set to allow trees and rocks only.

### entity_filter_count
- **Type:** [[uint32]]
The number of entity filters this deconstruction planner has.

### tile_filter_count
- **Type:** [[uint32]]
The number of tile filters this deconstruction planner has.

### mapper_count
- **Type:** [[uint32]]
The current count of mappers in the upgrade item.

### label
- **Type:** [[string]]
- **Writable:** [[string]]
- **Optional**
The current label for this record, if any.

### planner_description
- **Type:** [[string]]
- **Writable:** [[string]]
The description for this deconstruction planner or upgrade planner.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### export_record
Exports this record to a string.

**Returns:**
- [[string]]

### clear_blueprint
Clears this blueprint.
*Only available on:* `BlueprintRecord`

### is_blueprint_setup
Is this blueprint setup? I.e. is it a non-empty blueprint?
*Only available on:* `BlueprintRecord`

**Returns:**
- [[boolean]]

### build_blueprint
Build this blueprint at the given location.

Built entities can be come invalid between the building of the blueprint and the function returning if by_player or raise_built is used and one of those events invalidates the entity.
*Only available on:* `BlueprintRecord`

Takes a table with the following fields:
- **`surface`** — [[SurfaceIdentification]]: Surface to build on
- **`force`** — [[ForceID]]: Force to use for the building
- **`position`** — [[MapPosition]]: The position to build at
- **`direction`** — [[defines.direction]] *(optional)*: The direction to use when building
- **`build_mode`** — [[defines.build_mode]] *(optional)*: If `normal`, blueprint will not be built if any one thing can't be built. If `forced`, anything that can be built is built and obstructing nature entities will be deconstructed. If `superforced`, all obstructions will be deconstructed and the blueprint will be built.
- **`skip_fog_of_war`** — [[boolean]] *(optional)*: If chunks covered by fog-of-war are skipped.
- **`by_player`** — [[PlayerIdentification]] *(optional)*: The player to use if any. If provided [[defines.events#on_built_entity|defines.events.on_built_entity]] will be fired for new entities and [[defines.events#on_blueprint_settings_pasted|defines.events.on_blueprint_settings_pasted]] will be fired for existing entities that are updated.
- **`raise_built`** — [[boolean]] *(optional)*: If true; [[defines.events#script_raised_built|defines.events.script_raised_built]] will be fired for new entities and [[defines.events#on_blueprint_settings_pasted|defines.events.on_blueprint_settings_pasted]] will be fired for existing entities that are updated. Note: this is ignored if by_player is provided.

**Returns:**
- array<[[LuaEntity]]>: Array of created ghosts

### create_blueprint
Sets up this blueprint using the found blueprintable entities/tiles on the surface.
*Only available on:* `BlueprintRecord`

Takes a table with the following fields:
- **`surface`** — [[SurfaceIdentification]]: Surface to create from
- **`force`** — [[ForceID]]: Force to use for the creation
- **`area`** — [[BoundingBox]]: The bounding box
- **`always_include_tiles`** — [[boolean]] *(optional)*: When true, blueprintable tiles are always included in the blueprint. When false they're only included if no entities exist in the setup area. Defaults to false.
- **`include_entities`** — [[boolean]] *(optional)*: When true, entities are included in the blueprint. Defaults to true.
- **`include_modules`** — [[boolean]] *(optional)*: When true, modules are included in the blueprint. Defaults to true.
- **`include_station_names`** — [[boolean]] *(optional)*: When true, station names are included in the blueprint. Defaults to false.
- **`include_trains`** — [[boolean]] *(optional)*: When true, trains are included in the blueprint. Defaults to false.
- **`include_fuel`** — [[boolean]] *(optional)*: When true, train fuel is included in the blueprint, Defaults to true.

**Returns:**
- dictionary<[[uint32]] → [[LuaEntity]]>: The blueprint entity index to source entity mapping.

### get_blueprint_entity_tags
Gets the tags for the given blueprint entity index in this blueprint.
*Only available on:* `BlueprintRecord`

**Parameters:**
- **`index`** — [[uint32]]

**Returns:**
- [[Tags]] *(optional)*

### set_blueprint_entity_tags
Sets the tags on the given blueprint entity index in this blueprint.
*Only available on:* `BlueprintRecord`

**Parameters:**
- **`index`** — [[uint32]]: The entity index
- **`tags`** — [[Tags]]

### get_blueprint_entity_tag
Gets the given tag on the given blueprint entity index in this blueprint.
*Only available on:* `BlueprintRecord`

**Parameters:**
- **`index`** — [[uint32]]: The entity index.
- **`tag`** — [[string]]: The tag to get.

**Returns:**
- [[AnyBasic]] *(optional)*

### set_blueprint_entity_tag
Sets the given tag on the given blueprint entity index in this blueprint.
*Only available on:* `BlueprintRecord`

**Parameters:**
- **`index`** — [[uint32]]: The entity index.
- **`tag`** — [[string]]: The tag to set.
- **`value`** — [[AnyBasic]]: The tag value to set or `nil` to clear the tag.

### get_blueprint_entities
The entities in this blueprint.
*Only available on:* `BlueprintRecord`

**Returns:**
- array<[[BlueprintEntity]]> *(optional)*

### set_blueprint_entities
Set new entities to be a part of this blueprint.
*Only available on:* `BlueprintRecord`

**Parameters:**
- **`entities`** — array<[[BlueprintEntity]]>: The new blueprint entities.
- **`fix_positions`** — [[boolean]] *(optional)*: If false, positions will be left unchanged unless invalid for the current snapping.

### get_blueprint_tiles
A list of the tiles in this blueprint.
*Only available on:* `BlueprintRecord`

**Returns:**
- array<[[Tile]]> *(optional)*

### set_blueprint_tiles
Set specific tiles in this blueprint.
*Only available on:* `BlueprintRecord`

**Parameters:**
- **`tiles`** — array<[[Tile]]>: Tiles to be a part of the blueprint.

### get_blueprint_entity_count
Gets the number of entities in this blueprint blueprint.
*Only available on:* `BlueprintRecord`

**Returns:**
- [[uint32]]

### get_active_index
The active index of this BlueprintBookRecord. For records in "my blueprints", the result will be the same regardless of the player, but records in "game blueprints" may have different active indices per player.
*Only available on:* `BlueprintBookRecord`

**Parameters:**
- **`player`** — [[PlayerIdentification]]

**Returns:**
- [[uint32]]

### get_selected_record
Gets the currently selected record of the book for the given player.

Note: this will return a record even if the book is in a preview state.
*Only available on:* `BlueprintBookRecord`

**Parameters:**
- **`player`** — [[PlayerIdentification]]

**Returns:**
- [[LuaRecord]] *(optional)*

### get_entity_filter
Gets the entity filter at the given index for this deconstruction planner.
*Only available on:* `DeconstructionRecord`

**Parameters:**
- **`index`** — [[uint32]]

**Returns:**
- [[ItemFilter]] *(optional)*

### set_entity_filter
Sets the entity filter at the given index for this deconstruction planner.
*Only available on:* `DeconstructionRecord`

**Parameters:**
- **`index`** — [[uint32]]
- **`filter`** — [[ItemFilter]] | [[nil]]: Writing `nil` removes the filter.

**Returns:**
- [[boolean]]: Whether the new filter was successfully set (ie. was valid).

### get_tile_filter
Gets the tile filter at the given index for this deconstruction planner.
*Only available on:* `DeconstructionRecord`

**Parameters:**
- **`index`** — [[uint32]]

**Returns:**
- [[string]] *(optional)*

### set_tile_filter
Sets the tile filter at the given index for this deconstruction planner.
*Only available on:* `DeconstructionRecord`

**Parameters:**
- **`index`** — [[uint32]]
- **`filter`** — [[string]] | [[LuaTilePrototype]] | [[LuaTile]]: Setting to nil erases the filter.

**Returns:**
- [[boolean]]: Whether the new filter was successfully set (ie. was valid).

### deconstruct_area
Deconstruct the given area with this deconstruction planner.
*Only available on:* `DeconstructionRecord`

Takes a table with the following fields:
- **`surface`** — [[SurfaceIdentification]]: Surface to deconstruct on
- **`force`** — [[ForceID]]: Force to use for the deconstruction
- **`area`** — [[BoundingBox]]: The area to deconstruct
- **`skip_fog_of_war`** — [[boolean]] *(optional)*: If chunks covered by fog-of-war are skipped. Defaults to `false`.
- **`by_player`** — [[PlayerIdentification]] *(optional)*: The player to use if any.
- **`super_forced`** — [[boolean]] *(optional)*: If the deconstruction is super-forced. Defaults to `false`.

### cancel_deconstruct_area
Cancel deconstruct the given area with this deconstruction planner.
*Only available on:* `DeconstructionRecord`

Takes a table with the following fields:
- **`surface`** — [[SurfaceIdentification]]: Surface to cancel deconstruct on
- **`force`** — [[ForceID]]: Force to use for canceling deconstruction
- **`area`** — [[BoundingBox]]: The area to deconstruct
- **`skip_fog_of_war`** — [[boolean]] *(optional)*: If chunks covered by fog-of-war are skipped. Defaults to `false`.
- **`by_player`** — [[PlayerIdentification]] *(optional)*: The player to use if any.
- **`super_forced`** — [[boolean]] *(optional)*: If the cancel deconstruction is super-forced. Defaults to `false`.

### clear_deconstruction_data
Clears all settings/filters on this deconstruction planner, resetting it to default values.
*Only available on:* `DeconstructionRecord`

### clear_upgrade_data
Clears all settings/filters on this upgrade planner, resetting it to default values.
*Only available on:* `UpgradeRecord`

### get_mapper
Gets the filter at the given index for this upgrade item. Note that sources (`"from"` type) that are undefined will read as `{type = "item"}`, while destinations (`"to"` type) that are undefined will read as `nil`.

In contrast to [[LuaRecord#set_mapper|LuaRecord::set_mapper]], indices past the upgrade item's current size are considered to be out of bounds.
*Only available on:* `UpgradeRecord`

**Parameters:**
- **`index`** — [[uint32]]: The index of the mapper to read.
- **`type`** — `"from"` | `"to"`

**Returns:**
- [[UpgradeMapperSource]] | [[UpgradeMapperDestination]]

### set_mapper
Sets the module filter at the given index for this upgrade item.

In contrast to [[LuaRecord#get_mapper|LuaRecord::get_mapper]], indices past the upgrade item's current size are valid and expand the list of mappings accordingly, if within reasonable bounds.
*Only available on:* `UpgradeRecord`

**Parameters:**
- **`index`** — [[uint32]]: The index of the mapper to set.
- **`type`** — `"from"` | `"to"`
- **`mapper`** — [[UpgradeMapperSource]] | [[UpgradeMapperDestination]] | [[nil]]: The mapper to set. Set `nil` to clear the mapper.
