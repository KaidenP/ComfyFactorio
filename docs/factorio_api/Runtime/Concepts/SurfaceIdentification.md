---
title: SurfaceIdentification
tags: [factorio-api, runtime, concept]
---
# SurfaceIdentification

A surface may be specified in one of three ways.

## Type

[[uint32]] — It will be the index of the surface. `nauvis` has index `1`, the first surface-created surface will have index `2` and so on. | [[string]] — It will be the surface name. E.g. `"nauvis"`. | [[LuaSurface]] — A reference to [LuaSurface](runtime:LuaSurface) may be passed directly.
