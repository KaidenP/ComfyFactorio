---
title: TrainStopBlueprintControlBehavior
tags: [factorio-api, runtime, concept]
---
# TrainStopBlueprintControlBehavior

## Fields

### input_networks
- **Type:** [[CircuitNetworkSelection]]
- **Optional**

### output_networks
- **Type:** [[CircuitNetworkSelection]]
- **Optional**

### send_to_train
- **Type:** [[boolean]]
- **Optional**
Defaults to `true`.

### read_from_train
- **Type:** [[boolean]]
- **Optional**
Defaults to `false`.

### read_stopped_train
- **Type:** [[boolean]]
- **Optional**
Defaults to `false`.

### train_stopped_signal
- **Type:** [[SignalID]]

### set_trains_limit
- **Type:** [[boolean]]
- **Optional**
Defaults to `false`.

### trains_limit_signal
- **Type:** [[SignalID]]
- **Optional**

### read_trains_count
- **Type:** [[boolean]]
- **Optional**
Defaults to `false`.

### trains_count_signal
- **Type:** [[SignalID]]
- **Optional**

### set_priority
- **Type:** [[boolean]]
- **Optional**
Defaults to `false`.

### priority_signal
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
