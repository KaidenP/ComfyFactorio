---
title: LuaLogisticSection
tags: [factorio-api, runtime, class]
---
# LuaLogisticSection

Logistic section of a particular [[LuaLogisticPoint]] or [[LuaConstantCombinatorControlBehavior]].

## Attributes

### owner
- **Type:** [[LuaEntity]]
The [[LuaEntity]] owner of this LuaLogisticSection.

### index
- **Type:** [[uint32]]
The section index of this section.

### filters
- **Type:** array<[[LogisticFilter]]>
- **Writable:** array<[[LogisticFilter]]>
The logistic filters for this section.

This can only be written to when the section [[LuaLogisticSection#is_manual|is manual]].

### filters_count
- **Type:** [[uint32]]
Amount of filters this section has

### group
- **Type:** [[string]]
- **Writable:** [[string]]
The group this section belongs to.

An empty string when in no group.

This can only be written to when the section [[LuaLogisticSection#is_manual|is manual]].

### type
- **Type:** [[defines.logistic_section_type]]
The type of this logistic section. Sections that are not manual are controlled by game itself and may not be allowed to be changed by script.

### is_manual
- **Type:** [[boolean]]
Shortcut to check whether [[LuaLogisticSection#type|LuaLogisticSection::type]] is equal to [[defines.logistic_section_type#manual|manual]].

### active
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this section is active. This can only be written to when the section [[LuaLogisticSection#is_manual|is manual]].

### multiplier
- **Type:** [[float]]
- **Writable:** [[float]]
Multiplier applied to all filters before they are used by game. This can only be written to when the section [[LuaLogisticSection#is_manual|is manual]].

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### set_slot
Sets logistic request and auto-trash slot to the given value.

This will silently fail if personal logistics are not researched yet.

This can only be called when the section [[LuaLogisticSection#is_manual|is manual]].

**Parameters:**
- **`slot_index`** — [[LogisticFilterIndex]]: Index of a slot to set.
- **`filter`** — [[LogisticFilter]]: The details of the filter to set.

**Returns:**
- [[LogisticFilterIndex]] *(optional)*: The existing index for the given filter or nil if the filter was successfully set.

**Raises:**
- [[on_entity_logistic_slot_changed]] *(timeframe: instantly)*: Raised if setting of logistic slot was successful.

### get_slot
Gets current settings of logistic request and auto-trash from the given slot.

**Parameters:**
- **`slot_index`** — [[LogisticFilterIndex]]: Index of a slot to read.

**Returns:**
- [[LogisticFilter]]

### clear_slot
Clears the logistic request and auto-trash from the given slot.

This can only be called when the section [[LuaLogisticSection#is_manual|is manual]].

**Parameters:**
- **`slot_index`** — [[LogisticFilterIndex]]: Index of a slot to clear.
