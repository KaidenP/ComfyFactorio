---
title: BeaconModuleVisualizations
tags: [factorio-api, prototype, type]
---
# BeaconModuleVisualizations

## Properties

### art_style
- **Type:** [[string (type)]]
The visualization is chosen based on the [[ModulePrototype#art_style|ModulePrototype::art_style]], meaning if module art style equals beacon module visualization art style then this visualization is chosen. Vanilla uses `"vanilla"` here.

### use_for_empty_slots
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### tier_offset
- **Type:** [[int32 (type)]]
- **Optional**
- **Default:** `0`

### slots
- **Type:** array<array<[[BeaconModuleVisualization]]>>
- **Optional**
The outer array contains the different slots, the inner array contains the different layers for those slots (with different tints etc). Example:
**Examples:**

```
slots =
{
  { --slot 1
    { --layer 1 of slot 1
      BeaconModuleVisualization data
    },
    { --layer 2 of slot 1
      BeaconModuleVisualization data
    }
  },
  { --slot 2
    { --layer 1 of slot 2
      BeaconModuleVisualization data
    },
    { --layer 2 of slot 2
      BeaconModuleVisualization data
    },
    { --layer 3 of slot 2
      BeaconModuleVisualization data
    }
  }
}
```
