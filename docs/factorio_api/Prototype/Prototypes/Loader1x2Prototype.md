---
title: Loader1x2Prototype
tags: [factorio-api, prototype]
---
# Loader1x2Prototype

> **Parent:** [[LoaderPrototype]] · **Type name:** `loader`

Continuously loads and unloads machines, as an alternative to inserters.

This loader type is identical to [[Loader1x1Prototype]] with the exception of its hardcoded belt_distance. The belt_distance of the loader determines the distance between the position of this loader and the tile of the loader's belt target.

This loader type always has a belt_distance of 0.5, meaning by default it is 2 tiles long in total. For a loader type with a belt_distance of 0, see [[Loader1x1Prototype]].
