---
title: LuaItemCommon
tags: [factorio-api, runtime, class]
---
# LuaItemCommon

> **Abstract class** — not directly instantiable.

Common methods related to usage of item with data. It is useful when LuaItemStack contains item with data or in general with LuaItem as it can only point at an item with data.

## Attributes

### is_blueprint
- **Type:** [[boolean]]
If this is a blueprint item.

### is_blueprint_book
- **Type:** [[boolean]]
If this is a blueprint book item.

### is_item_with_label
- **Type:** [[boolean]]
If this is an item with label item.

### is_item_with_inventory
- **Type:** [[boolean]]
If this is an item with inventory item.

### is_item_with_entity_data
- **Type:** [[boolean]]
If this is an item with entity data item.

### is_selection_tool
- **Type:** [[boolean]]
If this is a selection tool item.

### is_item_with_tags
- **Type:** [[boolean]]
If this is an item with tags item.

### is_deconstruction_item
- **Type:** [[boolean]]
If this is a deconstruction tool item.

### is_upgrade_item
- **Type:** [[boolean]]
If this is a upgrade item.

### is_tool
- **Type:** [[boolean]]
If this is a tool item.

### is_ammo
- **Type:** [[boolean]]
If this is an ammo item.

### is_armor
- **Type:** [[boolean]]
If this is an armor item.

### is_repair_tool
- **Type:** [[boolean]]
If this is a repair tool item.

### item_number
- **Type:** [[uint64]]
- **Optional**
The unique identifier for this item, if any. Note that this ID stays the same no matter where the item is moved to.

### preview_icons
- **Type:** array<[[BlueprintSignalIcon]]>
- **Writable:** array<[[BlueprintSignalIcon]]>
- **Optional**
Icons of this blueprint item, blueprint book, deconstruction item or upgrade planner. An item that doesn't have icons returns `nil` on read and throws error on write.

### grid
- **Type:** [[LuaEquipmentGrid]]
- **Optional**
The equipment grid of this item, if any.

### owner_location
- **Type:** [[ItemLocationData]]
The location of this item if it can be found.

### blueprint_snap_to_grid
- **Type:** [[TilePosition]]
- **Writable:** [[TilePosition]]
- **Optional**
The snapping grid size in this blueprint item. `nil` if snapping is not enabled.

### blueprint_position_relative_to_grid
- **Type:** [[TilePosition]]
- **Writable:** [[TilePosition]]
- **Optional**
The offset from the absolute grid. `nil` if absolute snapping is not enabled.

### blueprint_absolute_snapping
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If absolute snapping is enabled on this blueprint item.

### blueprint_description
- **Type:** [[string]]
- **Writable:** [[string]]
The description for this blueprint or blueprint book

### cost_to_build
- **Type:** array<[[ItemWithQualityCount]]>
List of raw materials required to build this blueprint.

### default_icons
- **Type:** array<[[BlueprintSignalIcon]]>
The default icons for a blueprint item.

### active_index
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
- **Optional**
The active blueprint index for this blueprint book. `nil` if this blueprint book is empty.

### label
- **Type:** [[string]]
- **Writable:** [[string]]
- **Optional**
The current label for this item, if any.

### label_color
- **Type:** [[Color]]
- **Writable:** [[Color]]
- **Optional**
The current label color for this item, if any.

### allow_manual_label_change
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether the label for this item can be manually changed. When false the label can only be changed through the API.

### entity_label
- **Type:** [[string]]
- **Writable:** [[string]]
- **Optional**
If this is an item with entity data, get the stored entity label.

### entity_color
- **Type:** [[Color]]
- **Writable:** [[Color]]
- **Optional**
If this is an item with entity data, get the stored entity color.

### entity_logistic_sections
- **Type:** [[LogisticSections]]
- **Writable:** [[LogisticSections]]
If this is an item with entity data, get the stored logistic filters.

### entity_request_from_buffers
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this is an item with entity data, get the stored request from buffer state.

### entity_logistics_enabled
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this is an item with entity data, get the stored vehicle logistics enabled state.

### entity_enable_logistics_while_moving
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this is an item with entity data, get the stored enable logistics while moving state.

### entity_driver_is_gunner
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this is an item with entity data, get the stored driver is gunner state.

### entity_auto_target_without_gunner
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this is an item with entity data, get the stored auto target without gunner state.

### entity_auto_target_with_gunner
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this is an item with entity data, get the stored auto target with gunner state.

### tags
- **Type:** [[Tags]]
- **Writable:** [[Tags]]

### custom_description
- **Type:** [[LocalisedString]]
- **Writable:** [[LocalisedString]]
The custom description this item-with-tags. This is shown over the normal item description if this is set to a non-empty value.

### entity_filter_count
- **Type:** [[uint32]]
The number of entity filters this deconstruction item has.

### entity_filters
- **Type:** array<[[ItemFilter]]>
- **Writable:** array<[[ItemFilter]]>
The entity filters for this deconstruction item. The attribute is a sparse array with the keys representing the index of the filter. All prototypes in this array must not have the `"not-deconstructable"` flag set and are either a `cliff` or marked as `minable`.

