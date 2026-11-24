---
title: train_state
tags: [factorio-api, define]
---
# train_state

*Note: `defines.train_state`.*

## Values

### on_the_path
Normal state -- following the path.

### no_schedule
Doesn't have anywhere to go.

### no_path
Has no path and is stopped.

### arrive_signal
Braking before a rail signal.

### wait_signal
Waiting at a signal.

### arrive_station
Braking before a station.

### manual_control_stop
Switched to manual control and has to stop.

### manual_control
Can move if user explicitly sits in and rides the train.

### wait_station
Waiting at a station.

### destination_full
Same as no_path but all candidate train stops are full
