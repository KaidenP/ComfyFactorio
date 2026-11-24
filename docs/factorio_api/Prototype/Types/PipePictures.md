---
title: PipePictures
tags: [factorio-api, prototype, type]
---
# PipePictures

## Properties

### straight_vertical_single
- **Type:** [[SpriteVariations]]
- **Optional**

### straight_vertical
- **Type:** [[SpriteVariations]]
- **Optional**

### straight_vertical_window
- **Type:** [[SpriteVariations]]
- **Optional**

### straight_horizontal
- **Type:** [[SpriteVariations]]
- **Optional**

### straight_horizontal_window
- **Type:** [[SpriteVariations]]
- **Optional**

### corner_up_right
- **Type:** [[SpriteVariations]]
- **Optional**

### corner_up_left
- **Type:** [[SpriteVariations]]
- **Optional**

### corner_down_right
- **Type:** [[SpriteVariations]]
- **Optional**

### corner_down_left
- **Type:** [[SpriteVariations]]
- **Optional**

### t_up
- **Type:** [[SpriteVariations]]
- **Optional**

### t_down
- **Type:** [[SpriteVariations]]
- **Optional**

### t_right
- **Type:** [[SpriteVariations]]
- **Optional**

### t_left
- **Type:** [[SpriteVariations]]
- **Optional**

### cross
- **Type:** [[SpriteVariations]]
- **Optional**

### ending_up
- **Type:** [[SpriteVariations]]
- **Optional**

### ending_down
- **Type:** [[SpriteVariations]]
- **Optional**

### ending_right
- **Type:** [[SpriteVariations]]
- **Optional**

### ending_left
- **Type:** [[SpriteVariations]]
- **Optional**

### straight_vertical_single_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### straight_vertical_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### straight_vertical_window_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### straight_horizontal_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### straight_horizontal_window_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### corner_up_right_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### corner_up_left_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### corner_down_right_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### corner_down_left_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### t_up_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### t_down_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### t_right_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### t_left_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### cross_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### ending_up_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### ending_down_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### ending_right_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### ending_left_frozen
- **Type:** [[SpriteVariations]]
- **Optional**

### straight_vertical_single_visualization
- **Type:** [[Sprite]]
- **Optional**

### straight_vertical_visualization
- **Type:** [[Sprite]]
- **Optional**

### straight_vertical_window_visualization
- **Type:** [[Sprite]]
- **Optional**

### straight_horizontal_visualization
- **Type:** [[Sprite]]
- **Optional**

### straight_horizontal_window_visualization
- **Type:** [[Sprite]]
- **Optional**

### corner_up_right_visualization
- **Type:** [[Sprite]]
- **Optional**

### corner_up_left_visualization
- **Type:** [[Sprite]]
- **Optional**

### corner_down_right_visualization
- **Type:** [[Sprite]]
- **Optional**

### corner_down_left_visualization
- **Type:** [[Sprite]]
- **Optional**

### t_up_visualization
- **Type:** [[Sprite]]
- **Optional**

### t_down_visualization
- **Type:** [[Sprite]]
- **Optional**

### t_right_visualization
- **Type:** [[Sprite]]
- **Optional**

### t_left_visualization
- **Type:** [[Sprite]]
- **Optional**

### cross_visualization
- **Type:** [[Sprite]]
- **Optional**

### ending_up_visualization
- **Type:** [[Sprite]]
- **Optional**

### ending_down_visualization
- **Type:** [[Sprite]]
- **Optional**

### ending_right_visualization
- **Type:** [[Sprite]]
- **Optional**

### ending_left_visualization
- **Type:** [[Sprite]]
- **Optional**

### straight_vertical_single_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### straight_vertical_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### straight_vertical_window_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### straight_horizontal_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### straight_horizontal_window_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### corner_up_right_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### corner_up_left_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### corner_down_right_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### corner_down_left_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### t_up_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### t_down_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### t_right_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### t_left_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### cross_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### ending_up_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### ending_down_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### ending_right_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### ending_left_disabled_visualization
- **Type:** [[Sprite]]
- **Optional**

### horizontal_window_background
- **Type:** [[Sprite]]
- **Optional**

### vertical_window_background
- **Type:** [[Sprite]]
- **Optional**

### fluid_background
- **Type:** [[Sprite]]
- **Optional**

### low_temperature_flow
- **Type:** [[Sprite]]
- **Optional**
Visualizes the flow of the fluid in the pipe. Drawn when `(fluid_temp - fluid_min_temp) / (fluid_max_temp - fluid_min_temp)` is less than or equal to `1/3` and the fluid's temperature is below [[FluidPrototype#gas_temperature|FluidPrototype::gas_temperature]].

### middle_temperature_flow
- **Type:** [[Sprite]]
- **Optional**
Visualizes the flow of the fluid in the pipe. Drawn when `(fluid_temp - fluid_min_temp) / (fluid_max_temp - fluid_min_temp)` is larger than `1/3` and less than or equal to `2/3` and the fluid's temperature is below [[FluidPrototype#gas_temperature|FluidPrototype::gas_temperature]].

### high_temperature_flow
- **Type:** [[Sprite]]
- **Optional**
Visualizes the flow of the fluid in the pipe. Drawn when `(fluid_temp - fluid_min_temp) / (fluid_max_temp - fluid_min_temp)` is larger than `2/3` and the fluid's temperature is below [[FluidPrototype#gas_temperature|FluidPrototype::gas_temperature]].

### gas_flow
- **Type:** [[Animation]]
- **Optional**
Visualizes the flow of the fluid in the pipe. Drawn when the fluid's temperature is above [[FluidPrototype#gas_temperature|FluidPrototype::gas_temperature]].
