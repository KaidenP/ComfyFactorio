---
title: ElectricEnergySource
tags: [factorio-api, prototype, type]
---
# ElectricEnergySource

> **Parent:** [[BaseEnergySource]]

## Properties

### type
- **Type:** `"electric"`

### buffer_capacity
- **Type:** [[Energy]]
- **Optional**
How much energy this entity can hold.
**Examples:**

```
buffer_capacity = "5MJ"
```

### usage_priority
- **Type:** [[ElectricUsagePriority]]
**Examples:**

```
usage_priority = "secondary-input"
```

### input_flow_limit
- **Type:** [[Energy]]
- **Optional**
- **Default:** Max `double` value
The rate at which energy can be taken, from the network, to refill the energy buffer. `0` means no transfer.
**Examples:**

```
input_flow_limit = "300kW"
```

### output_flow_limit
- **Type:** [[Energy]]
- **Optional**
- **Default:** Max `double` value
The rate at which energy can be provided, to the network, from the energy buffer. `0` means no transfer.
**Examples:**

```
output_flow_limit = "300kW"
```

### drain
- **Type:** [[Energy]]
- **Optional**
How much energy (per second) will be continuously removed from the energy buffer. It is applied as a constant consumption-per-tick, even when the entity is not [[LuaEntity#active|active]].

If this is an output energy source then the drain will only affect this energy source's buffer, it will not result in energy being drawn from the network.

If this is an input energy source then the drain is shown in the tooltip as "Min. [Minimum] Consumption".
**Examples:**

```
drain = "1kW"
```

## Examples

```
energy_source = -- energy source of oil pumpjack
{
  type = "electric",
  emissions_per_minute = { pollution = 10 },
  usage_priority = "secondary-input"
}
```

```
energy_source = -- energy source of accumulator
{
  type = "electric",
  buffer_capacity = "5MJ",
  usage_priority = "tertiary",
  input_flow_limit = "300kW",
  output_flow_limit = "300kW"
}
```

```
energy_source = -- energy source of steam engine
{
  type = "electric",
  usage_priority = "secondary-output"
}
```
