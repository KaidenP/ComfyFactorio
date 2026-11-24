---
title: LuaPrototypes
tags: [factorio-api, runtime, class]
---
# LuaPrototypes

Provides read-only access to prototypes. It is accessible through the global object named `prototypes`.

## Attributes

### font
- **Type:** LuaCustomTable<[[string]] → [[LuaFontPrototype]]>
A dictionary containing every LuaFontPrototype indexed by `name`.

### map_gen_preset
- **Type:** LuaCustomTable<[[string]] → [[MapGenPreset]]>
A dictionary containing every MapGenPreset indexed by `name`.

A MapGenPreset is an exact copy of the prototype table provided from the data stage.

### style
- **Type:** LuaCustomTable<[[string]] → [[string]]>
A map of styles that [[LuaGuiElement]] can use.

Maps from the style's name to its type, as seen on [[StyleSpecification]].

### utility_constants
- **Type:** [[UtilityConstants]]
All game-defined utility constants. Note that his is implemented as a [[LuaCustomTable]].

### entity
- **Type:** LuaCustomTable<[[string]] → [[LuaEntityPrototype]]>
A dictionary containing every LuaEntityPrototype indexed by `name`.

### item
- **Type:** LuaCustomTable<[[string]] → [[LuaItemPrototype]]>
A dictionary containing every LuaItemPrototype indexed by `name`.

### fluid
- **Type:** LuaCustomTable<[[string]] → [[LuaFluidPrototype]]>
A dictionary containing every LuaFluidPrototype indexed by `name`.

### tile
- **Type:** LuaCustomTable<[[string]] → [[LuaTilePrototype]]>
A dictionary containing every LuaTilePrototype indexed by `name`.

### equipment
- **Type:** LuaCustomTable<[[string]] → [[LuaEquipmentPrototype]]>
A dictionary containing every LuaEquipmentPrototype indexed by `name`.

### damage
- **Type:** LuaCustomTable<[[string]] → [[LuaDamagePrototype]]>
A dictionary containing every LuaDamagePrototype indexed by `name`.

### virtual_signal
- **Type:** LuaCustomTable<[[string]] → [[LuaVirtualSignalPrototype]]>
A dictionary containing every LuaVirtualSignalPrototype indexed by `name`.

### equipment_grid
- **Type:** LuaCustomTable<[[string]] → [[LuaEquipmentGridPrototype]]>
A dictionary containing every LuaEquipmentGridPrototype indexed by `name`.

### recipe
- **Type:** LuaCustomTable<[[string]] → [[LuaRecipePrototype]]>
A dictionary containing every LuaRecipePrototype indexed by `name`.

### technology
- **Type:** LuaCustomTable<[[string]] → [[LuaTechnologyPrototype]]>
A dictionary containing every [[LuaTechnologyPrototype]] indexed by `name`.

### decorative
- **Type:** LuaCustomTable<[[string]] → [[LuaDecorativePrototype]]>
A dictionary containing every LuaDecorativePrototype indexed by `name`.

### particle
- **Type:** LuaCustomTable<[[string]] → [[LuaParticlePrototype]]>
A dictionary containing every LuaParticlePrototype indexed by `name`.

### autoplace_control
- **Type:** LuaCustomTable<[[string]] → [[LuaAutoplaceControlPrototype]]>
A dictionary containing every LuaAutoplaceControlPrototype indexed by `name`.

### mod_setting
- **Type:** LuaCustomTable<[[string]] → [[LuaModSettingPrototype]]>
A dictionary containing every LuaModSettingPrototype indexed by `name`.

### custom_input
- **Type:** LuaCustomTable<[[string]] → [[LuaCustomInputPrototype]]>
A dictionary containing every LuaCustomInputPrototype indexed by `name`.

### ammo_category
- **Type:** LuaCustomTable<[[string]] → [[LuaAmmoCategoryPrototype]]>
A dictionary containing every LuaAmmoCategoryPrototype indexed by `name`.

### named_noise_expression
- **Type:** LuaCustomTable<[[string]] → [[LuaNamedNoiseExpression]]>
A dictionary containing every LuaNamedNoiseExpression indexed by `name`.

### named_noise_function
- **Type:** LuaCustomTable<[[string]] → [[LuaNamedNoiseFunction]]>
A dictionary containing every LuaNamedNoiseFunction indexed by `name`.

### item_subgroup
- **Type:** LuaCustomTable<[[string]] → [[LuaItemSubGroup]]>
A dictionary containing every ItemSubgroup indexed by `name`.

### item_group
- **Type:** LuaCustomTable<[[string]] → [[LuaItemGroup]]>
A dictionary containing every ItemGroup indexed by `name`.

### fuel_category
- **Type:** LuaCustomTable<[[string]] → [[LuaFuelCategoryPrototype]]>
A dictionary containing every LuaFuelCategoryPrototype indexed by `name`.

