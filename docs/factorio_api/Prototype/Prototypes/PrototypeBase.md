---
title: PrototypeBase
tags: [factorio-api, prototype]
---
# PrototypeBase

> **Abstract**

The abstract base for prototypes. PrototypeBase defines the common features of prototypes, such as localization and order.

## Properties

### type
- **Type:** [[string (type)]]
Specifies the kind of prototype this is.

For a list of all possible types, see the [[Prototypes|prototype overview]].

### name
- **Type:** [[string (type)]]
Unique textual identification of the prototype. May only contain alphanumeric characters, dashes and underscores. May not exceed a length of 200 characters.

For a list of all names used in vanilla, see [data.raw](https://wiki.factorio.com/Data.raw).

### order
- **Type:** [[Order]]
- **Optional**
- **Default:** `""`
Used to order prototypes in inventory, recipes and GUIs. May not exceed a length of 200 characters.

### localised_name
- **Type:** [[LocalisedString (type)]]
- **Optional**
Overwrites the name set in the [locale file](https://wiki.factorio.com/Tutorial:Localisation). Can be used to easily set a procedurally-generated name because the LocalisedString format allows to insert parameters into the name directly from the Lua script.

### localised_description
- **Type:** [[LocalisedString (type)]]
- **Optional**
Overwrites the description set in the [locale file](https://wiki.factorio.com/Tutorial:Localisation). The description is usually shown in the tooltip of the prototype.

### factoriopedia_description
- **Type:** [[LocalisedString (type)]]
- **Optional**
Provides additional description used in factoriopedia.

### subgroup
- **Type:** [[ItemSubGroupID]]
- **Optional**
The name of an [[ItemSubGroup]].

### hidden
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### hidden_in_factoriopedia
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** Value of `hidden`

### parameter
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether the prototype is a special type which can be used to parametrize blueprints and doesn't have other function.

### factoriopedia_simulation
- **Type:** [[SimulationDefinition (type)]]
- **Optional**
The simulation shown when looking at this prototype in the Factoriopedia GUI.
