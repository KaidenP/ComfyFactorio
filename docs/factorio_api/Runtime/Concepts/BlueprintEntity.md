---
title: BlueprintEntity
tags: [factorio-api, runtime, concept]
---
# BlueprintEntity

The representation of an entity inside of a blueprint.

## Fields

### entity_number
- **Type:** [[uint32]]
The entity's unique identifier in the blueprint.

### name
- **Type:** [[string]]
The prototype name of the entity.

### position
- **Type:** [[MapPosition]]
The position of the entity.

### direction
- **Type:** [[defines.direction]]
- **Optional**
The direction the entity is facing. Only present for entities that can face in different directions and when the entity is not facing north.

### mirror
- **Type:** [[boolean]]
- **Optional**
Whether this entity is mirrored.

### quality
- **Type:** [[string]]
- **Optional**
The prototype name of the entity's quality.

### items
- **Type:** array<[[BlueprintInsertPlan]]>
- **Optional**
The items that the entity will request when revived, if any.

### tags
- **Type:** [[Tags]]
- **Optional**
The entity tags of the entity, if there are any.

### wires
- **Type:** array<[[BlueprintWire]]>
- **Optional**
Wires connected to this entity in the blueprint.

### burner_fuel_inventory
- **Type:** [[BlueprintInventoryWithFilters]]
- **Optional**
Used by entities with a burner energy source.