### resource_category
- **Type:** LuaCustomTable<[[string]] → [[LuaResourceCategoryPrototype]]>
A dictionary containing every LuaResourceCategoryPrototype indexed by `name`.

### achievement
- **Type:** LuaCustomTable<[[string]] → [[LuaAchievementPrototype]]>
A dictionary containing every LuaAchievementPrototype indexed by `name`.

### module_category
- **Type:** LuaCustomTable<[[string]] → [[LuaModuleCategoryPrototype]]>
A dictionary containing every LuaModuleCategoryPrototype indexed by `name`.

### equipment_category
- **Type:** LuaCustomTable<[[string]] → [[LuaEquipmentCategoryPrototype]]>
A dictionary containing every LuaEquipmentCategoryPrototype indexed by `name`.

### trivial_smoke
- **Type:** LuaCustomTable<[[string]] → [[LuaTrivialSmokePrototype]]>
A dictionary containing every LuaTrivialSmokePrototype indexed by `name`.

### shortcut
- **Type:** LuaCustomTable<[[string]] → [[LuaShortcutPrototype]]>
A dictionary containing every LuaShortcutPrototype indexed by `name`.

### recipe_category
- **Type:** LuaCustomTable<[[string]] → [[LuaRecipeCategoryPrototype]]>
A dictionary containing every LuaRecipeCategoryPrototype indexed by `name`.

### quality
- **Type:** LuaCustomTable<[[string]] → [[LuaQualityPrototype]]>

### surface_property
- **Type:** LuaCustomTable<[[string]] → [[LuaSurfacePropertyPrototype]]>

### space_location
- **Type:** LuaCustomTable<[[string]] → [[LuaSpaceLocationPrototype]]>

### space_connection
- **Type:** LuaCustomTable<[[string]] → [[LuaSpaceConnectionPrototype]]>

### custom_event
- **Type:** LuaCustomTable<[[string]] → [[LuaCustomEventPrototype]]>
A dictionary containing every defined custom event, indexed by `name`.

### active_trigger
- **Type:** LuaCustomTable<[[string]] → [[LuaActiveTriggerPrototype]]>
A dictionary containing every LuaActiveTriggerPrototype indexed by `name`.

### asteroid_chunk
- **Type:** LuaCustomTable<[[string]] → [[LuaAsteroidChunkPrototype]]>
A dictionary containing every LuaAsteroidChunkPrototype indexed by `name`.

### collision_layer
- **Type:** LuaCustomTable<[[string]] → [[LuaCollisionLayerPrototype]]>
A dictionary containing every LuaCollisionLayerPrototype indexed by `name`.

### airborne_pollutant
- **Type:** LuaCustomTable<[[string]] → [[LuaAirbornePollutantPrototype]]>
A dictionary containing every LuaAirbornePollutantPrototype indexed by `name`.

### burner_usage
- **Type:** LuaCustomTable<[[string]] → [[LuaBurnerUsagePrototype]]>
A dictionary containing every LuaBurnerUsagePrototype indexed by `name`.

### mod_data
- **Type:** LuaCustomTable<[[string]] → [[LuaModData]]>
A dictionary containing every LuaModData indexed by `name`.

### surface
- **Type:** LuaCustomTable<[[string]] → [[LuaSurfacePrototype]]>
A dictionary containing every LuaSurfacePrototype indexed by `name`.

### procession
- **Type:** LuaCustomTable<[[string]] → [[LuaProcessionPrototype]]>
A dictionary containing every LuaProcessionPrototype indexed by `name`.

### procession_layer_inheritance_group
- **Type:** LuaCustomTable<[[string]] → [[LuaProcessionLayerInheritanceGroupPrototype]]>
A dictionary containing every LuaProcessionLayerInheritanceGroupPrototype indexed by `name`.

### max_force_distraction_distance
- **Type:** [[double]]

### max_force_distraction_chunk_distance
- **Type:** [[uint32]]

### max_electric_pole_supply_area_distance
- **Type:** [[float]]

### max_electric_pole_connection_distance
- **Type:** [[double]]

### max_beacon_supply_area_distance
- **Type:** [[uint32]]

### max_gate_activation_distance
- **Type:** [[double]]

### max_inserter_reach_distance
- **Type:** [[double]]

### max_pipe_to_ground_distance
- **Type:** [[uint8]]

### max_underground_belt_distance
- **Type:** [[uint8]]

### max_logistics_connection_distance
- **Type:** [[float]]

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### get_entity_filtered
Returns a dictionary of all LuaEntityPrototypes that fit the given filters. The prototypes are indexed by `name`.

**Parameters:**
- **`filters`** — array<[[EntityPrototypeFilter]]>

**Returns:**
- LuaCustomTable<[[string]] → [[LuaEntityPrototype]]>

**Examples:**

```
-- Get every entity prototype that can craft recipes involving fluids in the way some assembling machines can
local prototypes = prototypes.get_entity_filtered{{filter="crafting-category", crafting_category="crafting-with-fluid"}}
```

