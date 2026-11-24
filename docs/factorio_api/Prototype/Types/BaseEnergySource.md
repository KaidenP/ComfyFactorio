---
title: BaseEnergySource
tags: [factorio-api, prototype, type]
---
# BaseEnergySource

> **Abstract**

The abstract base of all [[EnergySource|EnergySources]]. Specifies the way an entity gets its energy.

## Properties

### emissions_per_minute
- **Type:** dictionary<[[AirbornePollutantID]] → [[double (type)]]>
- **Optional**
The pollution an entity emits per minute at full energy consumption. This is exactly the value that is shown in the entity tooltip.

### render_no_power_icon
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether to render the "no power" icon if the entity is low on power. Also applies to the "no fuel" icon when using burner energy sources.

![[no_power_icon.png]]

### render_no_network_icon
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether to render the "no network" icon if the entity is not connected to an electric network.

![[no_network_icon.png]]
