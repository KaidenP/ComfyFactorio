---
title: TemporaryContainerPrototype
tags: [factorio-api, prototype]
---
# TemporaryContainerPrototype

> **Parent:** [[ContainerPrototype]] · **Type name:** `temporary-container`

A container that can automatically destroy itself when it is emptied or after it has existed for a certain time.

## Properties

### destroy_on_empty
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the container is automatically destroyed when it is emptied.

### time_to_live
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Duration after which the container and its contents are automatically destroyed. In ticks, 0 for infinite.

### alert_after_time
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
If the container has existed for this long, [[UtilitySprites#unclaimed_cargo_icon|an alert]] is show on it. In ticks, 0 for no alert.
