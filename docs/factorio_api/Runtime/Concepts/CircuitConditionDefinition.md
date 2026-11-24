---
title: CircuitConditionDefinition
tags: [factorio-api, runtime, concept]
---
# CircuitConditionDefinition

## Fields

### comparator
- **Type:** [[ComparatorString]]
- **Optional**
Specifies how the inputs should be compared. If not specified, defaults to `"<"`.

### first_signal
- **Type:** [[SignalID]]
- **Optional**
Defaults to blank.

### second_signal
- **Type:** [[SignalID]]
- **Optional**
What to compare `first_signal` to. If not specified, `first_signal` will be compared to `constant`.

### constant
- **Type:** [[int32]]
- **Optional**
Constant to compare `first_signal` to. Has no effect when `second_signal` is set. When neither `second_signal` nor `constant` are specified, the effect is as though `constant` were specified with the value `0`.

### fulfilled
- **Type:** [[boolean]]
- **Optional**
Whether the condition is currently fulfilled.
