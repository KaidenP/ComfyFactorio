---
title: CargoStationParameters
tags: [factorio-api, prototype, type]
---
# CargoStationParameters

*Note: `CargoStationParameters (type)`.*

A cargo station is any entity that has the capacity to send cargo units. In Space Age those are [[RocketSiloPrototype]], [[SpacePlatformHubPrototype]] and [[CargoLandingPadPrototype]]. [[CargoBayPrototype|Cargo bays]] may provide additional cargo hatches to cargo stations which are cargo bay connectable.

## Properties

### prefer_packed_cargo_units
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Packed cargo units will wait for the full order to be completed. This is useful to save rockets in rocket silos when items trickle in slowly. The platform hub has immediate access to items so false is better to allow partial fulfillments.

### hatch_definitions
- **Type:** array<[[CargoHatchDefinition (type)]]>
- **Optional**

### giga_hatch_definitions
- **Type:** array<[[GigaCargoHatchDefinition]]>
- **Optional**
Big additional hatch that goes over the actual hatches.

### is_input_station
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If set to false, this station will not accept incoming cargo units even if it has hatches that can. (can occur through linked cargo bays)

### is_output_station
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If set to false, this station will not dispatch cargo units even if it has hatches that can. (can occur through linked cargo bays)
