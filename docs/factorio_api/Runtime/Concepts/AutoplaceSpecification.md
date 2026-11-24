---
title: AutoplaceSpecification
tags: [factorio-api, runtime, concept]
---
# AutoplaceSpecification

Specifies how probability and richness are calculated when placing something on the map.

## Fields

### placement_density
- **Type:** [[uint32]]

### control
- **Type:** [[string]]
- **Optional**
Control prototype name.

### probability_expression
- **Type:** [[NoiseExpressionSourceString]]

### richness_expression
- **Type:** [[NoiseExpressionSourceString]]
- **Optional**

### order
- **Type:** [[string]]

### default_enabled
- **Type:** [[boolean]]

### tile_restriction
- **Type:** array<[[AutoplaceSpecificationRestriction]]>
- **Optional**

### force
- **Type:** [[string]]
