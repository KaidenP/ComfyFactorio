---
title: EntityTransferTipTrigger
tags: [factorio-api, prototype, type]
---
# EntityTransferTipTrigger

> **Parent:** [[CountBasedTipTrigger]]

Triggered when a player fast-transfers something to or from an entity, similar to the [[on_player_fast_transferred]] event.

## Properties

### type
- **Type:** `"entity-transfer"`

### transfer
- **Type:** `"in"` | `"out"`
- **Optional**
- **Default:** any transfer
Whether the transfer should be into or out of the player.
