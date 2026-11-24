---
title: rocket_silo_status
tags: [factorio-api, define]
---
# rocket_silo_status

*Note: `defines.rocket_silo_status`.*

The various parts of the launch sequence of the rocket silo.

## Values

### building_rocket
The rocket silo is crafting rocket parts. When there are enough rocket parts, the silo will switch into the `create_rocket` state.

### create_rocket
The next state is `lights_blinking_open`. The rocket silo rocket entity gets created.

### lights_blinking_open
The next state is `doors_opening`. The rocket is getting prepared for launch.

### doors_opening
The next state is `doors_opened`. The rocket is getting prepared for launch.

### doors_opened
The next state is `rocket_rising` or if the rocket is destroyed in this state then the next state will be `lights_blinking_close`. The rocket is getting prepared for launch.

### rocket_rising
The next state is `arms_advance` or if the rocket is destroyed in this state then the next state will be `lights_blinking_close`. The rocket is getting prepared for launch.

### arms_advance
The next state is `rocket_ready` or if the rocket is destroyed in this state then the next state will be `lights_blinking_close`. The rocket is getting prepared for launch.

### rocket_ready
The rocket launch can be started by the player. When the launch is started, the silo switches into the `launch_starting` state.

### launch_starting
The next state is `launch_started`.

### engine_starting
The next state is `arms_retract` or if the rocket is destroyed in this state then the next state will be `lights_blinking_close`. The rocket is getting launched.

### arms_retract
The next state is `rocket_flying` or if the rocket is destroyed in this state then the next state will be `lights_blinking_close`. The rocket is getting launched.

### rocket_flying
The next state is `lights_blinking_close`. The rocket is getting launched.

### lights_blinking_close
The next state is `doors_closing`.

### doors_closing
The next state is `building_rocket`.

### launch_started
The next state is `engine_starting` or if the rocket is destroyed in this state then the next state will be `lights_blinking_close`. The rocket is getting launched.
