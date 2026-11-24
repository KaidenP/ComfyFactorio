---
title: LuaRenderObject
tags: [factorio-api, runtime, class]
---
# LuaRenderObject

Reference to a single [[LuaRendering]] object.

## Attributes

### id
- **Type:** [[uint64]]
Unique identifier of this render object.

### type
- **Type:** `"text"` | `"line"` | `"circle"` | `"rectangle"` | `"arc"` | `"polygon"` | `"sprite"` | `"light"` | `"animation"`
Type of this object.

### surface
- **Type:** [[LuaSurface]]
Surface this object is rendered on.

### time_to_live
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
Time to live of this object. This will be 0 if the object does not expire.

### blink_interval
- **Type:** [[uint16]]
- **Writable:** [[uint16]]
Blink interval of this object based on the internal "update tick". When zero, blinking is disabled. For other values, the object will be visible the given number of ticks and then invisible for the same duration. Objects with the same blink interval will blink synchronously. Blink interval of game alerts is 30.

For example, when the interval is 60, the object is visible for 60 ticks and hidden for the next 60.

### forces
- **Type:** array<[[LuaForce]]>
- **Writable:** [[ForceSet]]
- **Optional**
Forces for which this object is rendered or `nil` if visible to all forces. Writing `nil` or empty array will make this object visible to all forces.

### players
- **Type:** array<[[LuaPlayer]]> | array<[[PlayerIdentification]]>
- **Writable:** array<[[LuaPlayer]]> | array<[[PlayerIdentification]]>
- **Optional**
Players for which this object is visible or `nil` if visible to all players. Writing `nil` or empty array will make this object visible to all players.

### visible
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this object is rendered to anyone at all.

### draw_on_ground
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this object is being drawn on the ground, under most entities and sprites.

