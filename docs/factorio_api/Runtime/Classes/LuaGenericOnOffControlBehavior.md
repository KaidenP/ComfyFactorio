---
title: LuaGenericOnOffControlBehavior
tags: [factorio-api, runtime, class]
---
# LuaGenericOnOffControlBehavior

> **Abstract class** — not directly instantiable.

> **Extends:** [[LuaControlBehavior]]

An abstract base class for behaviors that support switching the entity on or off based on some condition.

## Attributes

### disabled
- **Type:** [[boolean]]
If the entity is currently disabled because of the control behavior.

### circuit_enable_disable
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if this entity enable/disable state is controlled by circuit condition

### circuit_condition
- **Type:** [[CircuitConditionDefinition]]
- **Writable:** [[CircuitConditionDefinition]]
- **Optional**
The circuit condition. Writing `nil` clears the circuit condition.
**Examples:**

```
-- Tell an entity to be active (for example a lamp to be lit) when it receives a
-- circuit signal of more than 4 chain signals.
a_behavior.circuit_condition = {
  comparator=">",
  first_signal={type="item", name="rail-chain-signal"},
  constant=4
}
```

### connect_to_logistic_network
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if this should connect to the logistic network.

### logistic_condition
- **Type:** [[CircuitConditionDefinition]]
- **Writable:** [[CircuitConditionDefinition]]
- **Optional**
The logistic condition. Writing `nil` clears the logistic condition.
**Examples:**

```
-- Tell an entity to be active (for example a lamp to be lit) when the logistics
-- network it's connected to has more than four chain signals.
a_behavior.logistic_condition = {
  comparator=">",
  first_signal={type="item", name="rail-chain-signal"},
  constant=4
}
```
