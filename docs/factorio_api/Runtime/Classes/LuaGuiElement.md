---
title: LuaGuiElement
tags: [factorio-api, runtime, class]
---
# LuaGuiElement

An element of a custom GUI. This type is used to represent [[GuiElementType|any kind]] of a GUI element - labels, buttons and frames are all instances of this type. Just like [[LuaEntity]], different kinds of elements support different attributes; attempting to access an attribute on an element that doesn't support it (for instance, trying to access the `column_count` of a `textfield`) will result in a runtime error.

For information on all supported GUI elements, see [[GuiElementType]].

Each GUI element allows access to its children by having them as attributes. Thus, one can use the `parent.child` syntax to refer to children. Lua also supports the `parent["child"]` syntax to refer to the same element. This can be used in cases where the child has a name that isn't a valid Lua identifier.

## Attributes

### index
- **Type:** [[uint32]]
The index of this GUI element (unique amongst the GUI elements of a LuaPlayer).

### gui
- **Type:** [[LuaGui]]
The GUI this element is a child of.

### parent
- **Type:** [[LuaGuiElement]]
- **Optional**
The direct parent of this element. `nil` if this is a top-level element.

### name
- **Type:** [[string]]
- **Writable:** [[string]]
The name of this element. `""` if no name was set.
**Examples:**

```
game.player.gui.top.greeting.name == "greeting"
```

### caption
- **Type:** [[LocalisedString]]
- **Writable:** [[LocalisedString]]
The text displayed on this element. For frames, this is the "heading". For other elements, like buttons or labels, this is the content.

Whilst this attribute may be used on all elements without producing an error, it doesn't make sense for tables and flows as they won't display it.

### value
- **Type:** [[double]]
- **Writable:** [[double]]
How much this progress bar is filled. It is a value in the range `[0, 1]`.

### direction
- **Type:** [[GuiDirection]]
Direction of this element's layout.

### style
- **Type:** [[LuaStyle]] | [[string]]
- **Writable:** [[LuaStyle]] | [[string]]
The style of this element. When read, this evaluates to a [[LuaStyle]]. For writing, it only accepts a string that specifies the textual identifier (prototype name) of the desired style.

When writing, this clears all custom values set through [[LuaStyle]].

### visible
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Sets whether this GUI element is visible or completely hidden, taking no space in the layout.

### text
- **Type:** [[string]]
- **Writable:** [[string]]
The text contained in this textfield or text-box.

### children_names
- **Type:** array<[[string]]>
Names of all the children of this element. These are the identifiers that can be used to access the child as an attribute of this element.

### state
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Is this checkbox or radiobutton checked?

