---
title: ItemIDAndQualityIDPair
tags: [factorio-api, runtime, concept]
---
# ItemIDAndQualityIDPair

An item prototype with optional quality specification.

## Fields

### name
- **Type:** [[ItemID]]
Item prototype. Returns `LuaItemPrototype` when read.

### quality
- **Type:** [[QualityID]]
- **Optional**
Quality prototype. Normal quality will be used if not specified. Returns `LuaQualityPrototype` when read.
