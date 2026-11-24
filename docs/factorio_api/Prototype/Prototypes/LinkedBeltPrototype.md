---
title: LinkedBeltPrototype
tags: [factorio-api, prototype]
---
# LinkedBeltPrototype

> **Parent:** [[TransportBeltConnectablePrototype]] · **Type name:** `linked-belt`

A belt that can be connected to a belt anywhere else, including on a different surface. The linked belts have to be [connected with console commands](https://wiki.factorio.com/Console#Connect_linked_belts) or runtime scripting in mods or scenarios. [[LuaEntity#connect_linked_belts|LuaEntity::connect_linked_belts]] and other runtime functions.

## Properties

### structure
- **Type:** [[LinkedBeltStructure]]
- **Optional**

### structure_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### allow_clone_connection
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### allow_blueprint_connection
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### allow_side_loading
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
