---
title: DamageTypeFilters
tags: [factorio-api, runtime, concept]
---
# DamageTypeFilters

## Fields

### whitelist
- **Type:** [[boolean]]
Whether this is a whitelist or a blacklist of damage types. `true` means whitelist.

### types
- **Type:** dictionary<[[string]] → `true`>
The damage types to filter for. The value in the dictionary is meaningless and exists just to allow for easy lookup.
