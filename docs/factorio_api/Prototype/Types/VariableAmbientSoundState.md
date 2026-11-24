---
title: VariableAmbientSoundState
tags: [factorio-api, prototype, type]
---
# VariableAmbientSoundState

## Properties

### name
- **Type:** [[string (type)]]
Name has to be unique across all states.

### type
- **Type:** [[VariableAmbientSoundStateType]]
- **Optional**
- **Default:** `"regular"`

### next_state
- **Type:** [[string (type)]]
- **Optional**
Cannot be defined if `next_states` is defined.

Doesn't need to be defined if there is only one state.

### next_states
- **Type:** array<[[VariableAmbientSoundNextStateItem]]>
- **Optional**
Cannot be defined if `next_state` is defined.

Cannot be defined if there is only one state.

Cannot be empty.

### next_state_trigger
- **Type:** [[VariableAmbientSoundNextStateTrigger]]
- **Optional**
Mandatory if there is more than one state or if the only state transitions to itself.

Can be defined for `regular` states only.

### next_state_layers_finished_layers
- **Type:** array<[[string (type)]]>
- **Optional**
List of name of layers used to trigger state transition.

Only loaded, and mandatory if `next_state_trigger` is `"layers-finished"`.

### state_duration_seconds
- **Type:** [[uint32 (type)]]
- **Optional**
Defines for how long this state will be active.

Mandatory if `next_state_trigger` is `"duration"`.

Optionally loaded for `intermezzo` states.

### layers_properties
- **Type:** array<[[VariableAmbientSoundLayerStateProperties]]>
- **Optional**
Must contain as many items as there is layers in the variable track. The items themselves can be empty. The order of items corresponds to the order of layers as they appear in the prototype definition.

Mandatory for `regular` and `final` states.

Cannot be defined for `intermezzo` or `stop` states.

### start_pause
- **Type:** [[RandomRange]]
- **Optional**
Pause before a layer starts playing.

Optionally loaded for `intermezzo` states.

### end_pause
- **Type:** [[RandomRange]]
- **Optional**
Pause before a layer finishes playing. The layer being finished is not counted until the pause finishes.

Optionally loaded for `intermezzo` states.

### number_of_enabled_layers
- **Type:** [[RandomRange]]
- **Optional**
Defines how many layers will be playing. Which layers will be playing is selected randomly.

The minimum cannot be zero, the maximum cannot be greater than the number of layers.

Cannot be defined if any of `layers_properties` define the `enabled` property.

Cannot be defined for `intermezzo` or `stop` states.
