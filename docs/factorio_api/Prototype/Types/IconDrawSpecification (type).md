---
title: IconDrawSpecification
tags: [factorio-api, prototype, type]
---
# IconDrawSpecification

*Note: `IconDrawSpecification (type)`.*

Specification of where and how the alt-mode icons of entities should be drawn.

## Properties

### shift
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0, 0}`

### scale
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`

### scale_for_many
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
Scale of the icon when there are many items.

### render_layer
- **Type:** `"entity-info-icon"` | `"entity-info-icon-above"` | `"air-entity-info-icon"`
- **Optional**
- **Default:** `"entity-info-icon"`
Render layer of the icon.
