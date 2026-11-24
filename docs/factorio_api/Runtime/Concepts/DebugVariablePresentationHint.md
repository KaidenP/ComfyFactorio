---
title: DebugVariablePresentationHint
tags: [factorio-api, runtime, concept]
---
# DebugVariablePresentationHint

The supported subset of [DebugAdapter VariablePresentationHint](https://microsoft.github.io/debug-adapter-protocol/specification#Types_VariablePresentationHint)

## Fields

### kind
- **Type:** `"virtual"`
- **Optional**
The only supported kind is "virtual".

### attributes
- **Type:** array<`"readOnly"`>
- **Optional**
The only supported attribute is "readOnly".

### lazy
- **Type:** [[boolean]]
- **Optional**
