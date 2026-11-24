---
title: LampBlueprintControlBehavior
tags: [factorio-api, runtime, concept]
---
# LampBlueprintControlBehavior

## Fields

### input_networks
- **Type:** [[CircuitNetworkSelection]]
- **Optional**

### use_colors
- **Type:** [[boolean]]
- **Optional**
Defaults to `false`.

### red_signal
- **Type:** [[SignalID]]
- **Optional**

### green_signal
- **Type:** [[SignalID]]
- **Optional**

### blue_signal
- **Type:** [[SignalID]]
- **Optional**

### rgb_signal
- **Type:** [[SignalID]]
- **Optional**

### color_mode
- **Type:** [[defines.control_behavior#color_mode]]
- **Optional**
Defaults to `defines.control_behavior.lamp.color_mapping`.

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
