---
title: LuaTechnology
tags: [factorio-api, runtime, class]
---
# LuaTechnology

One research item.

## Attributes

### force
- **Type:** [[LuaForce]]
The force this technology belongs to.

### name
- **Type:** [[string]]
Name of this technology.

### localised_name
- **Type:** [[LocalisedString]]
Localised name of this technology.

### localised_description
- **Type:** [[LocalisedString]]

### prototype
- **Type:** [[LuaTechnologyPrototype]]
The prototype of this technology.

### enabled
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Can this technology be researched?

### visible_when_disabled
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this technology will be visible in the research GUI even though it is disabled.

### upgrade
- **Type:** [[boolean]]
Is this an upgrade-type research?

### researched
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Has this technology been researched? Switching from `false` to `true` will trigger the technology advancement perks; switching from `true` to `false` will reverse them.

### prerequisites
- **Type:** dictionary<[[string]] → [[LuaTechnology]]>
Prerequisites of this technology. The result maps technology name to the [[LuaTechnology]] object.

### successors
- **Type:** dictionary<[[string]] → [[LuaTechnology]]>
Successors of this technology, i.e. technologies which have this technology as a prerequisite.

### research_unit_ingredients
- **Type:** array<[[ResearchIngredient]]>
The types of ingredients that labs will require to research this technology.

### research_unit_count
- **Type:** [[uint32]]
The number of research units required for this technology.

This is multiplied by the current research cost multiplier, unless [[LuaTechnologyPrototype#ignore_tech_cost_multiplier|LuaTechnologyPrototype::ignore_tech_cost_multiplier]] is `true`.

### research_unit_energy
- **Type:** [[double]]
Amount of energy required to finish a unit of research.

### order
- **Type:** [[string]]
The string used to alphabetically sort these prototypes. It is a simple string that has no additional semantic meaning.

### level
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The current level of this technology. For level-based technology writing to this is the same as researching the technology to the previous level. Writing the level will set [[LuaTechnology#enabled|LuaTechnology::enabled]] to `true`.

### research_unit_count_formula
- **Type:** [[MathExpression]]
- **Optional**
The count formula, if this research has any. See [[TechnologyUnit#count_formula|TechnologyUnit::count_formula]] for details.

### saved_progress
- **Type:** [[double]]
- **Writable:** [[double]]
Saved technology progress fraction as a value in range `[0, 1)`. 0 means there is no saved progress.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### reload
Reload this technology from its prototype.

### research_recursive
Research this technology and all of its prerequisites recursively.
