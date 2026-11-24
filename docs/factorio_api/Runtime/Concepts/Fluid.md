---
title: Fluid
tags: [factorio-api, runtime, concept]
---
# Fluid

## Fields

### name
- **Type:** [[string]]
Fluid prototype name of the fluid.

### amount
- **Type:** [[double]]
Amount of the fluid.

### temperature
- **Type:** [[float]]
- **Optional**
The temperature. When reading this field will always be present. It is not necessary to specify it when writing, however. When not specified, the fluid will be set to the fluid's default temperature as specified in the fluid's prototype.
