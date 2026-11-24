---
title: InventoryWithCustomStackSizeSpecification
tags: [factorio-api, prototype, type]
---
# InventoryWithCustomStackSizeSpecification

*Note: `InventoryWithCustomStackSizeSpecification (type)`.*

## Properties

### stack_size_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
Must be >= 0.

### stack_size_min
- **Type:** [[ItemCountType (type)]]
- **Optional**
- **Default:** `1`
Must be >= 1.

### stack_size_max
- **Type:** [[ItemCountType (type)]]
- **Optional**
- **Default:** `1000000000`
Must be >= stack_size_min and <= 1000000000.

### stack_size_override
- **Type:** dictionary<[[ItemID (type)]] → [[ItemCountType (type)]]>
- **Optional**
Each record value must be >= 1. For non-stackable items this value will be ignored.

### with_bar
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
