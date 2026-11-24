---
title: DamageTypeFilters
tags: [factorio-api, prototype, type]
---
# DamageTypeFilters

*Note: `DamageTypeFilters (type)`.*

## Type

struct | [[DamageTypeID (type)]] | array<[[DamageTypeID (type)]]>

## Properties

### types
- **Type:** [[DamageTypeID (type)]] | array<[[DamageTypeID (type)]]>
The damage types to filter for.

### whitelist
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether this is a whitelist or a blacklist of damage types. Defaults to being a blacklist.

## Examples

```
damage_type_filters = "fire"
```

```
damage_type_filters = { "fire" } -- more damage types could be specified here
```

```
damage_type_filters =
{
  whitelist = false, -- optional
  types = "fire"
}
```

```
damage_type_filters =
{
  whitelist = false, -- optional
  types = { "fire" } -- more damage types could be specified here
}
```
