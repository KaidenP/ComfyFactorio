---
title: PrototypeFilter
tags: [factorio-api, runtime, concept]
---
# PrototypeFilter

Types `"signal"` and `"item-group"` do not support filters.

Filters are always used as an array of filters of a specific type. Every filter can only be used with its corresponding prototype type, and different types of prototype filters can not be mixed.

## Type

array<[[ModSettingPrototypeFilter]] | [[SpaceLocationPrototypeFilter]] | [[DecorativePrototypeFilter]] | [[TilePrototypeFilter]] | [[AsteroidChunkPrototypeFilter]] | [[ItemPrototypeFilter]] | [[TechnologyPrototypeFilter]] | [[RecipePrototypeFilter]] | [[AchievementPrototypeFilter]] | [[VirtualSignalPrototypeFilter]] | [[EquipmentPrototypeFilter]] | [[FluidPrototypeFilter]] | [[EntityPrototypeFilter]]>
