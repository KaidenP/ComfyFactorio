---
title: DebugVariable
tags: [factorio-api, runtime, concept]
---
# DebugVariable

The supported subset of [DebugAdapter Variable](https://microsoft.github.io/debug-adapter-protocol/specification#Types_Variable)

## Fields

### name
- **Type:** [[string]]

### value
- **Type:** [[string]]

### type
- **Type:** [[string]]
- **Optional**

### variablesReference
- **Type:** [[int32]]
- **Optional**

### namedVariables
- **Type:** [[int32]]
- **Optional**

### indexedVariables
- **Type:** [[int32]]
- **Optional**

### presentationHint
- **Type:** [[DebugVariablePresentationHint]]
- **Optional**
