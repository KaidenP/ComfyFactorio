---
title: Resistance
tags: [factorio-api, prototype, type]
---
# Resistance

*Note: `Resistance (type)`.*

Resistances to certain types of attacks from enemy, and physical damage. See [Damage](https://wiki.factorio.com/Damage).

## Properties

### type
- **Type:** [[DamageTypeID (type)]]

### decrease
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
The [flat resistance](https://wiki.factorio.com/Damage#Decrease.2C_or_.22flat.22_resistance) to the given damage type. (Higher is better)

### percent
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
The [percentage resistance](https://wiki.factorio.com/Damage#Percentage_resistance) to the given damage type. Expected range is from 0 to 100, e.g. 50 is 50%. (Higher is better.)

## Examples

```
resistances =
{
  {
    type = "physical",
    decrease = 6,
    percent = 30
  },
  {
    type = "explosion",
    decrease = 20,
    percent = 30
  },
  {
    type = "acid",
    decrease = 3,
    percent = 30
  },
  {
    type = "fire",
    decrease = 0,
    percent = 30
  }
}
```
