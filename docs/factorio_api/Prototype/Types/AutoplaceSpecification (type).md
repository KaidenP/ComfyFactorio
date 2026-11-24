---
title: AutoplaceSpecification
tags: [factorio-api, prototype, type]
---
# AutoplaceSpecification

*Note: `AutoplaceSpecification (type)`.*

Autoplace specification is used to determine which entities are placed when generating map. Currently it is used for enemy bases, tiles, resources and other entities (trees, fishes, etc.).

Autoplace specification describe conditions for placing tiles, entities, and decoratives during surface generation. Autoplace specification defines probability of placement on any given tile and richness, which has different meaning depending on the thing being placed.

## Properties

### control
- **Type:** [[AutoplaceControlID]]
- **Optional**
Name of the [[AutoplaceControl (prototype)|AutoplaceControl]] (row in the map generator GUI) that applies to this entity.

### default_enabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Indicates whether the thing should be placed even if [[MapGenSettings]] do not provide frequency/size/richness for it. (either for the specific prototype or for the control named by AutoplaceSpecification.control).

If true, normal frequency/size/richness (`value=1`) are used in that case. Otherwise it is treated as if 'none' were selected.

### force
- **Type:** `"enemy"` | `"player"` | `"neutral"` | [[string (type)]]
- **Optional**
- **Default:** `"neutral"`
Force of the placed entity. Can be a custom force name. Only relevant for [[EntityWithOwnerPrototype]].

### order
- **Type:** [[Order]]
- **Optional**
- **Default:** `""`
Order for placing the entity (has no effect when placing tiles). Entities whose order compares less are placed earlier (this influences placing multiple entities which collide with itself), from entities with equal order string only one with the highest probability is placed.

### placement_density
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`
For entities and decoratives, how many times to attempt to place on each tile. Probability and collisions are taken into account each attempt.

### tile_restriction
- **Type:** array<[[TileIDRestriction]]>
- **Optional**
Restricts tiles or tile transitions the entity can appear on.

### probability_expression
- **Type:** [[NoiseExpression]]
Provides a noise expression that will be evaluated at every point on the map to determine probability.

### richness_expression
- **Type:** [[NoiseExpression]]
- **Optional**
If specified, provides a noise expression that will be evaluated to determine richness. Otherwise, `probability_expression` will be used instead.

### local_expressions
- **Type:** dictionary<[[string (type)]] → [[NoiseExpression]]>
- **Optional**
A map of expression name to expression. Used by `probability_expression` and `richness_expression`.

Local expressions are meant to store data locally similar to local variables in Lua. Their purpose is to hold noise expressions used multiple times in the named noise expression, or just to tell the reader that the local expression has a specific purpose. Local expressions can access other local definitions and also function parameters, but recursive definitions aren't supported.

### local_functions
- **Type:** dictionary<[[string (type)]] → [[NoiseFunction]]>
- **Optional**
A map of function name to function. Used by `probability_expression` and `richness_expression`.

Local functions serve the same purpose as local expressions - they aren't visible outside of the specific prototype and they have access to other local definitions.
