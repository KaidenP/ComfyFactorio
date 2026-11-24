---
title: LuaRemote
tags: [factorio-api, runtime, class]
---
# LuaRemote

Registry of interfaces between scripts. An interface is simply a dictionary mapping names to functions. A script or mod can then register an interface with [[LuaRemote]], after that any script can call the registered functions, provided it knows the interface name and the desired function name. An instance of LuaRemote is available through the global object named `remote`.

## Attributes

### interfaces
- **Type:** dictionary<[[string]] → dictionary<[[string]] → `true`>>
List of all registered interfaces. For each interface name, `remote.interfaces[name]` is a dictionary mapping the interface's registered functions to `true`.
**Examples:**

```
-- Assuming the "human interactor" interface is registered as above
game.player.print(tostring(remote.interfaces["human interactor"]["hello"]))        -- prints true
game.player.print(tostring(remote.interfaces["human interactor"]["nonexistent"]))  -- prints nil
```

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### add_interface
Add a remote interface.

**Parameters:**
- **`name`** — [[string]]: Name of the interface. If the name matches any existing interface, an error is thrown.
- **`functions`** — dictionary<[[string]] → function()>: List of functions that are members of the new interface.

### remove_interface
Removes an interface with the given name.

**Parameters:**
- **`name`** — [[string]]: Name of the interface.

**Returns:**
- [[boolean]]: Whether the interface was removed. `false` if the interface didn't exist.

### call
Call a function of an interface.

Providing an unknown interface or function name will result in a script error.

**Parameters:**
- **`interface`** — [[string]]: Interface to look up `function` in.
- **`?`** — [[Any]]: Arguments to pass to the called function. Note that any arguments passed through the interface are a copy of the original, not a reference. Metatables are not retained, while references to LuaObjects stay intact. Functions cannot be passed through the interface.
- **`function`** — [[string]]: Function name that belongs to the `interface`.

**Returns:**
- [[Any]] *(optional)*

## Examples

```
-- Will register a remote interface containing two functions. Later, it will call these functions through `remote`.
remote.add_interface("human interactor",
  {
    hello = function() game.player.print("Hi!") end,
    bye = function(name) game.player.print("Bye " .. name) end
  })
-- Some time later, possibly in a different mod...
remote.call("human interactor", "hello")
remote.call("human interactor", "bye", "dear reader")
```