### get_item_filtered
Returns a dictionary of all LuaItemPrototypes that fit the given filters. The prototypes are indexed by `name`.

**Parameters:**
- **`filters`** — array<[[ItemPrototypeFilter]]>

**Returns:**
- LuaCustomTable<[[string]] → [[LuaItemPrototype]]>

**Examples:**

```
-- Get every item prototype that has a fuel top speed multiplier larger than 1.
local prototypes = prototypes.get_item_filtered{{filter = "fuel-top-speed-multiplier", comparison = ">", value = 1}}
```

### get_equipment_filtered
Returns a dictionary of all LuaEquipmentPrototypes that fit the given filters. The prototypes are indexed by `name`.

**Parameters:**
- **`filters`** — array<[[EquipmentPrototypeFilter]]>

**Returns:**
- LuaCustomTable<[[string]] → [[LuaEquipmentPrototype]]>

**Examples:**

```
-- Get every equipment prototype that functions as a battery.
local prototypes = prototypes.get_equipment_filtered{{filter="type", type="battery-equipment"}}
```

### get_mod_setting_filtered
Returns a dictionary of all LuaModSettingPrototypes that fit the given filters. The prototypes are indexed by `name`.

**Parameters:**
- **`filters`** — array<[[ModSettingPrototypeFilter]]>

**Returns:**
- LuaCustomTable<[[string]] → [[LuaModSettingPrototype]]>

**Examples:**

```
-- Get every mod setting prototype that belongs to the specified mod.
local prototypes = prototypes.get_mod_setting_filtered{{filter="mod", mod="space-exploration"}}
```

### get_achievement_filtered
Returns a dictionary of all LuaAchievementPrototypes that fit the given filters. The prototypes are indexed by `name`.

**Parameters:**
- **`filters`** — array<[[AchievementPrototypeFilter]]>

**Returns:**
- LuaCustomTable<[[string]] → [[LuaAchievementPrototype]]>

**Examples:**

```
-- Get every achievement prototype that is not allowed to be completed on the peaceful difficulty setting.
local prototypes = prototypes.get_achievement_filtered{{filter="allowed-without-fight", invert=true}}
```

### get_tile_filtered
Returns a dictionary of all LuaTilePrototypes that fit the given filters. The prototypes are indexed by `name`.

**Parameters:**
- **`filters`** — array<[[TilePrototypeFilter]]>

**Returns:**
- LuaCustomTable<[[string]] → [[LuaTilePrototype]]>

**Examples:**

```
-- Get every tile prototype that improves a player's walking speed by at least 50%.
local prototypes = prototypes.get_tile_filtered{{filter="walking-speed-modifier", comparison="≥", value=1.5}}
```

### get_decorative_filtered
Returns a dictionary of all LuaDecorativePrototypes that fit the given filters. The prototypes are indexed by `name`.

**Parameters:**
- **`filters`** — array<[[DecorativePrototypeFilter]]>

**Returns:**
- LuaCustomTable<[[string]] → [[LuaDecorativePrototype]]>

**Examples:**

```
-- Get every decorative prototype that is auto-placed.
local prototypes = prototypes.get_decorative_filtered{{filter="autoplace"}}
```

### get_fluid_filtered
Returns a dictionary of all LuaFluidPrototypes that fit the given filters. The prototypes are indexed by `name`.

**Parameters:**
- **`filters`** — array<[[FluidPrototypeFilter]]>

**Returns:**
- LuaCustomTable<[[string]] → [[LuaFluidPrototype]]>

**Examples:**

```
-- Get every fluid prototype that has a heat capacity of exactly `100`.
local prototypes = prototypes.get_fluid_filtered{{filter="heat-capacity", comparison="=", value=100}}
```

### get_recipe_filtered
Returns a dictionary of all LuaRecipePrototypes that fit the given filters. The prototypes are indexed by `name`.

**Parameters:**
- **`filters`** — array<[[RecipePrototypeFilter]]>

**Returns:**
- LuaCustomTable<[[string]] → [[LuaRecipePrototype]]>

**Examples:**

```
-- Get every recipe prototype that takes less than half a second to craft (at crafting speed `1`).
local prototypes = prototypes.get_recipe_filtered{{filter="energy", comparison="<", value=0.5}}
```

### get_technology_filtered
Returns a dictionary of all LuaTechnologyPrototypes that fit the given filters. The prototypes are indexed by `name`.

**Parameters:**
- **`filters`** — array<[[TechnologyPrototypeFilter]]>

**Returns:**
- LuaCustomTable<[[string]] → [[LuaTechnologyPrototype]]>

**Examples:**

```
-- Get every technology prototype that can be researched at the start of the game.
local prototypes = prototypes.get_technology_filtered{{filter="has-prerequisites", invert=true}}
```

### get_history
Gets the prototype history for the given type and name.

**Parameters:**
- **`type`** — [[string]]
- **`name`** — [[string]]

**Returns:**
- [[PrototypeHistory]]