### tile_filter_count
- **Type:** [[uint32]]
The number of tile filters this deconstruction item has.

### tile_filters
- **Type:** array<[[TileID]]>
- **Writable:** array<[[TileID]]>
The tile filters for this deconstruction item. The attribute is a sparse array with the keys representing the index of the filter. Reading filters always returns an array of strings which are the tile prototype names.

### entity_filter_mode
- **Type:** [[defines.deconstruction_item#entity_filter_mode]]
- **Writable:** [[defines.deconstruction_item#entity_filter_mode]]
The blacklist/whitelist entity filter mode for this deconstruction item.

### tile_filter_mode
- **Type:** [[defines.deconstruction_item#tile_filter_mode]]
- **Writable:** [[defines.deconstruction_item#tile_filter_mode]]
The blacklist/whitelist tile filter mode for this deconstruction item.

### tile_selection_mode
- **Type:** [[defines.deconstruction_item#tile_selection_mode]]
- **Writable:** [[defines.deconstruction_item#tile_selection_mode]]
The tile selection mode for this deconstruction item.

### trees_and_rocks_only
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this deconstruction item is set to allow trees and rocks only.

### mapper_count
- **Type:** [[uint32]]
The current count of mappers in the upgrade item.

### planner_description
- **Type:** [[string]]
- **Writable:** [[string]]
The description for this deconstruction planner or upgrade planner

### durability
- **Type:** [[double]]
- **Writable:** [[double]]
Durability of the contained item. Automatically capped at the item's maximum durability.

### ammo
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
Number of bullets left in the magazine.

## Methods

### get_inventory
Access the inner inventory of an item.

**Parameters:**
- **`inventory`** — [[defines.inventory]]: Index of the inventory to access, which can only be [[defines.inventory#item_main|defines.inventory.item_main]].

**Returns:**
- [[LuaInventory]] *(optional)*: `nil` if there is no inventory with the given index.

### clear_blueprint
Clears this blueprint item.
*Only available on:* `BlueprintItem`

### is_blueprint_setup
Is this blueprint item setup? I.e. is it a non-empty blueprint?
*Only available on:* `BlueprintItem`

**Returns:**
- [[boolean]]

### build_blueprint
Build this blueprint at the given location.

Built entities can be come invalid between the building of the blueprint and the function returning if by_player or raise_built is used and one of those events invalidates the entity.
*Only available on:* `BlueprintItem`

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
*Only available on:* `BlueprintItem`

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
Gets the tags for the given blueprint entity index in this blueprint item.
*Only available on:* `BlueprintItem`

**Parameters:**
- **`index`** — [[uint32]]

**Returns:**
- [[Tags]] *(optional)*

### set_blueprint_entity_tags
Sets the tags on the given blueprint entity index in this blueprint item.
*Only available on:* `BlueprintItem`

**Parameters:**
- **`index`** — [[uint32]]: The entity index
- **`tags`** — [[Tags]]

### get_blueprint_entity_tag
Gets the given tag on the given blueprint entity index in this blueprint item.
*Only available on:* `BlueprintItem`

**Parameters:**
- **`index`** — [[uint32]]: The entity index.
- **`tag`** — [[string]]: The tag to get.

**Returns:**
- [[AnyBasic]] *(optional)*

### set_blueprint_entity_tag
Sets the given tag on the given blueprint entity index in this blueprint item.
*Only available on:* `BlueprintItem`

**Parameters:**
- **`index`** — [[uint32]]: The entity index.
- **`tag`** — [[string]]: The tag to set.
- **`value`** — [[AnyBasic]]: The tag value to set or `nil` to clear the tag.

### get_blueprint_entities
The entities in this blueprint.
*Only available on:* `BlueprintItem`

**Returns:**
- array<[[BlueprintEntity]]> *(optional)*

### set_blueprint_entities
Set new entities to be a part of this blueprint.
*Only available on:* `BlueprintItem`

**Parameters:**
- **`entities`** — array<[[BlueprintEntity]]>: The new blueprint entities.
- **`fix_positions`** — [[boolean]] *(optional)*: If false, positions will be left unchanged unless invalid for the current snapping.

### get_blueprint_tiles
A list of the tiles in this blueprint.
*Only available on:* `BlueprintItem`

**Returns:**
- array<[[Tile]]> *(optional)*

### set_blueprint_tiles
Set specific tiles in this blueprint.
*Only available on:* `BlueprintItem`

**Parameters:**
- **`tiles`** — array<[[Tile]]>: Tiles to be a part of the blueprint.

### get_blueprint_entity_count
Gets the number of entities in this blueprint item.
*Only available on:* `BlueprintItem`

**Returns:**
- [[uint32]]

### get_tag
Gets the tag with the given name or returns `nil` if it doesn't exist.
*Only available on:* `ItemWithTags`

**Parameters:**
- **`tag_name`** — [[string]]

**Returns:**
- [[AnyBasic]] *(optional)*

### set_tag
Sets the tag with the given name and value.
*Only available on:* `ItemWithTags`

**Parameters:**
- **`tag_name`** — [[string]]
- **`tag`** — [[AnyBasic]]

### remove_tag
Removes a tag with the given name.
*Only available on:* `ItemWithTags`

**Parameters:**
- **`tag`** — [[string]]

**Returns:**
- [[boolean]]: If the tag existed and was removed.

### get_tag_names
Gets the names of all tags on this item.
*Only available on:* `ItemWithTags`

**Returns:**
- array<[[string]]>

### get_entity_filter
Gets the entity filter at the given index for this deconstruction item.
*Only available on:* `DeconstructionItem`

**Parameters:**
- **`index`** — [[uint32]]

**Returns:**
- [[ItemFilter]] *(optional)*

### set_entity_filter
Sets the entity filter at the given index for this deconstruction item.
*Only available on:* `DeconstructionItem`

**Parameters:**
- **`index`** — [[uint32]]
- **`filter`** — [[ItemFilter]] | [[nil]]: Writing `nil` removes the filter.

**Returns:**
- [[boolean]]: Whether the new filter was successfully set (meaning it was valid).

### get_tile_filter
Gets the tile filter at the given index for this deconstruction item.
*Only available on:* `DeconstructionItem`

**Parameters:**
- **`index`** — [[uint32]]

**Returns:**
- [[string]] *(optional)*

### set_tile_filter
Sets the tile filter at the given index for this deconstruction item.
*Only available on:* `DeconstructionItem`

**Parameters:**
- **`index`** — [[uint32]]
- **`filter`** — [[string]] | [[LuaTilePrototype]] | [[LuaTile]] | [[nil]]: Writing `nil` removes the filter.

**Returns:**
- [[boolean]]: Whether the new filter was successfully set (meaning it was valid).

### deconstruct_area
Deconstruct the given area with this deconstruction item.
*Only available on:* `DeconstructionItem`

Takes a table with the following fields:
- **`surface`** — [[SurfaceIdentification]]: Surface to deconstruct on
- **`force`** — [[ForceID]]: Force to use for the deconstruction
- **`area`** — [[BoundingBox]]: The area to deconstruct
- **`skip_fog_of_war`** — [[boolean]] *(optional)*: If chunks covered by fog-of-war are skipped. Defaults to `false`.
- **`by_player`** — [[PlayerIdentification]] *(optional)*: The player to use if any.
- **`super_forced`** — [[boolean]] *(optional)*: If the deconstruction is super-forced. Defaults to `false`.

### cancel_deconstruct_area
Cancel deconstruct the given area with this deconstruction item.
*Only available on:* `DeconstructionItem`

Takes a table with the following fields:
- **`surface`** — [[SurfaceIdentification]]: Surface to cancel deconstruct on
- **`force`** — [[ForceID]]: Force to use for canceling deconstruction
- **`area`** — [[BoundingBox]]: The area to deconstruct
- **`skip_fog_of_war`** — [[boolean]] *(optional)*: If chunks covered by fog-of-war are skipped. Defaults to `false`.
- **`by_player`** — [[PlayerIdentification]] *(optional)*: The player to use if any.
- **`super_forced`** — [[boolean]] *(optional)*: If the cancel deconstruction is super-forced. Defaults to `false`.

### clear_deconstruction_item
Clears all settings/filters on this deconstruction item resetting it to default values.
*Only available on:* `DeconstructionItem`

### clear_upgrade_item
Clears all settings/filters on this upgrade item resetting it to default values.
*Only available on:* `UpgradeItem`

### get_mapper
Gets the filter at the given index for this upgrade item. Note that sources (`"from"` type) that are undefined will read as `{type = "item"}`, while destinations (`"to"` type) that are undefined will read as `nil`.

In contrast to [[LuaItemCommon#set_mapper|LuaItemCommon::set_mapper]], indices past the upgrade item's current size are considered to be out of bounds.
*Only available on:* `UpgradeItem`

**Parameters:**
- **`index`** — [[uint32]]: The index of the mapper to read.
- **`type`** — `"from"` | `"to"`

**Returns:**
- [[UpgradeMapperSource]] | [[UpgradeMapperDestination]] *(optional)*

### set_mapper
Sets the module filter at the given index for this upgrade item.

In contrast to [[LuaItemCommon#get_mapper|LuaItemCommon::get_mapper]], indices past the upgrade item's current size are valid and expand the list of mappings accordingly, if within reasonable bounds.
*Only available on:* `UpgradeItem`

**Parameters:**
- **`index`** — [[uint32]]: The index of the mapper to set.
- **`type`** — `"from"` | `"to"`
- **`mapper`** — [[UpgradeMapperSource]] | [[UpgradeMapperDestination]] | [[nil]]: The mapper to set. Set `nil` to clear the mapper.
