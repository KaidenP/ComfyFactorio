---
title: LuaPrototypeBase
tags: [factorio-api, runtime, class]
---
# LuaPrototypeBase

> **Abstract class** — not directly instantiable.

Base for all prototype classes.

## Attributes

### type
- **Type:** [[string]]
Type of this prototype.

### name
- **Type:** [[string]]
Name of this prototype.

### order
- **Type:** [[string]]
The string used to alphabetically sort these prototypes. It is a simple string that has no additional semantic meaning.

### localised_name
- **Type:** [[LocalisedString]]

### localised_description
- **Type:** [[LocalisedString]]

### factoriopedia_description
- **Type:** [[LocalisedString]]
Provides additional description used in factoriopedia.

### group
- **Type:** [[LuaItemGroup]]
Group of this prototype.

### subgroup
- **Type:** [[LuaItemSubGroup]]
Subgroup of this prototype.

### hidden
- **Type:** [[boolean]]

### hidden_in_factoriopedia
- **Type:** [[boolean]]

### parameter
- **Type:** [[boolean]]

### custom_tooltip_fields
- **Type:** array<[[CustomTooltipField]]>
- **Optional**
Extra description items in the tooltip and Factoriopedia.