### player_index
- **Type:** [[uint32]]
Index into [[LuaGameScript#players|LuaGameScript::players]] specifying the player who owns this element.

### sprite
- **Type:** [[SpritePath]]
- **Writable:** [[SpritePath]]
The sprite to display on this sprite-button or sprite in the default state.

### resize_to_sprite
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether the sprite widget should resize according to the sprite in it. Defaults to `true`.

### hovered_sprite
- **Type:** [[SpritePath]]
- **Writable:** [[SpritePath]]
The sprite to display on this sprite-button when it is hovered.

### clicked_sprite
- **Type:** [[SpritePath]]
- **Writable:** [[SpritePath]]
The sprite to display on this sprite-button when it is clicked.

### tooltip
- **Type:** [[LocalisedString]]
- **Writable:** [[LocalisedString]]
The text to display when hovering over this element. Writing `""` or `nil` will disable the tooltip.

### elem_tooltip
- **Type:** [[ElemID]]
- **Writable:** [[ElemID]]
- **Optional**
The element tooltip to display when hovering over this element, or `nil`.

### horizontal_scroll_policy
- **Type:** [[ScrollPolicy]]
- **Writable:** [[ScrollPolicy]]
Policy of the horizontal scroll bar.

### vertical_scroll_policy
- **Type:** [[ScrollPolicy]]
- **Writable:** [[ScrollPolicy]]
Policy of the vertical scroll bar.

### type
- **Type:** [[GuiElementType]]
The type of this GUI element.

### children
- **Type:** array<[[LuaGuiElement]]>
The child-elements of this GUI element.

### items
- **Type:** array<[[LocalisedString]]>
- **Writable:** array<[[LocalisedString]]>
The items in this dropdown or listbox.

### selected_index
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The selected index for this dropdown or listbox. Returns `0` if none is selected.

### quality
- **Type:** [[LuaQualityPrototype]]
- **Writable:** [[QualityID]]
- **Optional**
The quality to be shown in the bottom left corner of this sprite-button, or `nil` to show nothing.

### number
- **Type:** [[double]]
- **Writable:** [[double]]
- **Optional**
The number to be shown in the bottom right corner of this sprite-button, or `nil` to show nothing.

### secondary_number
- **Type:** [[double]]
- **Writable:** [[double]]
- **Optional**
The number to be shown on the right side of this sprite-button, directly above the regular [[LuaGuiElement#number|LuaGuiElement::number]], or `nil` to show nothing.

### show_percent_for_small_numbers
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Related to the numbers to be shown in the bottom right corner of this sprite-button. When set to `true`, numbers that are non-zero and smaller than one are shown as a percentage rather than the value. For example, `0.5` will be shown as `50%` instead.

### opacity
- **Type:** [[float]]
- **Writable:** [[float]]
The opacity of the sprite shown in this widget, clamped to the range [0, 1].

Setting this to `0.5` makes the sprite look like a ghost item or an unfulfilled recipe ingredient.

### location
- **Type:** [[GuiLocation]]
- **Writable:** [[GuiLocation]]
- **Optional**
The location of this widget when stored in [[LuaGui#screen|LuaGui::screen]]. `nil` if not set or not in [[LuaGui#screen|LuaGui::screen]].

### auto_center
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this frame auto-centers on window resize when stored in [[LuaGui#screen|LuaGui::screen]].

### badge_text
- **Type:** [[LocalisedString]]
- **Writable:** [[LocalisedString]]
The text to display after the normal tab text (designed to work with numbers)

### auto_toggle
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this button will automatically toggle when clicked.

### toggled
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this button is currently toggled. When a button is toggled, it will use the `selected_graphical_set` and `selected_font_color` defined in its style.

### game_controller_interaction
- **Type:** [[defines.game_controller_interaction]]
- **Writable:** [[defines.game_controller_interaction]]
How this element should interact with game controllers.

### position
- **Type:** [[MapPosition]]
- **Writable:** [[MapPosition]]
The position this camera or minimap is focused on, if any.

### surface_index
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The surface index this camera or minimap is using.

### zoom
- **Type:** [[double]]
- **Writable:** [[double]]
The zoom this camera or minimap is using. This value must be positive.

### zoom_limits
- **Type:** [[ZoomLimits]]
- **Writable:** [[ZoomLimits]]
The zoom limits of this camera. By default the camera can zoom in to 3x, the same as most player controllers.

Reading this field creates a copy and only contains the limits previously set by a script. To change the zoom limits, set the entire field to the desired [[ZoomLimits]] table.
**Examples:**

```
-- Lets the camera zoom in to 10x the standard zoom level.
camera.zoom_limits = { closest = { zoom = 10 } }
camera.zoom = 10
```

### minimap_player_index
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The player index this minimap is using.

### force
- **Type:** [[string]]
- **Writable:** [[string]]
- **Optional**
The force this minimap is using, if any.

### elem_type
- **Type:** [[ElemType]]
The elem type of this choose-elem-button.

### elem_value
- **Type:** [[string]] | [[SignalID]] | [[PrototypeWithQuality]]
- **Writable:** [[string]] | [[SignalID]] | [[PrototypeWithQuality]]
- **Optional**
The elem value of this choose-elem-button, if any.

The `"signal"` type operates with [[SignalID]].

The `"with-quality"` types operate with [[PrototypeWithQuality]].

The remaining types use strings.

### elem_filters
- **Type:** [[PrototypeFilter]]
- **Writable:** [[PrototypeFilter]]
- **Optional**
The elem filters of this choose-elem-button, if any. The compatible type of filter is determined by `elem_type`.

Writing to this field does not change or clear the currently selected element.
**Examples:**

```
-- This will configure a choose-elem-button of type "entity" to only show items of type "furnace".
button.elem_filters = {{filter = "type", type = "furnace"}}
```

```
-- Then, there are some types of filters that work on a specific kind of attribute. The following will configure a
--   choose-elem-button of type "entity" to only show entities that have their `hidden` property set to `true`.
button.elem_filters = {{filter = "hidden"}}
```

```
-- Lastly, these filters can be combined at will, taking care to specify how they should be combined (either "and" or "or").
--   The following will filter for any entities that are "furnaces" and that are not "hidden".
button.elem_filters = {{filter = "type", type = "furnace"}, {filter = "hidden", invert = true, mode = "and"}}
```

### selectable
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether the contents of this text-box are selectable. Defaults to `true`.

### word_wrap
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this text-box will word-wrap automatically. Defaults to `false`.

### read_only
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this text-box is read-only. Defaults to `false`.

### enabled
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this GUI element is enabled. Disabled GUI elements don't trigger events when clicked.

### ignored_by_interaction
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this GUI element is ignored by interaction. This makes clicks on this element 'go through' to the GUI element or even the game surface below it.

### locked
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this choose-elem-button can be changed by the player.

### draw_vertical_lines
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this table should draw vertical grid lines.

### draw_horizontal_lines
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this table should draw horizontal grid lines.

### draw_horizontal_line_after_headers
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this table should draw a horizontal grid line below the first table row.

### column_count
- **Type:** [[uint32]]
The number of columns in this table.

### vertical_centering
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether the content of this table should be vertically centered. Overrides [[LuaStyle#column_alignments|LuaStyle::column_alignments]]. Defaults to `true`.

### slider_value
- **Type:** [[double]]
- **Writable:** [[double]]
The value of this slider element.

### mouse_button_filter
- **Type:** [[ActiveMouseButtonFlags]]
- **Writable:** [[MouseButtonFlags]]
The mouse button filters for this button or sprite-button.

### numeric
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this textfield is limited to only numeric characters.

### allow_decimal
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this textfield (when in numeric mode) allows decimal numbers.

### allow_negative
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this textfield (when in numeric mode) allows negative numbers.

### is_password
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this textfield displays as a password field, which renders all characters as `*`.

### lose_focus_on_confirm
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this textfield loses focus after [[defines.events#on_gui_confirmed|defines.events.on_gui_confirmed]] is fired.

### icon_selector
- **Type:** [[boolean]]
Whether this textfield or text-box was created with an icon selector.

### drag_target
- **Type:** [[LuaGuiElement]]
- **Writable:** [[LuaGuiElement]]
- **Optional**
The `frame` that is being moved when dragging this GUI element, if any. This element needs to be a child of the `drag_target` at some level.

Only top-level elements in [[LuaGui#screen|LuaGui::screen]] can be `drag_target`s.
**Examples:**

```
-- This creates a frame that contains a dragging handle which can move the frame.
local frame = player.gui.screen.add{type="frame", direction="vertical"}
local dragger = frame.add{type="empty-widget", style="draggable_space"}
dragger.style.size = {128, 24}
dragger.drag_target = frame
```

### selected_tab_index
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
- **Optional**
The selected tab index for this tabbed pane, if any.

### tabs
- **Type:** array<[[TabAndContent]]>
The tabs and contents being shown in this tabbed-pane.

### entity
- **Type:** [[LuaEntity]]
- **Writable:** [[LuaEntity]]
- **Optional**
The entity associated with this entity-preview, camera, minimap, if any.

### anchor
- **Type:** [[GuiAnchor]]
- **Writable:** [[GuiAnchor]]
- **Optional**
The anchor for this relative widget, if any. Setting `nil` clears the anchor.

### tags
- **Type:** [[Tags]]
- **Writable:** [[Tags]]
The tags associated with this LuaGuiElement.

### raise_hover_events
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this element will raise [[on_gui_hover]] and [[on_gui_leave]].

### inventory
- **Type:** [[LuaInventory]]
- **Writable:** [[LuaInventory]]
- **Optional**
The inventory target for this custom inventory widget.

### slots_per_row
- **Type:** [[uint8]]
- **Writable:** [[uint8]]
- **Optional**

### empty_slot_info
- **Type:** [[EmptySlotInfo]]
- **Writable:** [[EmptySlotInfo]]
- **Optional**

### handle_cursor_transfer
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### handle_cursor_split
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### handle_open_item
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### handle_open_mod_item
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### handle_send_stack_to_trash
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### handle_send_stacks_to_trash
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### switch_state
- **Type:** [[SwitchState]]
- **Writable:** [[SwitchState]]
The switch state for this switch.

If [[LuaGuiElement#allow_none_state|LuaGuiElement::allow_none_state]] is false this can't be set to `"none"`.

### allow_none_state
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether the `"none"` state is allowed for this switch.

This can't be set to false if the current switch_state is 'none'.

### left_label_caption
- **Type:** [[LocalisedString]]
- **Writable:** [[LocalisedString]]
The text shown for the left switch label.

### left_label_tooltip
- **Type:** [[LocalisedString]]
- **Writable:** [[LocalisedString]]
The tooltip shown on the left switch label.

### right_label_caption
- **Type:** [[LocalisedString]]
- **Writable:** [[LocalisedString]]
The text shown for the right switch label.

### right_label_tooltip
- **Type:** [[LocalisedString]]
- **Writable:** [[LocalisedString]]
The tooltip shown on the right switch label.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### add
Add a new child element to this GuiElement.

Takes a table with the following fields:
- **`type`** — [[GuiElementType]]: The kind of element to add, which potentially has its own attributes as listed below.
- **`name`** — [[string]] *(optional)*: Name of the child element. It must be unique within the parent element.
- **`caption`** — [[LocalisedString]] *(optional)*: Text displayed on the child element. For frames, this is their title. For other elements, like buttons or labels, this is the content. Whilst this attribute may be used on all elements, it doesn't make sense for tables and flows as they won't display it.
- **`tooltip`** — [[LocalisedString]] *(optional)*: Tooltip of the child element.
- **`elem_tooltip`** — [[ElemID]] *(optional)*: Elem tooltip of the child element. Will be displayed above `tooltip`.
- **`enabled`** — [[boolean]] *(optional)*: Whether the child element is enabled. Defaults to `true`.
- **`visible`** — [[boolean]] *(optional)*: Whether the child element is visible. Defaults to `true`.
- **`locked`** — [[boolean]] *(optional)*: Whether the child element is locked. Defaults to `false`.
- **`ignored_by_interaction`** — [[boolean]] *(optional)*: Whether the child element is ignored by interaction. Defaults to `false`.
- **`style`** — [[string]] *(optional)*: The name of the style prototype to apply to the new element.
- **`tags`** — [[Tags]] *(optional)*: [[Tags]] associated with the child element.
- **`index`** — [[uint32]] *(optional)*: Location in its parent that the child element should slot into. By default, the child will be appended onto the end.
- **`anchor`** — [[GuiAnchor]] *(optional)*: Where to position the child element when in the `relative` element.
- **`game_controller_interaction`** — [[defines.game_controller_interaction]] *(optional)*: How the element should interact with game controllers. Defaults to [[defines.game_controller_interaction#normal|defines.game_controller_interaction.normal]].
- **`raise_hover_events`** — [[boolean]] *(optional)*: Whether this element will raise [[on_gui_hover]] and [[on_gui_leave]]. Defaults to `false`.

Other attributes may be specified depending on `type`:

**Variant `button`:**
  - **`mouse_button_filter`** — [[MouseButtonFlags]] *(optional)*: Which mouse buttons the button responds to. Defaults to `"left-and-right"`.
  - **`auto_toggle`** — [[boolean]] *(optional)*: Whether the button will automatically toggle when clicked. Defaults to `false`.
  - **`toggled`** — [[boolean]] *(optional)*: The initial toggled state of the button. Defaults to `false`.

**Variant `camera`:**
  - **`position`** — [[MapPosition]]: The position the camera centers on.
  - **`surface_index`** — [[uint32]] *(optional)*: The surface that the camera will render. Defaults to the player's current surface.
  - **`zoom`** — [[double]] *(optional)*: The initial camera zoom. Defaults to `0.75`.

**Variant `checkbox`:**
  - **`state`** — [[boolean]]: The initial checked-state of the checkbox.

**Variant `choose-elem-button`:**
  - **`elem_type`** — [[ElemType]]: The type of the button.
  - **`item`** — [[string]] *(optional)*: If type is `"item"` - the default value for the button.
  - **`tile`** — [[string]] *(optional)*: If type is `"tile"` - the default value for the button.
  - **`entity`** — [[string]] *(optional)*: If type is `"entity"` - the default value for the button.
  - **`signal`** — [[SignalID]] *(optional)*: If type is `"signal"` - the default value for the button.
  - **`fluid`** — [[string]] *(optional)*: If type is `"fluid"` - the default value for the button.
  - **`recipe`** — [[string]] *(optional)*: If type is `"recipe"` - the default value for the button.
  - **`decorative`** — [[string]] *(optional)*: If type is `"decorative"` - the default value for the button.
  - **`item-group`** — [[string]] *(optional)*: If type is `"item-group"` - the default value for the button.
  - **`achievement`** — [[string]] *(optional)*: If type is `"achievement"` - the default value for the button.
  - **`equipment`** — [[string]] *(optional)*: If type is `"equipment"` - the default value for the button.
  - **`technology`** — [[string]] *(optional)*: If type is `"technology"` - the default value for the button.
  - **`asteroid-chunk`** — [[string]] *(optional)*: If type is `"asteroid-chunk"` - the default value for the button.
  - **`space-location`** — [[string]] *(optional)*: If type is `"space-location"` - the default value for the button.
  - **`item-with-quality`** — [[PrototypeWithQuality]] *(optional)*: If type is `"item-with-quality"` - the default value for the button.
  - **`entity-with-quality`** — [[PrototypeWithQuality]] *(optional)*: If type is `"entity-with-quality"` - the default value for the button.
  - **`recipe-with-quality`** — [[PrototypeWithQuality]] *(optional)*: If type is `"recipe-with-quality"` - the default value for the button.
  - **`equipment-with-quality`** — [[PrototypeWithQuality]] *(optional)*: If type is `"equipment-with-quality"` - the default value for the button.
  - **`elem_filters`** — [[PrototypeFilter]] *(optional)*: Filters describing what to show in the selection window. The applicable filter depends on the `elem_type`.

**Variant `drop-down`:**
  - **`items`** — array<[[LocalisedString]]> *(optional)*: The initial items in the dropdown.
  - **`selected_index`** — [[uint32]] *(optional)*: The index of the initially selected item. Defaults to 0.

**Variant `flow`:**
  - **`direction`** — [[GuiDirection]] *(optional)*: The initial direction of the flow's layout. Defaults to `"horizontal"`.

**Variant `frame`:**
  - **`direction`** — [[GuiDirection]] *(optional)*: The initial direction of the frame's layout. Defaults to `"horizontal"`.

**Variant `inventory`:**
  - **`slots_per_row`** — [[uint8]] *(optional)*
  - **`empty_slot_info`** — [[EmptySlotInfo]] *(optional)*
  - **`handle_cursor_transfer`** — [[boolean]] *(optional)*
  - **`handle_cursor_split`** — [[boolean]] *(optional)*
  - **`handle_open_item`** — [[boolean]] *(optional)*
  - **`handle_open_mod_item`** — [[boolean]] *(optional)*
  - **`handle_send_stack_to_trash`** — [[boolean]] *(optional)*
  - **`handle_send_stacks_to_trash`** — [[boolean]] *(optional)*

**Variant `line`:**
  - **`direction`** — [[GuiDirection]] *(optional)*: The initial direction of the line. Defaults to `"horizontal"`.

**Variant `list-box`:**
  - **`items`** — array<[[LocalisedString]]> *(optional)*: The initial items in the listbox.
  - **`selected_index`** — [[uint32]] *(optional)*: The index of the initially selected item. Defaults to 0.

**Variant `minimap`:**
  - **`position`** — [[MapPosition]] *(optional)*: The position the minimap centers on. Defaults to the player's current position.
  - **`surface_index`** — [[uint32]] *(optional)*: The surface the camera will render. Defaults to the player's current surface.
  - **`chart_player_index`** — [[uint32]] *(optional)*: The player index the map should use. Defaults to the current player.
  - **`force`** — [[string]] *(optional)*: The force this minimap should use. Defaults to the player's current force.
  - **`zoom`** — [[double]] *(optional)*: The initial camera zoom. Defaults to `0.75`.

**Variant `progressbar`:**
  - **`value`** — [[double]] *(optional)*: The initial value of the progressbar, in the range `[0, 1]`. Defaults to `0`.

**Variant `radiobutton`:**
  - **`state`** — [[boolean]]: The initial checked-state of the radiobutton.

**Variant `scroll-pane`:**
  - **`horizontal_scroll_policy`** — [[ScrollPolicy]] *(optional)*: Policy of the horizontal scroll bar. Defaults to `"auto"`.
  - **`vertical_scroll_policy`** — [[ScrollPolicy]] *(optional)*: Policy of the vertical scroll bar. Defaults to `"auto"`.

**Variant `slider`:**
  - **`minimum_value`** — [[double]] *(optional)*: The minimum value for the slider. Defaults to `0`.
  - **`maximum_value`** — [[double]] *(optional)*: The maximum value for the slider. Defaults to `30`.
  - **`value`** — [[double]] *(optional)*: The initial value for the slider. Defaults to `minimum_value`.
  - **`value_step`** — [[double]] *(optional)*: The minimum value the slider can move. Defaults to `1`.
  - **`discrete_values`** — [[boolean]] *(optional)*: Defaults to `true`.

**Variant `sprite`:**
  - **`sprite`** — [[SpritePath]] *(optional)*: Path to the image to display.
  - **`resize_to_sprite`** — [[boolean]] *(optional)*: Whether the widget should resize according to the sprite in it. Defaults to `true`.
  - **`opacity`** — [[float]] *(optional)*: Opacity of the sprite, clamped to the range [0, 1]. Defaults to `1`.

**Variant `sprite-button`:**
  - **`sprite`** — [[SpritePath]] *(optional)*: Path to the image to display on the button.
  - **`hovered_sprite`** — [[SpritePath]] *(optional)*: Path to the image to display on the button when it is hovered.
  - **`clicked_sprite`** — [[SpritePath]] *(optional)*: Path to the image to display on the button when it is clicked.
  - **`quality`** — [[string]] *(optional)*: The name of the quality shown on the button.
  - **`number`** — [[double]] *(optional)*: The number shown on the button.
  - **`secondary_number`** — [[double]] *(optional)*: The secondary number shown on the button, above the regular number.
  - **`show_percent_for_small_numbers`** — [[boolean]] *(optional)*: Formats small numbers as percentages. Defaults to `false`.
  - **`opacity`** — [[float]] *(optional)*: Opacity of the sprite shown on the button, clamped to the range [0, 1]. Defaults to `1`.
  - **`mouse_button_filter`** — [[MouseButtonFlags]] *(optional)*: The mouse buttons that the button responds to. Defaults to `"left-and-right"`.
  - **`auto_toggle`** — [[boolean]] *(optional)*: Whether the button will automatically toggle when clicked. Defaults to `false`.
  - **`toggled`** — [[boolean]] *(optional)*: The initial toggled state of the button. Defaults to `false`.

**Variant `switch`:**
  - **`switch_state`** — [[SwitchState]] *(optional)*: If set to "none", `allow_none_state` must be `true`. Defaults to `"left"`.
  - **`allow_none_state`** — [[boolean]] *(optional)*: Whether the switch can be set to a middle state. Defaults to `false`.
  - **`left_label_caption`** — [[LocalisedString]] *(optional)*
  - **`left_label_tooltip`** — [[LocalisedString]] *(optional)*
  - **`right_label_caption`** — [[LocalisedString]] *(optional)*
  - **`right_label_tooltip`** — [[LocalisedString]] *(optional)*

**Variant `tab`:**
  - **`badge_text`** — [[LocalisedString]] *(optional)*: The text to display after the normal tab text (designed to work with numbers).

**Variant `table`:**
  - **`column_count`** — [[uint32]]: Number of columns. This can't be changed after the table is created.
  - **`draw_vertical_lines`** — [[boolean]] *(optional)*: Whether the table should draw vertical grid lines. Defaults to `false`.
  - **`draw_horizontal_lines`** — [[boolean]] *(optional)*: Whether the table should draw horizontal grid lines. Defaults to `false`.
  - **`draw_horizontal_line_after_headers`** — [[boolean]] *(optional)*: Whether the table should draw a single horizontal grid line after the headers. Defaults to `false`.
  - **`vertical_centering`** — [[boolean]] *(optional)*: Whether the content of the table should be vertically centered. Defaults to `true`.

**Variant `text-box`:**
  - **`text`** — [[string]] *(optional)*: The initial text contained in the text-box.
  - **`icon_selector`** — [[boolean]] *(optional)*: Whether to add the rich text icon selector to the text box. This attribute can't be changed after creating the widget. Defaults to `false`.

**Variant `textfield`:**
  - **`text`** — [[string]] *(optional)*: The initial text contained in the textfield.
  - **`numeric`** — [[boolean]] *(optional)*: Defaults to `false`.
  - **`allow_decimal`** — [[boolean]] *(optional)*: Defaults to `false`.
  - **`allow_negative`** — [[boolean]] *(optional)*: Defaults to `false`.
  - **`is_password`** — [[boolean]] *(optional)*: Defaults to `false`.
  - **`lose_focus_on_confirm`** — [[boolean]] *(optional)*: Defaults to `false`.
  - **`icon_selector`** — [[boolean]] *(optional)*: Whether to add the rich text icon selector to the text field. This attribute can't be changed after creating the widget. Defaults to `false`.

**Returns:**
- [[LuaGuiElement]]: The GUI element that was added.

### clear
Remove children of this element. Any [[LuaGuiElement]] objects referring to the destroyed elements become invalid after this operation.

**Examples:**

```
game.player.gui.top.clear()
```

### destroy
Remove this element, along with its children. Any [[LuaGuiElement]] objects referring to the destroyed elements become invalid after this operation.

The top-level GUI elements - [[LuaGui#top|LuaGui::top]], [[LuaGui#left|LuaGui::left]], [[LuaGui#center|LuaGui::center]] and [[LuaGui#screen|LuaGui::screen]] - can't be destroyed.

**Examples:**

```
game.player.gui.top.greeting.destroy()
```

### get_mod
The mod that owns this GUI element or `nil` if it's owned by the scenario script.

This has a not-super-expensive, but non-free cost to get.

**Returns:**
- [[string]] *(optional)*

### get_index_in_parent
Gets the index that this element has in its parent element.

This iterates through the children of the parent of this element, meaning this has a non-free cost to get, but is faster than doing the equivalent in Lua.

**Returns:**
- [[uint32]]

### swap_children
Swaps the children at the given indices in this element.

**Parameters:**
- **`index_1`** — [[uint32]]: The index of the first child.
- **`index_2`** — [[uint32]]: The index of the second child.

### clear_items
Removes the items in this dropdown or listbox.
*Only available on:* `drop-down`, `list-box`

### get_item
Gets the item at the given index from this dropdown or listbox.
*Only available on:* `drop-down`, `list-box`

**Parameters:**
- **`index`** — [[uint32]]: The index to get

**Returns:**
- [[LocalisedString]]

### set_item
Sets the given string at the given index in this dropdown or listbox.
*Only available on:* `drop-down`, `list-box`

**Parameters:**
- **`index`** — [[uint32]]: The index whose text to replace.
- **`string`** — [[LocalisedString]]: The text to set at the given index.

### add_item
Inserts a string at the end or at the given index of this dropdown or listbox.
*Only available on:* `drop-down`, `list-box`

**Parameters:**
- **`string`** — [[LocalisedString]]: The text to insert.
- **`index`** — [[uint32]] *(optional)*: The index at which to insert the item.

### remove_item
Removes the item at the given index from this dropdown or listbox.
*Only available on:* `drop-down`, `list-box`

**Parameters:**
- **`index`** — [[uint32]]: The index

### get_slider_minimum
Gets this sliders minimum value.

**Returns:**
- [[double]]

### get_slider_maximum
Gets this sliders maximum value.

**Returns:**
- [[double]]

### set_slider_minimum_maximum
Sets this sliders minimum and maximum values. The minimum can't be >= the maximum.

**Parameters:**
- **`minimum`** — [[double]]
- **`maximum`** — [[double]]

### get_slider_value_step
Gets the minimum distance this slider can move.

**Returns:**
- [[double]]

### get_slider_discrete_values
Returns whether this slider only allows discrete values.

**Returns:**
- [[boolean]]

### set_slider_value_step
Sets the minimum distance this slider can move. The minimum distance can't be > (max - min).

**Parameters:**
- **`value`** — [[double]]

### set_slider_discrete_values
Sets whether this slider only allows discrete values.

**Parameters:**
- **`value`** — [[boolean]]

### focus
Focuses this GUI element if possible.

### scroll_to_top
Scrolls this scroll bar to the top.
*Only available on:* `scroll-pane`, `text-box`

### scroll_to_bottom
Scrolls this scroll bar to the bottom.
*Only available on:* `scroll-pane`, `text-box`

### scroll_to_left
Scrolls this scroll bar to the left.
*Only available on:* `scroll-pane`, `text-box`

### scroll_to_right
Scrolls this scroll bar to the right.
*Only available on:* `scroll-pane`, `text-box`

### scroll_to_element
Scrolls this scroll bar such that the specified GUI element is visible to the player.
*Only available on:* `scroll-pane`

**Parameters:**
- **`element`** — [[LuaGuiElement]]: The element to scroll to.
- **`scroll_mode`** — `"in-view"` | `"top-third"` *(optional)*: Where the element should be positioned in the scroll-pane. Defaults to `"in-view"`.

### select_all
Selects all the text in this textbox.
*Only available on:* `textfield`, `text-box`

### select
Selects a range of text in this textbox.
*Only available on:* `textfield`, `text-box`

**Parameters:**
- **`start_index`** — [[int32]]: The index of the first character to select
- **`end_index`** — [[int32]]: The index of the last character to select

**Examples:**

```
-- Select the characters "amp" from "example":
textbox.select(3, 5)
```

```
-- Move the cursor to the start of the text box:
textbox.select(1, 0)
```

### add_tab
Adds the given tab and content widgets to this tabbed pane as a new tab.
*Only available on:* `tabbed-pane`

**Parameters:**
- **`tab`** — [[LuaGuiElement]]: The tab to add, must be a GUI element of type "tab".
- **`content`** — [[LuaGuiElement]]: The content to show when this tab is selected. Can be any type of GUI element.

### remove_tab
Removes the given tab and its associated content from this tabbed pane.

Removing a tab does not destroy the tab or the tab contents. It just removes them from the view.
*Only available on:* `tabbed-pane`

**Parameters:**
- **`tab`** — [[LuaGuiElement]] *(optional)*: The tab to remove or `nil` to remove all tabs.

### force_auto_center
Forces this frame to re-auto-center. Only works on frames stored directly in [[LuaGui#screen|LuaGui::screen]].
*Only available on:* `frame`

**Raises:**
- [[on_gui_location_changed]] *(timeframe: future_tick)*

### scroll_to_item
Scrolls the scroll bar such that the specified listbox item is visible to the player.
*Only available on:* `list-box`

**Parameters:**
- **`index`** — [[int32]]: The item index to scroll to.
- **`scroll_mode`** — `"in-view"` | `"top-third"` *(optional)*: Where the item should be positioned in the list-box. Defaults to `"in-view"`.

### bring_to_front
Moves this GUI element to the "front" so it will draw over other elements.

Only works for elements in [[LuaGui#screen|LuaGui::screen]].

### close_dropdown
Closes the dropdown list if this is a dropdown and it is open.

## Operators

### index
The indexing operator. Gets children by name.

## Examples

```
-- This will add a label called "greeting" to the top flow.
-- Immediately after, it will change its text to illustrate accessing child elements.
game.player.gui.top.add{type="label", name="greeting", caption="Hi"}
game.player.gui.top.greeting.caption = "Hello there!"
game.player.gui.top["greeting"].caption = "Actually, never mind, I don't like your face"
```

```
-- This will add a tabbed-pane and 2 tabs with contents.
local tabbed_pane = game.player.gui.top.add{type="tabbed-pane"}
local tab1 = tabbed_pane.add{type="tab", caption="Tab 1"}
local tab2 = tabbed_pane.add{type="tab", caption="Tab 2"}
local label1 = tabbed_pane.add{type="label", caption="Label 1"}
local label2 = tabbed_pane.add{type="label", caption="Label 2"}
tabbed_pane.add_tab(tab1, label1)
tabbed_pane.add_tab(tab2, label2)
```
