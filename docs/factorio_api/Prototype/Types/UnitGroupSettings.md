---
title: UnitGroupSettings
tags: [factorio-api, prototype, type]
---
# UnitGroupSettings

## Properties

### min_group_gathering_time
- **Type:** [[uint32 (type)]]
Pollution triggered group waiting time is a random time between min and max gathering time

### max_group_gathering_time
- **Type:** [[uint32 (type)]]

### max_wait_time_for_late_members
- **Type:** [[uint32 (type)]]
After the gathering is finished the group can still wait for late members, but it doesn't accept new ones anymore.

### max_group_radius
- **Type:** [[double (type)]]
Limits for group radius (calculated by number of numbers).

### min_group_radius
- **Type:** [[double (type)]]

### max_member_speedup_when_behind
- **Type:** [[double (type)]]
When a member falls behind the group he can speedup up till this much of his regular speed.

### max_member_slowdown_when_ahead
- **Type:** [[double (type)]]
When a member gets ahead of its group, it will slow down to at most this factor of its speed.

### max_group_slowdown_factor
- **Type:** [[double (type)]]
When members of a group are behind, the entire group will slow down to at most this factor of its max speed.

### max_group_member_fallback_factor
- **Type:** [[double (type)]]
If a member falls behind more than this times the group radius, the group will slow down to max_group_slowdown_factor.

### member_disown_distance
- **Type:** [[double (type)]]
If a member falls behind more than this time the group radius, it will be removed from the group.

### tick_tolerance_when_member_arrives
- **Type:** [[uint32 (type)]]

### max_gathering_unit_groups
- **Type:** [[uint32 (type)]]
Maximum number of automatically created unit groups gathering for attack at any time.

### max_unit_group_size
- **Type:** [[uint32 (type)]]
Maximum size of an attack unit group. This only affects automatically-created unit groups; manual groups created through the API are unaffected.
