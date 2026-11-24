---
title: HeatSetting
tags: [factorio-api, runtime, concept]
---
# HeatSetting

The settings used by a heat-interface type entity.

## Fields

### temperature
- **Type:** [[double]]
- **Optional**
The target temperature. Defaults to the minimum temperature of the heat buffer.

### mode
- **Type:** [[HeatSettingMode]]
- **Optional**
Defaults to `"at-least"`.