In [[LuaRenderObject#render_mode|render_mode]] == "chart", this value is unused.

### only_in_alt_mode
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this object is only rendered in alt-mode.

### render_mode
- **Type:** [[ScriptRenderMode]]
- **Writable:** [[ScriptRenderMode]]
Whether the object is rendered in game world or on the chart (map view).

When it is changed, the object is pushed to front of its new group.

### use_target_orientation
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this object uses the target orientation.

### tall
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this render object will be translucent when "Hide tall entities" mode is active.

### color
- **Type:** [[Color]]
- **Writable:** [[Color]]
Color or tint of the object.

### width
- **Type:** [[float]]
- **Writable:** [[float]]
Width of the object. Value is in pixels (32 per tile).

### from
- **Type:** [[ScriptRenderTarget]]
- **Writable:** [[ScriptRenderTarget]]
Where this line is drawn from.

### to
- **Type:** [[ScriptRenderTarget]]
- **Writable:** [[ScriptRenderTarget]]
Where this line is drawn to.

### dash_length
- **Type:** [[double]]
- **Writable:** [[double]]
Dash length of this line.

### gap_length
- **Type:** [[double]]
- **Writable:** [[double]]
Length of the gaps in this line.

### dash_offset
- **Type:** [[double]]
- **Writable:** [[double]]
Starting offset to apply to dashes of this line. Cannot be greater than dash_length + gap_length.

### target
- **Type:** [[ScriptRenderTarget]]
- **Writable:** [[ScriptRenderTarget]]
Where this object is drawn.

Polygon vertices that are set to an entity will ignore this.

### orientation
- **Type:** [[RealOrientation]]
- **Writable:** [[RealOrientation]]
Orientation of this object.

Polygon vertices that are set to an entity will ignore this.

### scale
- **Type:** [[double]]
- **Writable:** [[double]]
Scale of the text or light.

### text
- **Type:** [[LocalisedString]]
- **Writable:** [[LocalisedString]]
Text that is displayed by this text object.

### font
- **Type:** [[string]]
- **Writable:** [[string]]
Font of this text.

### alignment
- **Type:** [[TextAlign]]
- **Writable:** [[TextAlign]]
Alignment of this text.

### vertical_alignment
- **Type:** [[VerticalTextAlign]]
- **Writable:** [[VerticalTextAlign]]
Vertical alignment of this text.

### scale_with_zoom
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this text scales with player zoom.

### use_rich_text
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this text parses rich text tags.

### filled
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this circle or rectangle is filled.

### radius
- **Type:** [[double]]
- **Writable:** [[double]]
Radius of this circle.

### left_top
- **Type:** [[ScriptRenderTarget]]
- **Writable:** [[ScriptRenderTarget]]
Where top left corner of this rectangle is drawn.

### right_bottom
- **Type:** [[ScriptRenderTarget]]
- **Writable:** [[ScriptRenderTarget]]
Where bottom right corner of this rectangle is drawn.

### max_radius
- **Type:** [[double]]
- **Writable:** [[double]]
Radius of the outer edge of this arc.

### min_radius
- **Type:** [[double]]
- **Writable:** [[double]]
Radius of the inner edge of this arc.

### start_angle
- **Type:** [[float]]
- **Writable:** [[float]]
Where this arc starts. Angle in radian.

### angle
- **Type:** [[float]]
- **Writable:** [[float]]
Angle of this arc. Angle in radian.

### vertices
- **Type:** array<[[ScriptRenderTarget]]>
- **Writable:** array<[[ScriptRenderTarget]]>
Vertices of this polygon.

### sprite
- **Type:** [[SpritePath]]
- **Writable:** [[SpritePath]]
Sprite of the sprite or light.

### x_scale
- **Type:** [[double]]
- **Writable:** [[double]]
- **Optional**
Horizontal scale of this sprite or animation. Write operation requires a valid number and clears `sprite_width`.

### y_scale
- **Type:** [[double]]
- **Writable:** [[double]]
- **Optional**
Vertical scale of this sprite or animation. Write operation requires a valid number and clears `sprite_height`.

### sprite_width
- **Type:** [[double]]
- **Writable:** [[double]]
- **Optional**
Width of this sprite or animation in tiles. If set, the sprite or animation is stretched to this width regardless of its original size. `nil` if `x_scale` is set. Writing requires a number greater than 0 and clears `x_scale`.

### sprite_height
- **Type:** [[double]]
- **Writable:** [[double]]
- **Optional**
Height of this sprite or animation in tiles. If set, the sprite or animation is stretched to this height regardless of its original size. `nil` if `y_scale` is set. Writing requires a number greater than 0 and clears `y_scale`.

### render_layer
- **Type:** [[RenderLayer]]
- **Writable:** [[RenderLayer]]
Render layer of this sprite or animation.

### orientation_target
- **Type:** [[ScriptRenderTarget]]
- **Writable:** [[ScriptRenderTarget]]
- **Optional**
Target to which this object rotates so that it faces the target. Note that `orientation` is still applied to the object. Writing `nil` will clear the orientation_target. `nil` if no target.

Polygon vertices that are set to an entity will ignore this.

### oriented_offset
- **Type:** [[Vector]]
- **Writable:** [[Vector]]
Offsets the center of the sprite or animation if `orientation_target` is given. This offset will rotate together with the sprite or animation.

### light_mode
- **Type:** [[ScriptSpriteLightMode]]
- **Writable:** [[ScriptSpriteLightMode]]
Whether this sprite or animation should be rendered as a sprite, light or both at once.

### intensity
- **Type:** [[float]]
- **Writable:** [[float]]
Intensity of this light.

### minimum_darkness
- **Type:** [[float]]
- **Writable:** [[float]]
Minimum darkness at which this light is rendered.

### oriented
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this light is rendered with the same orientation as the target entity. Note that `orientation` is still applied to the sprite.

### animation
- **Type:** [[string]]
- **Writable:** [[string]]
Animation prototype name of this animation.

### animation_speed
- **Type:** [[double]]
- **Writable:** [[double]]
Animation speed of this animation, in frames per tick. It is multiplied by [[AnimationPrototype#animation_speed|animation speed]] of the selected animation prototype. Changing speed will update `animation_offset`, so that the current `animation_frame` stays the same. Set it to 0 if you want to pause the animation.

### animation_offset
- **Type:** [[double]]
- **Writable:** [[double]]
Animation offset of this animation, in frames. Relative to game tick 0. This means the current animation frame is `((tick * speed) + animation_offset) % frame_count` with speed defined as [[LuaRenderObject#animation_speed|LuaRenderObject::animation_speed]] multiplied by [[AnimationPrototype#animation_speed|AnimationPrototype::animation_speed]].

### animation_frame
- **Type:** [[double]]
- **Writable:** [[double]]
Current frame of this animation. All writes update `animation_offset` to show the desired frame.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### destroy
Destroys this object. Does not error when the object is invalid.

### bring_to_front
Reorder this object so that it is drawn in front of the already existing objects.

### move_to_back
Reorder this object so that it is drawn in the back of the already existing objects.

### set_dashes
Set the length of the dashes and the length of the gaps in this line.
*Only available on:* `Line`

**Parameters:**
- **`dash_length`** — [[double]]
- **`gap_length`** — [[double]]

### set_corners
Set the corners of the rectangle with this id.
*Only available on:* `Rectangle`

**Parameters:**
- **`left_top`** — [[ScriptRenderTarget]]
- **`right_bottom`** — [[ScriptRenderTarget]]
