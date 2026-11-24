---
title: LuaDisplayPanelControlBehavior
tags: [factorio-api, runtime, class]
---
# LuaDisplayPanelControlBehavior

> **Extends:** [[LuaControlBehavior]]

Control behavior for display panels.

## Attributes

### max_records_count
- **Type:** [[uint32]]
Provides a maximum amount of records that can be added to this behavior. When at full capacity, attempts to add more records will fail.

### records_count
- **Type:** [[uint32]]
Current amount of records this control behavior has.

### records
- **Type:** array<[[DisplayPanelMessageDefinition]]>
- **Writable:** array<[[DisplayPanelMessageDefinition]]>
The full list of configured messages.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### add_record
Adds a single message record.

**Parameters:**
- **`message`** — [[DisplayPanelMessageDefinition]]: Message record to be added.
- **`index`** — [[uint32]] *(optional)*: Index at which this record should be inserted. Must be within [[LuaDisplayPanelControlBehavior#records_count]] + 1]. When not provided, record will be appended.

**Returns:**
- [[boolean]]: If a message record was added.

### remove_record
Removes message record at specified index.

**Parameters:**
- **`index`** — [[uint32]]: Index of the message record to be removed. Must be within [[LuaDisplayPanelControlBehavior#records_count]]].

### move_record
Moves record from old position to a new position

**Parameters:**
- **`old_index`** — [[uint32]]: Index where the record to be moved is currently.
- **`new_index`** — [[uint32]]: Index where the record should be moved to.

### get_record
Get a single record.

**Parameters:**
- **`index`** — [[uint32]]: Index of the record to read.

**Returns:**
- [[DisplayPanelMessageDefinition]]

### set_record
Change content of a specific record.

**Parameters:**
- **`index`** — [[uint32]]: Index of the record to change
- **`record`** — [[DisplayPanelMessageDefinition]]
