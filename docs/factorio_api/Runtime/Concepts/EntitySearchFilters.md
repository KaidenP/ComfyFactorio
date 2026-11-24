---
title: EntitySearchFilters
tags: [factorio-api, runtime, concept]
---
# EntitySearchFilters

## Fields

### area
- **Type:** [[BoundingBox]]
- **Optional**

### position
- **Type:** [[MapPosition]]
- **Optional**
Has precedence over area field.

### radius
- **Type:** [[double]]
- **Optional**
If given with position, will return all entities within the radius of the position.

### name
- **Type:** [[EntityID]] | array<[[EntityID]]>
- **Optional**
An empty array means nothing matches the name filter.

### type
- **Type:** [[string]] | array<[[string]]>
- **Optional**
An empty array means nothing matches the type filter.

### ghost_name
- **Type:** [[EntityID]] | array<[[EntityID]]>
- **Optional**
An empty array means nothing matches the ghost_name filter.

### ghost_type
- **Type:** [[string]] | array<[[string]]>
- **Optional**
An empty array means nothing matches the ghost_type filter.

### direction
- **Type:** [[defines.direction]] | array<[[defines.direction]]>
- **Optional**

### collision_mask
- **Type:** [[CollisionLayerID]] | array<[[CollisionLayerID]]> | dictionary<[[CollisionLayerID]] → `true`>
- **Optional**

### force
- **Type:** [[ForceSet]]
- **Optional**

### to_be_deconstructed
- **Type:** [[boolean]]
- **Optional**

### to_be_upgraded
- **Type:** [[boolean]]
- **Optional**

### limit
- **Type:** [[uint32]]
- **Optional**

### is_military_target
- **Type:** [[boolean]]
- **Optional**

### has_item_inside
- **Type:** [[ItemWithQualityID]]
- **Optional**

### quality
- **Type:** [[QualityCondition]]
- **Optional**

### invert
- **Type:** [[boolean]]
- **Optional**
Whether the filters should be inverted.
