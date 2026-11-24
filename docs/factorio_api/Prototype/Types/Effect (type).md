---
title: Effect
tags: [factorio-api, prototype, type]
---
# Effect

*Note: `Effect (type)`.*

When applied to [[ModulePrototype|modules]], the resulting effect is a sum of all module effects, multiplied through calculations: `(1 + sum module effects)`, or `(0 + sum)` for productivity.

## Properties

### consumption
- **Type:** [[EffectValue (type)]]
- **Optional**
Multiplier to energy used during operation (not idle/drain use). The minimum possible sum defaults to -80% and can be changed through [[EffectReceiver (type)#consumption_limits|EffectReceiver::consumption_limits]] on the machine.

### speed
- **Type:** [[EffectValue (type)]]
- **Optional**
Modifier to crafting speed, research speed, etc. The minimum possible sum defaults to -80% and can be changed through [[EffectReceiver (type)#speed_limits|EffectReceiver::speed_limits]] on the machine.

### productivity
- **Type:** [[EffectValue (type)]]
- **Optional**
Multiplied against work completed, adds to the bonus results of operating. E.g. an extra crafted recipe or immediate research bonus. The minimum possible sum defaults to -80% and can be changed through [[EffectReceiver (type)#productivity_limits|EffectReceiver::productivity_limits]] on the machine.

### pollution
- **Type:** [[EffectValue (type)]]
- **Optional**
Multiplier to the pollution factor of an entity's pollution during use. The minimum possible sum defaults to -80% and can be changed through [[EffectReceiver (type)#pollution_limits|EffectReceiver::pollution_limits]] on the machine.

### quality
- **Type:** [[EffectValue (type)]]
- **Optional**
Adds a bonus chance to increase a product's quality. The minimum possible sum defaults to 0% and can be changed through [[EffectReceiver (type)#quality_limits|EffectReceiver::quality_limits]] on the machine. If negative values are allowed on the effect receiver, the product's quality can be [[QualityPrototype#previous_probability|decreased]].

## Examples

```
-- These are the effects of the vanilla Speed Module 3
{speed = 0.5, consumption = 0.7, quality = -0.025}
```
