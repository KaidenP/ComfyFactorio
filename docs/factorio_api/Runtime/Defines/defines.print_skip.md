---
title: print_skip
tags: [factorio-api, define]
---
# print_skip

*Note: `defines.print_skip`.*

## Values

### never
Print will not be skipped.

### if_redundant
Print will be skipped if same text was recently printed (within last 60 ticks). Used by most game messages.

### if_visible
Print will be skipped if same text is still visible (printed within last 1152 ticks). Used by some notifications.
