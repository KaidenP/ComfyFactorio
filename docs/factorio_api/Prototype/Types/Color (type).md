---
title: Color
tags: [factorio-api, prototype, type]
---
# Color

*Note: `Color (type)`.*

Table of red, green, blue, and alpha float values between 0 and 1. Alternatively, values can be from 0-255, they are interpreted as such if at least one value is `> 1`.

Color allows the short-hand notation of passing an array of exactly 3 or 4 numbers. The array items are r, g, b and optionally a, in that order.

The game usually expects colors to be in pre-multiplied form (color channels are pre-multiplied by alpha).

## Type

struct | ([[float (type)]], [[float (type)]], [[float (type)]]) | ([[float (type)]], [[float (type)]], [[float (type)]], [[float (type)]])

## Properties

### r
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
red value

### g
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
green value

### b
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
blue value

### a
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
alpha value (opacity)

## Examples

```
color = {r=1, g=0, b=0, a=1} -- red, full opacity
color = {r=1} -- the same red, omitting default values
color = {1, 0, 0, 1} -- also the same red
color = {0, 0, 1} -- blue
color = {r=0, g=0.5, b=0, a=0.5} -- half transparency green
color = {} -- full opacity black
```
