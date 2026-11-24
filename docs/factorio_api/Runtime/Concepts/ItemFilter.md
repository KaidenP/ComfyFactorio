---
title: ItemFilter
tags: [factorio-api, runtime, concept]
---
# ItemFilter

An item filter may be specified in two ways, either as a string which is an item prototype name or as a table.

If this is specified as a string that is an item prototype name, then quality is set to `"normal"` and the comparator is set to `"="`, so only normal quality items will match the filter.

## Type

table | [[string]]
