---
title: RepairToolPrototype
tags: [factorio-api, prototype]
---
# RepairToolPrototype

> **Parent:** [[ToolPrototype]] · **Type name:** `repair-tool`

A [repair pack](https://wiki.factorio.com/Repair_pack). Using the tool decreases durability to restore entity health.

## Properties

### speed
- **Type:** [[float (type)]]
Entity health repaired per used [[ToolPrototype#durability|ToolPrototype::durability]]. E.g. a repair tool with 5 durability and a repair speed of 2 will restore 10 health.

This is then multiplied by the [[EntityWithHealthPrototype#repair_speed_modifier|EntityWithHealthPrototype::repair_speed_modifier]] of the entity.
