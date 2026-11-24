---
title: LuaItemPrototype
tags: [factorio-api, runtime, class]
---
# LuaItemPrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of an item. For example, an item prototype can be obtained from [[LuaPrototypes#item|LuaPrototypes::item]] by its name: `prototypes.item["iron-plate"]`.

## Attributes

### place_result
- **Type:** [[LuaEntityPrototype]]
- **Optional**
Prototype of the entity that will be created by placing this item, if any.

### place_as_equipment_result
- **Type:** [[LuaEquipmentPrototype]]
- **Optional**
Prototype of the equipment that will be created by placing this item in an equipment grid, if any.

### place_as_tile_result
- **Type:** [[PlaceAsTileResult]]
- **Optional**
The place-as-tile result if one is defined, if any.

### stackable
- **Type:** [[boolean]]
Is this item allowed to stack at all?

### stack_size
- **Type:** [[uint32]]
Maximum stack size of the item specified by this prototype.

### fuel_categories
- **Type:** array<[[string]]>
- **Optional**
Fuel categories. Only provided when not empty.

### burnt_result
- **Type:** [[LuaItemPrototype]]
- **Optional**
The result of burning this item as fuel, if any.

### fuel_value
- **Type:** [[float]]
Fuel value when burned.

### fuel_acceleration_multiplier
- **Type:** [[double]]
The acceleration multiplier when this item is used as fuel in a vehicle.

### fuel_top_speed_multiplier
- **Type:** [[double]]
The fuel top speed multiplier when this item is used as fuel in a vehicle.

### fuel_emissions_multiplier
- **Type:** [[double]]
The emissions multiplier if this is used as fuel.

### fuel_acceleration_multiplier_quality_bonus
- **Type:** [[double]]
Additional fuel acceleration multiplier per quality level.

### fuel_top_speed_multiplier_quality_bonus
- **Type:** [[double]]
Additional fuel top speed multiplier per quality level.

### flags
- **Type:** [[ItemPrototypeFlags]]
The flags for this item prototype.

### rocket_launch_products
- **Type:** array<[[Product]]>
The results of launching this item in a rocket.

### send_to_orbit_mode
- **Type:** `"not-sendable"` | `"manual"` | `"automated"`
How this item interacts when being sent to orbit.

### can_be_mod_opened
- **Type:** [[boolean]]
If this item can be mod-opened.

### spoil_result
- **Type:** [[LuaItemPrototype]]
- **Optional**
The spoil result of this item, if any

### spoil_quality_min
- **Type:** [[LuaQualityPrototype]]
- **Optional**

### spoil_quality_max
- **Type:** [[LuaQualityPrototype]]
- **Optional**

### spoil_quality_change
- **Type:** [[int8]]

### plant_result
- **Type:** [[LuaEntityPrototype]]
- **Optional**
The result entity when planting this item as a seed.

### spoil_to_trigger_result
- **Type:** [[SpoilToTriggerResult]]
- **Optional**

### destroyed_by_dropping_trigger
- **Type:** array<[[TriggerItem]]>
- **Optional**

### weight
- **Type:** [[Weight]]
Weight of this item. More information on how item weight is determined can be found on its [[item-weight|auxiliary page]].

### ingredient_to_weight_coefficient
- **Type:** [[double]]

### fuel_glow_color
- **Type:** [[Color]]
- **Optional**

### default_import_location
- **Type:** [[LuaSpaceLocationPrototype]]

### factoriopedia_alternative
- **Type:** [[LuaItemPrototype]]
- **Optional**
An alternative prototype that will be used to display info about this prototype in Factoriopedia.

### moved_to_hub_when_building
- **Type:** [[boolean]]

### quality_affects_spoil_ticks
- **Type:** [[boolean]]

### lab_ignores_spoil_percent
- **Type:** [[boolean]]

### science_capacity
- **Type:** [[double]]

### space_platform_request_priority
- **Type:** [[boolean]]

### color_hint
- **Type:** [[ColorHintSpecification]]

### spoil_level
- **Type:** [[uint8]]

