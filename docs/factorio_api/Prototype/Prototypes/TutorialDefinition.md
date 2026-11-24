---
title: TutorialDefinition
tags: [factorio-api, prototype]
---
# TutorialDefinition

> **Parent:** [[PrototypeBase]] · **Type name:** `tutorial`

The definition of the tutorial to be used in the tips and tricks, see [[TipsAndTricksItem]]. The actual tutorial scripting code is defined in the tutorial scenario. The scenario must be placed in the `tutorials` folder in the mod.

## Properties

### scenario
- **Type:** [[string (type)]]
Name of the folder for this tutorial scenario in the [[mod-structure|tutorials folder]].

### order
- **Type:** [[Order]]
- **Optional**
- **Default:** Value of `name`
- **Overrides parent**
Used to order prototypes in inventory, recipes and GUIs. May not exceed a length of 200 characters.
