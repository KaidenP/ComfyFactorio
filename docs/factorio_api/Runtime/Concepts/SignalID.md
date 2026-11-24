---
title: SignalID
tags: [factorio-api, runtime, concept]
---
# SignalID

## Fields

### type
- **Type:** [[SignalIDType]]
- **Optional**
The type of the signal. If the type is `"item"`, this will be `nil` when reading.

### name
- **Type:** [[string]]
- **Optional**
Name of the prototype.

### quality
- **Type:** [[QualityID]]
- **Optional**
The prototype name of the signal's quality. Defaults to `normal`.
