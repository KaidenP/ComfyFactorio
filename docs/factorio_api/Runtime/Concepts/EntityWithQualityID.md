---
title: EntityWithQualityID
tags: [factorio-api, runtime, concept]
---
# EntityWithQualityID

An entity prototype with optional quality specification. Can be specified in one of four ways.

## Type

[[LuaEntity]] — The entity. Both prototype and quality of the entity will be used. | [[LuaEntityPrototype]] — The entity prototype. Normal quality will be used. | [[string]] — The prototype name. Normal quality will be used. | [[EntityIDAndQualityIDPair]] — A table of entity prototype and quality.
