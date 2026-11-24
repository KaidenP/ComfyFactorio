---
title: LuaSettings
tags: [factorio-api, runtime, class]
---
# LuaSettings

Object containing the three different types of mod settings: startup settings, global runtime settings and per-player runtime settings. An instance of LuaSettings is available through the global object named `settings`.

## Attributes

### startup
- **Type:** LuaCustomTable<[[string]] → [[ModSetting]]>
The startup mod settings, indexed by prototype name.

### global
- **Type:** LuaCustomTable<[[string]] → [[ModSetting]]>
The current global mod settings, indexed by prototype name.

Even though this attribute is marked as read-only, individual settings can be changed by overwriting their [[ModSetting]] table. Mods can only change their own settings. Using the in-game console, all player settings can be changed.

### player_default
- **Type:** LuaCustomTable<[[string]] → [[ModSetting]]>
The **default** player mod settings for this map, indexed by prototype name. Changing these settings only affects the default settings for future players joining the game.

Individual settings can be changed by overwriting their [[ModSetting]] table. Mods can only change their own settings. Using the in-game console, all player settings can be changed.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### get_player_settings
Gets the current per-player settings for the given player, indexed by prototype name. Returns the same structure as [[LuaPlayer#mod_settings|LuaPlayer::mod_settings]]. This table becomes invalid if its associated player does.

Even though this attribute is a getter, individual settings can be changed by overwriting their [[ModSetting]] table. Mods can only change their own settings. Using the in-game console, all player settings can be changed.

**Parameters:**
- **`player`** — [[PlayerIdentification]]

**Returns:**
- LuaCustomTable<[[string]] → [[ModSetting]]>

**Examples:**

```
-- Change the value of the "active_lifestyle" setting
settings.get_player_settings(player_index)["active_lifestyle"] = {value = true}
```