### used_by_labs
- **Type:** [[boolean]]
Whether this item is referenced by any [[LabPrototype#inputs|lab input]].

### ammo_category
- **Type:** [[LuaAmmoCategoryPrototype]]
- **Optional**

### magazine_size
- **Type:** [[float]]
- **Optional**
Size of full magazine.

### reload_time
- **Type:** [[float]]
- **Optional**
Amount of extra time (in ticks) it takes to reload the weapon after depleting the magazine.

### shoot_protected
- **Type:** [[boolean]]
- **Optional**

### equipment_grid
- **Type:** [[LuaEquipmentGridPrototype]]
- **Optional**
The prototype of this armor's equipment grid, if any.

### resistances
- **Type:** dictionary<[[string]] → [[Resistance]]>
- **Optional**
Resistances of this armor item, if any, indexed by damage type name.

### collision_box
- **Type:** [[BoundingBox]]
- **Optional**
The collision box used by character entities when wearing this armor.

### drawing_box
- **Type:** [[BoundingBox]]
- **Optional**
The drawing box used by character entities when wearing this armor.

### provides_flight
- **Type:** [[boolean]]
- **Optional**
If this armor provides flight to character entities when worm.

### capsule_action
- **Type:** [[CapsuleAction]]
- **Optional**
The capsule action for this capsule item prototype.

### radius_color
- **Type:** [[Color]]
- **Optional**

### cuts
- **Type:** [[boolean]]
- **Optional**

### attack_parameters
- **Type:** [[AttackParameters]]
- **Optional**
The gun attack parameters.

### item_filters
- **Type:** array<[[LuaItemPrototype]]>
- **Optional**

### item_group_filters
- **Type:** array<[[LuaItemGroup]]>
- **Optional**

### item_subgroup_filters
- **Type:** array<[[LuaItemSubGroup]]>
- **Optional**

### filter_mode
- **Type:** [[PrototypeFilterMode]]
- **Optional**
The filter mode used by this item with inventory.

### localised_filter_message
- **Type:** [[LocalisedString]]
- **Optional**
The localised string used when the player attempts to put items into this item with inventory that aren't allowed.

### quality_affects_inventory_size
- **Type:** [[boolean]]
- **Optional**

### default_label_color
- **Type:** [[Color]]
- **Optional**
The default label color used for this item with label, if any.

### draw_label_for_cursor_render
- **Type:** [[boolean]]
- **Optional**
If true, and this item with label has a label it is drawn in place of the normal number when held in the cursor.

### speed
- **Type:** [[float]]
- **Optional**
The repairing speed if this is a repairing tool.

### module_effects
- **Type:** [[Effect]]
- **Optional**
Effects of this module.

### category
- **Type:** [[string]]
- **Optional**
The name of a [[LuaModuleCategoryPrototype]]. Used when upgrading modules: Ctrl + click modules into an entity and it will replace lower tier modules of the same category with higher tier modules.

### tier
- **Type:** [[uint32]]
- **Optional**
Tier of the module inside its category. Used when upgrading modules: Ctrl + click modules into an entity and it will replace lower tier modules with higher tier modules if they have the same category.

### requires_beacon_alt_mode
- **Type:** [[boolean]]
- **Optional**

### beacon_tint
- **Type:** array<[[Color]]>
- **Optional**

### consumption_quality_multiplier
- **Type:** [[float]]
- **Optional**

### speed_quality_multiplier
- **Type:** [[float]]
- **Optional**

### productivity_quality_multiplier
- **Type:** [[float]]
- **Optional**

### pollution_quality_multiplier
- **Type:** [[float]]
- **Optional**

### quality_quality_multiplier
- **Type:** [[float]]
- **Optional**

### rails
- **Type:** array<[[LuaEntityPrototype]]>
- **Optional**
Prototypes of all rails possible to be used by this rail planner prototype.

### support
- **Type:** [[LuaEntityPrototype]]
- **Optional**
The rail support used by this rail planner.

### manual_length_limit
- **Type:** [[double]]
- **Optional**

### always_include_tiles
- **Type:** [[boolean]]
- **Optional**
If tiles area always included when doing selection with this selection tool prototype.

### skip_fog_of_war
- **Type:** [[boolean]]
- **Optional**
If this selection tool skips things covered by fog of war.

### durability_description_key
- **Type:** [[string]]
- **Optional**
The durability message key used when displaying the durability of this tool.

### factoriopedia_durability_description_key
- **Type:** [[string]]
- **Optional**
The durability message key used when displaying the durability of this tool in Factoriopedia.

### durability_description_value
- **Type:** [[string]]
- **Optional**
The durability message value used when displaying the durability of this tool.

### infinite
- **Type:** [[boolean]]
- **Optional**
If this tool item has infinite durability.

### trigger
- **Type:** [[TriggerItem]]
- **Optional**

### surface
- **Type:** [[LuaSurfacePrototype]]
- **Optional**

### create_electric_network
- **Type:** [[boolean]]
- **Optional**

### tiles
- **Type:** array<[[SpacePlatformTileDefinition]]>
- **Optional**

### initial_items
- **Type:** array<[[ItemProduct]]>
- **Optional**

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### has_flag
Test whether this item prototype has a certain flag set.

**Parameters:**
- **`flag`** — [[ItemPrototypeFlag]]: The flag to test.

**Returns:**
- [[boolean]]

### get_spoil_ticks
The number of ticks before this item spoils, or `0` if it does not spoil.

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[uint32]]

### get_ammo_type
The type of this ammo prototype.
*Only available on:* `AmmoItem`

**Parameters:**
- **`ammo_source_type`** — `"default"` | `"player"` | `"turret"` | `"vehicle"` *(optional)*: Defaults to `"default"`.

**Returns:**
- [[AmmoType]] *(optional)*

### get_inventory_size_bonus
The inventory size bonus for this armor prototype.
*Only available on:* `ArmorPrototype`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[uint32]] *(optional)*

