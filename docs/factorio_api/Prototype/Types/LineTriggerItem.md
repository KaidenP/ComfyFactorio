---
title: LineTriggerItem
tags: [factorio-api, prototype, type]
---
# LineTriggerItem

> **Parent:** [[TriggerItem (type)]]

## Properties

### type
- **Type:** `"line"`

### range
- **Type:** [[double (type)]]

### width
- **Type:** [[double (type)]]

### range_effects
- **Type:** [[TriggerEffect]]
- **Optional**

## Examples

```
action =
{
  type = "line",
  range = 25,
  width = 0.5,

  range_effects =
  {
    type = "create-explosion",
    entity_name = "railgun-beam"
  },

  action_delivery =
  {
    type = "instant",
    target_effects =
    {
      type = "damage",
      damage = { amount = 100, type = "physical"}
    }
  }
}
```
