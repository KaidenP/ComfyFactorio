---
title: CargoDestination
tags: [factorio-api, runtime, concept]
---
# CargoDestination

The destination of a cargo pod.

## Fields

### type
- **Type:** [[defines.cargo_destination]]
The type of destination.

### station
- **Type:** [[LuaEntity]]
- **Optional**
Only used if `type` is [[defines.cargo_destination#station|station]]. Must be entity of type `cargo-landing-pad` or `space-platform-hub`.

### hatch
- **Type:** [[LuaCargoHatch]]
- **Optional**
Only used if `type` is [[defines.cargo_destination#station|station]]. Must be connected to the station and not reserved.

### transform_launch_products
- **Type:** [[boolean]]
- **Optional**
Only used if `type` is [[defines.cargo_destination#station|station]] or [[defines.cargo_destination#surface|surface]]. If true, items with [[ItemPrototype#rocket_launch_products|rocket_launch_products]] defined will be transformed into their products before starting descent. Defaults to `false`.

### surface
- **Type:** [[SurfaceIdentification]]
- **Optional**
Only used if `type` is [[defines.cargo_destination#surface|surface]].

### position
- **Type:** [[MapPosition]]
- **Optional**
Only used if `type` is [[defines.cargo_destination#surface|surface]]. Determines the position on the surface to land near. If not provided, cargo pod will switch destination type from [[defines.cargo_destination#surface|surface]] to [[defines.cargo_destination#station|station]] before starting descent if there is a station available, and will land at {0, 0} if there is no station available.

### land_at_exact_position
- **Type:** [[boolean]]
- **Optional**
Only used if `type` is [[defines.cargo_destination#surface|surface]] and `position` is specified. Determines whether to land at `position` exactly or at a random location nearby. Defaults to `false`.

### space_platform
- **Type:** [[LuaSpacePlatform]]
- **Optional**
Only used if `type` is [[defines.cargo_destination#space_platform|space_platform]]. Only used for sending space platform starter packs to a platform that is waiting for a starter pack.
