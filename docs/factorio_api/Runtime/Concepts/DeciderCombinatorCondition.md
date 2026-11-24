---
title: DeciderCombinatorCondition
tags: [factorio-api, runtime, concept]
---
# DeciderCombinatorCondition

## Fields

### first_signal
- **Type:** [[SignalID]]
- **Optional**
Defaults to blank

### first_signal_networks
- **Type:** [[CircuitNetworkSelection]]
- **Optional**
Which circuit networks (red/green) to read `first_signal` from. Defaults to both.

### second_signal
- **Type:** [[SignalID]]
- **Optional**
What to compare `first_signal` to. If not specified, `first_signal` will be compared to `constant`.

### second_signal_networks
- **Type:** [[CircuitNetworkSelection]]
- **Optional**
Which circuit networks (red/green) to read `second_signal` from. Defaults to both.

### constant
- **Type:** [[int32]]
- **Optional**
Constant to compare `first_signal` to. Has no effect when `second_signal` is set. When neither `second_signal` nor `constant` are specified, the effect is as though `constant` were specified with the value `0`.

### comparator
- **Type:** [[ComparatorString]]
- **Optional**
Specifies how the inputs should be compared. If not specified, defaults to `"<"`.

### compare_type
- **Type:** `"and"` | `"or"`
- **Optional**
Tells how this condition is compared with the preceding conditions in the corresponding `conditions` array. Defaults to `"or"`.