### get_inventory_size
The main inventory size for item-with-inventory-prototype.
*Only available on:* `ItemWithInventoryPrototype`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[uint32]] *(optional)*

### get_module_effects
Effects of this module at the specified quality.
*Only available on:* `ModuleItem`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[Effect]] *(optional)*

### get_selection_border_color
The color used when doing normal selection with this selection tool prototype.
*Only available on:* `SelectionTool`

**Parameters:**
- **`selection_mode`** — [[defines.selection_mode]]

**Returns:**
- [[Color]] *(optional)*

### get_selection_mode_flags
Flags that affect which entities will be selected.
*Only available on:* `SelectionTool`

**Parameters:**
- **`selection_mode`** — [[defines.selection_mode]]

**Returns:**
- [[SelectionModeFlags]] *(optional)*

### get_cursor_box_type
*Only available on:* `SelectionTool`

**Parameters:**
- **`selection_mode`** — [[defines.selection_mode]]

**Returns:**
- [[CursorBoxRenderType]] *(optional)*

### get_draw_selection_counts
Whether the list of how many entities are selected should be shown.
*Only available on:* `SelectionTool`

**Parameters:**
- **`selection_mode`** — [[defines.selection_mode]]

**Returns:**
- [[boolean]] *(optional)*

### get_entity_filter_mode
The entity filter mode used by this selection tool.
*Only available on:* `SelectionTool`

**Parameters:**
- **`selection_mode`** — [[defines.selection_mode]]

**Returns:**
- [[PrototypeFilterMode]] *(optional)*

### get_tile_filter_mode
The tile filter mode used by this selection tool.
*Only available on:* `SelectionTool`

**Parameters:**
- **`selection_mode`** — [[defines.selection_mode]]

**Returns:**
- [[PrototypeFilterMode]] *(optional)*

### get_entity_filters
The entity filters used by this selection tool.
*Only available on:* `SelectionTool`

**Parameters:**
- **`selection_mode`** — [[defines.selection_mode]]

**Returns:**
- array<[[LuaEntityPrototype]]> *(optional)*

### get_entity_type_filters
The entity type filters used by this selection tool indexed by entity type.

The boolean value is meaningless and is used to allow easy lookup if a type exists in the dictionary.
*Only available on:* `SelectionTool`

**Parameters:**
- **`selection_mode`** — [[defines.selection_mode]]

**Returns:**
- dictionary<[[string]] → `true`> *(optional)*

### get_tile_filters
The tile filters used by this selection tool.
*Only available on:* `SelectionTool`

**Parameters:**
- **`selection_mode`** — [[defines.selection_mode]]

**Returns:**
- array<[[LuaTilePrototype]]> *(optional)*

### get_durability
The durability of this tool item prototype.
*Only available on:* `ToolItem`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*
