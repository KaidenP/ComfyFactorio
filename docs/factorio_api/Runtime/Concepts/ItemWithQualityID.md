---
title: ItemWithQualityID
tags: [factorio-api, runtime, concept]
---
# ItemWithQualityID

An item prototype with optional quality specification. Can be specified in one of four ways.

## Type

[[LuaItemStack]] — The item stack. Both prototype and quality of the item stack will be used. | [[LuaItemPrototype]] — The item prototype. Normal quality will be used. | [[string]] — The prototype name. Normal quality will be used. | [[ItemIDAndQualityIDPair]] — A table of item prototype and quality.
