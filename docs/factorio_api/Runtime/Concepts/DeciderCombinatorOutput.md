---
title: DeciderCombinatorOutput
tags: [factorio-api, runtime, concept]
---
# DeciderCombinatorOutput

## Fields

### signal
- **Type:** [[SignalID]]
Specifies a signal to output.

### copy_count_from_input
- **Type:** [[boolean]]
- **Optional**
Defaults to `true`. When `false`, will output the value from `constant` for the given `output_signal`.

### constant
- **Type:** [[int32]]
- **Optional**
The value to output when not copying input. Defaults to `1`.

### networks
- **Type:** [[CircuitNetworkSelection]]
- **Optional**
Sets which input network to read the value of `signal` from if `copy_count_from_input` is `true`. Defaults to both.
