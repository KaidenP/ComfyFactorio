---
title: MineableProperties
tags: [factorio-api, runtime, concept]
---
# MineableProperties

## Fields

### minable
- **Type:** [[boolean]]
Is this entity mineable at all?

### mining_time
- **Type:** [[double]]
Energy required to mine an entity.

### transfer_entity_health_to_products
- **Type:** [[boolean]]

### mining_particle
- **Type:** [[string]]
- **Optional**
Prototype name of the particle produced when mining this entity. Will only be present if this entity produces any particle during mining.

### products
- **Type:** array<[[Product]]>
- **Optional**
Products obtained by mining this entity.

### fluid_amount
- **Type:** [[double]]
- **Optional**
The required fluid amount if any.

### required_fluid
- **Type:** [[string]]
- **Optional**
The prototype name of the required fluid if any.

### mining_trigger
- **Type:** array<[[TriggerItem]]>
- **Optional**
The mining trigger if any.
