---
title: NoiseFunction
tags: [factorio-api, prototype, type]
---
# NoiseFunction

The advantage of noise functions over [[NoiseExpression|noise expressions]] is that they have parameters.

## Properties

### parameters
- **Type:** array<[[string (type)]]>
The order of the parameters matters because functions can also be called with positional arguments.

A function can't have more than 255 parameters.

### expression
- **Type:** [[NoiseExpression]]

### local_expressions
- **Type:** dictionary<[[string (type)]] → [[NoiseExpression]]>
- **Optional**
A map of expression name to expression.

Local expressions are meant to store data locally similar to local variables in Lua. Their purpose is to hold noise expressions used multiple times in the named noise expression, or just to tell the reader that the local expression has a specific purpose. Local expressions can access other local definitions and also function parameters, but recursive definitions aren't supported.

### local_functions
- **Type:** dictionary<[[string (type)]] → [[NoiseFunction]]>
- **Optional**
A map of function name to function.

Local functions serve the same purpose as local expressions - they aren't visible outside of the specific prototype and they have access to other local definitions.
