---
title: AnimationSheet
tags: [factorio-api, prototype, type]
---
# AnimationSheet

> **Parent:** [[AnimationParameters]]

## Properties

### variation_count
- **Type:** [[uint32 (type)]]

### line_length
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** Value of `variation_count`
- **Overrides parent**

### filename
- **Type:** [[FileName]]
- **Optional**
- **Overrides parent**
Only loaded, and mandatory if `filenames` is not defined.

The path to the animation file to use.

### filenames
- **Type:** array<[[FileName]]>
- **Optional**

### lines_per_file
- **Type:** [[uint32 (type)]]
- **Optional**
Mandatory if `filenames` is defined.
