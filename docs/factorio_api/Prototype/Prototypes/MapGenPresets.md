---
title: MapGenPresets
tags: [factorio-api, prototype]
---
# MapGenPresets

> **Type name:** `map-gen-presets` · **Instance limit:** 1

The available map gen presets.

## Properties

### type
- **Type:** `"map-gen-presets"`

### name
- **Type:** [[string (type)]]
Name of the map gen presets. Base game uses "default".

## Custom properties
Presets are defined as uniquely named [[MapGenPreset (type)|MapGenPreset]] properties of the prototype. Zero or more named presets can be specified within the prototype.

## Example

```
{
  type = "map-gen-presets",
  name = "default",
  ["marathon"] =
  {
    order = "c",
    basic_settings =
    {
      property_expression_names = {},
    },
    advanced_settings =
    {
      difficulty_settings =
      {
        technology_price_multiplier = 4
      }
    }
  },
  ["island"] =
  {
    order = "h",
    basic_settings =
    {
      property_expression_names =
      {
        elevation = "elevation_island",
        moisture = "moisture_basic",
        aux = "aux_basic",
        cliffiness = "cliffiness_basic",
        cliff_elevation = "cliff_elevation_from_elevation",
        trees_forest_path_cutout = 1
      },
      cliff_settings =
      {
        cliff_smoothing = 1
      },
      autoplace_controls =
      {
        ["trees"] =
        {
          frequency = 1,
          size = 0.5
        }
      }
    }
  }
}
```
