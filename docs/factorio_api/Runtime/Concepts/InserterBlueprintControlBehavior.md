---
title: InserterBlueprintControlBehavior
tags: [factorio-api, runtime, concept]
---
# InserterBlueprintControlBehavior

## Fields

### input_networks
- **Type:** [[CircuitNetworkSelection]]
- **Optional**

### output_networks
- **Type:** [[CircuitNetworkSelection]]
- **Optional**

### circuit_set_filters
- **Type:** [[boolean]]
- **Optional**
Defaults to `false`.

### circuit_read_hand_contents
- **Type:** [[boolean]]
- **Optional**
Defaults to `false`.

### circuit_hand_read_mode
- **Type:** [[defines.control_behavior#hand_read_mode]]
- **Optional**
Defaults to `pulse`.

### circuit_set_stack_size
- **Type:** [[boolean]]
- **Optional**
Defaults to `false`. Whether the inserter hand size is controlled by the circuit network.

### stack_control_input_signal
- **Type:** [[SignalID]]
- **Optional**

### circuit_enabled
- **Type:** [[boolean]]
- **Optional**
Defaults to `false`.

### circuit_condition
- **Type:** [[CircuitCondition]]
- **Optional**

### connect_to_logistic_network
- **Type:** [[boolean]]
- **Optional**
Defaults to `false`.

### logistic_condition
- **Type:** [[CircuitCondition]]
- **Optional**
