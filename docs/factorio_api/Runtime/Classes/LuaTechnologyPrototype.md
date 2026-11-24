---
title: LuaTechnologyPrototype
tags: [factorio-api, runtime, class]
---
# LuaTechnologyPrototype

> **Extends:** [[LuaPrototypeBase]]

A Technology prototype.

## Attributes

### enabled
- **Type:** [[boolean]]
If this technology prototype is enabled by default (enabled at the beginning of a game).

### essential
- **Type:** [[boolean]]
If this technology prototype is essential, meaning it is shown in the condensed technology graph.

### visible_when_disabled
- **Type:** [[boolean]]
If this technology will be visible in the research GUI even though it is disabled.

### ignore_tech_cost_multiplier
- **Type:** [[boolean]]
If this technology ignores the technology cost multiplier setting.

[[LuaTechnologyPrototype#research_unit_count|LuaTechnologyPrototype::research_unit_count]] will already take this setting into account.

### upgrade
- **Type:** [[boolean]]
If the is technology prototype is an upgrade to some other technology.

### prerequisites
- **Type:** dictionary<[[string]] → [[LuaTechnologyPrototype]]>
Prerequisites of this technology. The result maps technology name to the [[LuaTechnologyPrototype]] object.

### successors
- **Type:** dictionary<[[string]] → [[LuaTechnologyPrototype]]>
Successors of this technology, i.e. technologies which have this technology as a prerequisite.

### research_unit_ingredients
- **Type:** array<[[ResearchIngredient]]>
The types of ingredients that labs will require to research this technology.

### effects
- **Type:** array<[[TechnologyModifier]]>
Effects applied when this technology is researched.

### research_unit_count
- **Type:** [[uint32]]
The number of research units required for this technology.

This is multiplied by the current research cost multiplier, unless [[LuaTechnologyPrototype#ignore_tech_cost_multiplier|LuaTechnologyPrototype::ignore_tech_cost_multiplier]] is `true`.

### research_unit_energy
- **Type:** [[double]]
Amount of energy required to finish a unit of research.

### level
- **Type:** [[uint32]]
The level of this research.

### max_level
- **Type:** [[uint32]]
The max level of this research.

### research_unit_count_formula
- **Type:** [[MathExpression]]
- **Optional**
The count formula, if this research has any. See [[TechnologyUnit#count_formula|TechnologyUnit::count_formula]] for details.

### research_trigger
- **Type:** [[ResearchTrigger]]
- **Optional**
The trigger that will research this technology if any.

### allows_productivity
- **Type:** [[boolean]]

### factoriopedia_alternative
- **Type:** [[LuaTechnologyPrototype]]
- **Optional**
An alternative prototype that will be used to display info about this prototype in Factoriopedia.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
