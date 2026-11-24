---
title: CargoPodPrototype
tags: [factorio-api, prototype]
---
# CargoPodPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `cargo-pod`

Entity used to send cargo between the [[CargoHatchDefinition (type)|cargo hatches]] of [[CargoLandingPadPrototype|cargo landing pads]], [[SpacePlatformHubPrototype|space platform hubs]], [[CargoBayPrototype|cargo bays]] and [[RocketSiloPrototype|rocket silos]].

The pod for sending cargo is determined by [[CargoHatchDefinition (type)#cargo_unit_entity_to_spawn|CargoHatchDefinition::cargo_unit_entity_to_spawn]]. A cargo pod will only be sent to a destination if [[CargoHatchDefinition (type)#receiving_cargo_units|receiving_cargo_units]] of the destination hatch contains the cargo pod.

## Properties

### default_graphic
- **Type:** [[ProcessionGraphic]]
- **Optional**
Has to be of type 'pod-catalogue'.

### default_shadow_graphic
- **Type:** [[ProcessionGraphic]]
- **Optional**
Has to be of type 'pod-catalogue'.

### procession_graphic_catalogue
- **Type:** [[ProcessionGraphicCatalogue]]
- **Optional**

### procession_audio_catalogue
- **Type:** [[ProcessionAudioCatalogue]]
- **Optional**

### shadow_slave_entity
- **Type:** [[EntityID (type)]]
- **Optional**

### inventory_size
- **Type:** [[ItemStackIndex (type)]]
The amount of item stacks that this cargo pod can transport.

### spawned_container
- **Type:** [[EntityID (type)]]
The entity that is created if this cargo pod lands on the ground instead of in a cargo hatch. The transported items will be transferred into the spawned entity.

### impact_trigger
- **Type:** [[Trigger]]
- **Optional**

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
