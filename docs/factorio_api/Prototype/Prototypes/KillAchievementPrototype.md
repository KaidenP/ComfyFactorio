---
title: KillAchievementPrototype
tags: [factorio-api, prototype]
---
# KillAchievementPrototype

> **Parent:** [[AchievementPrototype]] · **Type name:** `kill-achievement`

This prototype is used for receiving an achievement when the player destroys a certain amount of an entity, with a specific damage type.

## Properties

### to_kill
- **Type:** [[EntityID (type)]] | array<[[EntityID (type)]]>
- **Optional**
This defines which entity needs to be destroyed in order to receive the achievement.

### type_to_kill
- **Type:** [[string (type)]]
- **Optional**
This defines what entity type needs to be destroyed in order to receive the achievement.
**Examples:**

```
type_to_kill = "inserter"
```

### damage_type
- **Type:** [[DamageTypeID (type)]]
- **Optional**
This defines how the player needs to destroy the specific entity.
**Examples:**

```
damage_type = "impact"
```

### damage_dealer
- **Type:** [[EntityID (type)]] | array<[[EntityID (type)]]>
- **Optional**
The killer of the entity must be one of these entities.
**Examples:**

```
damage_dealer = "artillery-turret"
```

```
damage_dealer = {"artillery-turret", "artillery-wagon"}
```

### amount
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`
This is the amount of entity of the specified type the player needs to destroy to receive the achievement.
**Examples:**

```
amount = 100
```

### in_vehicle
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
This defines if the player needs to be in a vehicle.
**Examples:**

```
in_vehicle = true
```

### personally
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
This defines to make sure you are the one driving, for instance, in a tank rather than an automated train.
**Examples:**

```
personally = true
```
