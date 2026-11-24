---
title: DeliverImpactCombination
tags: [factorio-api, prototype]
---
# DeliverImpactCombination

> **Type name:** `deliver-impact-combination`

## Properties

### type
- **Type:** `"deliver-impact-combination"`

### name
- **Type:** [[string (type)]]
Name of the deliver impact combination.

### impact_category
- **Type:** [[string (type)]]

### deliver_category
- **Type:** [[string (type)]]

### trigger_effect_item
- **Type:** [[TriggerEffect]]

## Example

```
{
  type = "deliver-impact-combination",
  name = "bullet-organic",
  deliver_category = "bullet",
  impact_category = "organic",
  trigger_effect_item =
  {
    type = "play-sound",
    sound =
    {
      category = "weapon",
      variations = sound_variations("__base__/sound/bullets/bullet-impact-organic", 5, 0.3),
      aggregation = {max_count = 4, remove = true, count_already_playing = true}
    }
  }
}
```
