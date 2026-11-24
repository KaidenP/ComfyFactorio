---
title: LuaControl
tags: [factorio-api, runtime, class]
---
# LuaControl

> **Abstract class** — not directly instantiable.

This is an abstract base class containing the common functionality between [[LuaPlayer]] and entities (see [[LuaEntity]]). When accessing player-related functions through a [[LuaEntity]], it must refer to a character entity.

## Attributes

### surface
- **Type:** [[LuaSurface]]
The surface this entity is currently on.

### surface_index
- **Type:** [[uint32]]
Unique [[LuaSurface#index|index]] (ID) associated with the surface this entity is currently on.

### position
- **Type:** [[MapPosition]]
The current position of the entity.

### render_position
- **Type:** [[MapPosition]]
The current render position of the entity.

### is_flying
- **Type:** [[boolean]]
If this player or character entity is flying.

When called on an entity, only valid if this entity is a character.

### flight_height
- **Type:** [[double]]
The current flight height for this player or character entity.

When called on an entity, only valid if this entity is a character.

### vehicle
- **Type:** [[LuaEntity]]
- **Optional**
The vehicle the player is currently sitting in.

### cargo_pod
- **Type:** [[LuaEntity]]
- **Optional**
The cargo pod the player is currently sitting in or the cargo pod attached to this rocket silo.

### hub
- **Type:** [[LuaEntity]]
- **Optional**
The space platform hub the player is currently sitting in.

### force
- **Type:** [[LuaForce]]
- **Writable:** [[ForceID]]
The force of this entity. Reading will always give a [[LuaForce]], but it is possible to assign either [[string]], [[uint8]] or [[LuaForce]] to this attribute to change the force.

### force_index
- **Type:** [[uint32]]
Unique [[LuaForce#index|index]] (ID) associated with the force of this entity.

### selected
- **Type:** [[LuaEntity]]
- **Writable:** [[LuaEntity]]
- **Optional**
The currently selected entity. Assigning an entity will select it if is selectable, otherwise the selection is cleared.

### opened
- **Type:** [[LuaEntity]] | [[LuaItemStack]] | [[LuaEquipment]] | [[LuaEquipmentGrid]] | [[LuaPlayer]] | [[LuaGuiElement]] | [[LuaInventory]] | [[LuaLogisticNetwork]] | [[LuaTile]] | [[LuaRecord]] | [[defines.gui_type]]
- **Writable:** [[LuaEntity]] | [[LuaItemStack]] | [[LuaEquipment]] | [[LuaEquipmentGrid]] | [[LuaPlayer]] | [[LuaGuiElement]] | [[LuaInventory]] | [[LuaLogisticNetwork]] | [[LuaTile]] | [[LuaRecord]] | [[defines.gui_type]]
- **Optional**
The GUI the player currently has open.

This is the GUI that will asked to close (by firing the [[on_gui_closed]] event) when the `Esc` or `E` keys are pressed. If this attribute is non-nil, then writing `nil` or a new GUI to it will ask the existing GUI to close.

Write supports any of the types. Read will return the `entity`, `equipment`, `equipment-grid`, `player`, `element`, `inventory`, `item`, `tile`, or `nil`.

### crafting_queue_size
- **Type:** [[uint32]]
Size of the crafting queue.

### crafting_queue_progress
- **Type:** [[double]]
- **Writable:** [[double]]
The crafting queue progress in the range `[0-1]`. `0` when no recipe is being crafted.

### walking_state
- **Type:** table
- **Writable:** table
Current walking state of the player, or the spider-vehicle the character is driving.
**Examples:**

```
-- Make the player go north. Note that a one-shot action like this will only make the player walk for one tick.
game.player.walking_state = {walking = true, direction = defines.direction.north}
```

### riding_state
- **Type:** [[RidingState]]
- **Writable:** [[RidingState]]
Current riding state of this car, or of the car this player is riding in.

### mining_state
- **Type:** table
- **Writable:** table
Current mining state. Will error if written to with a [[LuaPlayer#controller_type|controller_type]] other than `character`, `god`, or `editor`.

When the player isn't mining tiles the player will mine whatever entity is currently selected. See [[LuaControl#selected|LuaControl::selected]] and [[LuaControl#update_selected_entity|LuaControl::update_selected_entity]].

### shooting_state
- **Type:** table
- **Writable:** table
Current shooting state.

### picking_state
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Current item-picking state.

### repair_state
- **Type:** table
- **Writable:** table
Current repair state.

### mining_progress
- **Type:** [[double]]
- **Writable:** [[double]]
For characters and players the number is between 0 and 1.

For mining drills the number is with the range [0, mining_target.prototype.mineable_properties.mining_time].

For all other types the number is 0.

### cursor_stack
- **Type:** [[LuaItemStack]]
- **Optional**
The player's cursor stack. `nil` if the player controller is a spectator.
**Examples:**

```
-- Even though this property is marked as read-only, it returns a LuaItemStack,
-- meaning it can be manipulated like so:
player.cursor_stack.clear()
```

### cursor_ghost
- **Type:** [[ItemIDAndQualityIDPair]]
- **Writable:** [[ItemWithQualityID]]
- **Optional**
The ghost prototype in the player's cursor.

Items in the cursor stack will take priority over the cursor ghost.

### cursor_record
- **Type:** [[LuaRecord]]
- **Optional**
The blueprint record in the player's cursor.

### driving
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if the player is in a vehicle. Writing to this attribute puts the player in or out of a vehicle.

### crafting_queue
- **Type:** array<[[CraftingQueueItem]]>
- **Optional**
The current crafting queue items.

### following_robots
- **Type:** array<[[LuaEntity]]>
The current combat robots following the character.

When called on a [[LuaPlayer]], it must be associated with a character (see [[LuaPlayer#character|LuaPlayer::character]]).

### cheat_mode
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
When `true` hand crafting is free and instant.

### character_crafting_speed_modifier
- **Type:** [[double]]
- **Writable:** [[double]]
When called on a [[LuaPlayer]], it must be associated with a character (see [[LuaPlayer#character|LuaPlayer::character]]).

### character_mining_speed_modifier
- **Type:** [[double]]
- **Writable:** [[double]]
When called on a [[LuaPlayer]], it must be associated with a character (see [[LuaPlayer#character|LuaPlayer::character]]).

### character_additional_mining_categories
- **Type:** array<[[string]]>
- **Writable:** array<[[string]]>
When called on a [[LuaPlayer]], it must be associated with a character (see [[LuaPlayer#character|LuaPlayer::character]]).

### character_running_speed_modifier
- **Type:** [[double]]
- **Writable:** [[double]]
Modifies the running speed of this character by the given value as a percentage. Setting the running modifier to `0.5` makes the character run 50% faster. The minimum value of `-1` reduces the movement speed by 100%, resulting in a speed of `0`.

When called on a [[LuaPlayer]], it must be associated with a character (see [[LuaPlayer#character|LuaPlayer::character]]).

### character_build_distance_bonus
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
When called on a [[LuaPlayer]], it must be associated with a character (see [[LuaPlayer#character|LuaPlayer::character]]).

### character_item_drop_distance_bonus
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
When called on a [[LuaPlayer]], it must be associated with a character (see [[LuaPlayer#character|LuaPlayer::character]]).

### character_reach_distance_bonus
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
When called on a [[LuaPlayer]], it must be associated with a character (see [[LuaPlayer#character|LuaPlayer::character]]).

### character_resource_reach_distance_bonus
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
When called on a [[LuaPlayer]], it must be associated with a character (see [[LuaPlayer#character|LuaPlayer::character]]).

### character_item_pickup_distance_bonus
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
When called on a [[LuaPlayer]], it must be associated with a character (see [[LuaPlayer#character|LuaPlayer::character]]).

### character_loot_pickup_distance_bonus
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
When called on a [[LuaPlayer]], it must be associated with a character (see [[LuaPlayer#character|LuaPlayer::character]]).

### character_inventory_slots_bonus
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
When called on a [[LuaPlayer]], it must be associated with a character (see [[LuaPlayer#character|LuaPlayer::character]]).

### character_trash_slot_count_bonus
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
When called on a [[LuaPlayer]], it must be associated with a character (see [[LuaPlayer#character|LuaPlayer::character]]).

### character_maximum_following_robot_count_bonus
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
When called on a [[LuaPlayer]], it must be associated with a character (see [[LuaPlayer#character|LuaPlayer::character]]).

### character_health_bonus
- **Type:** [[float]]
- **Writable:** [[float]]
When called on a [[LuaPlayer]], it must be associated with a character (see [[LuaPlayer#character|LuaPlayer::character]]).

### opened_gui_type
- **Type:** [[defines.gui_type]]
- **Optional**

### build_distance
- **Type:** [[uint32]]
The build distance of this character or max uint when not a character or player connected to a character.

### drop_item_distance
- **Type:** [[uint32]]
The item drop distance of this character or max uint when not a character or player connected to a character.

### reach_distance
- **Type:** [[uint32]]
The reach distance of this character or max uint when not a character or player connected to a character.

### item_pickup_distance
- **Type:** [[double]]
The item pickup distance of this character or max double when not a character or player connected to a character.

### loot_pickup_distance
- **Type:** [[double]]
The loot pickup distance of this character or max double when not a character or player connected to a character.

### resource_reach_distance
- **Type:** [[double]]
The resource reach distance of this character or max double when not a character or player connected to a character.

### in_combat
- **Type:** [[boolean]]
Whether this character entity is in combat.

### character_running_speed
- **Type:** [[double]]
The current movement speed of this character, including effects from exoskeletons, tiles, stickers and shooting.

### character_mining_progress
- **Type:** [[double]]
The current mining progress between 0 and 1 of this character, or 0 if they aren't mining.

## Methods

### get_inventory
Get an inventory belonging to this entity. This can be either the "main" inventory or some auxiliary one, like the module slots or logistic trash slots.

A given [[defines.inventory]] is only meaningful for the corresponding LuaObject type. EG: get_inventory(defines.inventory.character_main) is only meaningful if 'this' is a player character. You may get a value back but if the type of 'this' isn't the type referred to by the [[defines.inventory]] it's almost guaranteed to not be the inventory asked for.

**Parameters:**
- **`inventory`** — [[defines.inventory]]

**Returns:**
- [[LuaInventory]] *(optional)*: The inventory or `nil` if none with the given index was found.

### get_inventory_name
Get name of inventory. Names match keys of [[defines.inventory]].

**Parameters:**
- **`inventory`** — [[defines.inventory]]

**Returns:**
- [[string]] *(optional)*

### get_max_inventory_index
The highest index of all inventories this entity can use. Allows iteration over all of them if desired.

**Returns:**
- [[defines.inventory]]

**Examples:**

```
for k = 1, entity.get_max_inventory_index() do [...] end
```

### get_main_inventory
Gets the main inventory for this character or player if this is a character or player.

**Returns:**
- [[LuaInventory]] *(optional)*: The inventory or `nil` if this entity is not a character or player.

### can_insert
Can at least some items be inserted?

**Parameters:**
- **`items`** — [[ItemStackIdentification]]: Items that would be inserted.

**Returns:**
- [[boolean]]: `true` if at least a part of the given items could be inserted into this inventory.

### insert
Insert items into this entity. This works the same way as inserters or shift-clicking: the "best" inventory is chosen automatically.

**Parameters:**
- **`items`** — [[ItemStackIdentification]]: The items to insert.

**Returns:**
- [[uint32]]: The number of items that were actually inserted.

### set_gui_arrow
Create an arrow which points at this entity. This is used in the tutorial. For examples, see `control.lua` in the campaign missions.

Takes a table with the following fields:
- **`margin`** — [[uint32]]
- **`type`** — [[GuiArrowType]]: Where to point to. This field determines what other fields are mandatory.

Other attributes may be specified depending on `type`:

**Variant `crafting_queue`:**
  - **`crafting_queueindex`** — [[uint32]]: Index in the crafting queue to point to.

**Variant `entity`:**
  - **`entity`** — [[LuaEntity]]

**Variant `item_stack`:**
  - **`inventory_index`** — [[defines.inventory]]: Which inventory the stack is in.
  - **`item_stack_index`** — [[uint32]]: Which stack to point to.
  - **`source`** — `"player"` | `"target"` | `"player-quickbar"`

**Variant `position`:**
  - **`position`** — [[MapPosition]]

### clear_gui_arrow
Removes the arrow created by `set_gui_arrow`.

### get_item_count
Get the number of all or some items in this entity.

**Parameters:**
- **`item`** — [[ItemFilter]] *(optional)*: The item to count. If not specified, count all items.

**Returns:**
- [[uint32]]

### has_items_inside
Does this entity have any item inside it?

**Returns:**
- [[boolean]]

### can_reach_entity
Can a given entity be opened or accessed?

**Parameters:**
- **`entity`** — [[LuaEntity]]

**Returns:**
- [[boolean]]

### clear_items_inside
Remove all items from this entity.

### remove_item
Remove items from this entity.

**Parameters:**
- **`items`** — [[ItemStackIdentification]]: The items to remove.

**Returns:**
- [[uint32]]: The number of items that were actually removed.

### teleport
Teleport the entity to a given position, possibly on another surface.

Some entities may not be teleported. For instance, transport belts won't allow teleportation and this method will always return `false` when used on any such entity.

You can also pass 1 or 2 numbers as the parameters and they will be used as relative teleport coordinates `'teleport(0, 1)'` to move the entity 1 tile positive y. `'teleport(4)'` to move the entity 4 tiles to the positive x.

`script_raised_teleported` will not be raised if teleporting a player with no character.

**Parameters:**
- **`position`** — [[MapPosition]]: Where to teleport to.
- **`surface`** — [[SurfaceIdentification]] *(optional)*: Surface to teleport to. If not given, will teleport to the entity's current surface. Only players, cars, and spidertrons can be teleported cross-surface.
- **`raise_teleported`** — [[boolean]] *(optional)*: If true, [[defines.events#script_raised_teleported|defines.events.script_raised_teleported]] will be fired on successful entity teleportation.
- **`snap_to_grid`** — [[boolean]] *(optional)*: If false the exact position given is used to instead of snapping to the normal entity grid. This only applies if the entity normally snaps to the grid.
- **`build_check_type`** — [[defines.build_check_type]] *(optional)*: The build check type done when teleporting to the destination. Defaults to `script`. This is ignored when teleporting between surfaces.

**Returns:**
- [[boolean]]: `true` if the entity was successfully teleported.

**Raises:**
- [[on_player_changed_position]] *(timeframe: instantly)*: Raised if the teleported entity is a player character.
- [[script_raised_teleported]] *(timeframe: instantly)*: Raised if the `raise_teleported` flag was set and the entity was successfully teleported.

### update_selected_entity
Select an entity, as if by hovering the mouse above it.

**Parameters:**
- **`position`** — [[MapPosition]]: Position of the entity to select.

**Raises:**
- [[on_selected_entity_changed]] *(timeframe: instantly)*: Raised if there is an entity at the given position to select.

### clear_selected_entity
Unselect any selected entity.

**Raises:**
- [[on_selected_entity_changed]] *(timeframe: instantly)*: Raised if there is a currently selected entity.

### disable_flashlight
Disable the flashlight.

Applied per controller. Only supported by [[defines.controllers#character|defines.controllers.character]] and [[defines.controllers#remote|defines.controllers.remote]].

### enable_flashlight
Enable the flashlight.

Applied per controller. Only supported by [[defines.controllers#character|defines.controllers.character]] and [[defines.controllers#remote|defines.controllers.remote]].

### is_flashlight_enabled
Is the flashlight enabled for the current controller. Only supported by [[defines.controllers#character|defines.controllers.character]] and [[defines.controllers#remote|defines.controllers.remote]].

**Returns:**
- [[boolean]]

### get_craftable_count
Gets the count of the given recipe that can be crafted.

**Parameters:**
- **`recipe`** — [[RecipeID]]: The recipe.

**Returns:**
- [[uint32]]: The count that can be crafted.

### begin_crafting
Begins crafting the given count of the given recipe.

Takes a table with the following fields:
- **`count`** — [[uint32]]: The count to craft.
- **`recipe`** — [[RecipeID]]: The recipe to craft.
- **`silent`** — [[boolean]] *(optional)*: If false and the recipe can't be crafted the requested number of times printing the failure is skipped.

**Returns:**
- [[uint32]]: The count that was actually started crafting.

**Raises:**
- [[on_player_main_inventory_changed]] *(timeframe: current_tick)*: Raised if crafting was able to be started.
- [[on_pre_player_crafted_item]] *(timeframe: instantly)*: Raised if crafting was able to be started.

### cancel_crafting
Cancels the given amount of crafts at the given crafting queue position. If this causes any later crafts that depend on the cancelled one to have insufficient ingredients, those crafts will also be cancelled.

Takes a table with the following fields:
- **`index`** — [[uint32]]: The crafting queue index.
- **`count`** — [[uint32]]: The count to cancel crafting.

**Raises:**
- [[on_player_cancelled_crafting]] *(timeframe: instantly)*: Raised if crafting was able to be cancelled.
- [[on_player_main_inventory_changed]] *(timeframe: current_tick)*: Raised if crafting was able to be cancelled.

### mine_entity
Mines the given entity as if this player (or character) mined it.

**Parameters:**
- **`entity`** — [[LuaEntity]]: The entity to mine
- **`force`** — [[boolean]] *(optional)*: Forces mining the entity even if the items can't fit in the player.

**Returns:**
- [[boolean]]: Whether the mining succeeded.

**Raises:**
- [[on_player_mined_entity]] *(timeframe: instantly)*: Raised if mining is successful.
- [[on_player_mined_item]] *(timeframe: instantly)*: Raised if mining is successful.
- [[on_pre_player_mined_item]] *(timeframe: instantly)*: Raised if mining is possible.

### mine_tile
Mines the given tile as if this player (or character) mined it.

**Parameters:**
- **`tile`** — [[LuaTile]]: The tile to mine.

**Returns:**
- [[boolean]]: Whether the mining succeeded.

**Raises:**
- [[on_player_mined_item]] *(timeframe: instantly)*: Raised if mining is successful.
- [[on_player_mined_tile]] *(timeframe: instantly)*: Raised if mining is successful.

### is_player
When `true` control adapter is a LuaPlayer object, `false` for entities including characters with players.

**Returns:**
- [[boolean]]

### open_technology_gui
Open the technology GUI and select a given technology.

**Parameters:**
- **`technology`** — [[TechnologyID]] *(optional)*: The technology to select after opening the GUI.

### open_factoriopedia_gui
Open the Factoriopedia GUI and select a given entry, if any valid ID is given.

**Parameters:**
- **`prototype`** — [[FactoriopediaID]] *(optional)*

### close_factoriopedia_gui
Closes the Factoriopedia GUI if it's open.

### is_cursor_blueprint
Returns whether the player is holding a blueprint. This takes both blueprint items as well as blueprint records from the blueprint library into account.

Note that both this method refers to the currently selected blueprint, which means that a blueprint book with a selected blueprint will return the information as well.

**Returns:**
- [[boolean]]

### is_cursor_empty
Returns whether the player is holding something in the cursor. Takes into account items from the blueprint library, as well as items and ghost cursor.

**Returns:**
- [[boolean]]

### get_requester_point
Gets the requester logistic point for this entity if it has one.

**Returns:**
- [[LuaLogisticPoint]] *(optional)*

### set_driving
Sets if this character or player is driving. Returns if the player or character is still driving.

**Parameters:**
- **`driving`** — [[boolean]]: True for enter-vehicle, false for leave.
- **`force`** — [[boolean]] *(optional)*: If true, the player will be ejected and left at the position of the car if normal "leave" is not possible.

### can_place_entity
Checks if this character or player can build the given entity at the given location on the surface the character or player is on.

Takes a table with the following fields:
- **`name`** — [[EntityID]]: Name of the entity that would be built.
- **`position`** — [[MapPosition]]: Where the entity would be placed.
- **`direction`** — [[defines.direction]] *(optional)*: Direction the entity would be facing. Defaults to `north`.

**Returns:**
- [[boolean]]
