---
title: AutoplaceSettings
tags: [factorio-api, prototype, type]
---
# AutoplaceSettings

*Note: `AutoplaceSettings (type)`.*

## Properties

### treat_missing_as_default
- **Type:** [[boolean (type)]]
- **Optional**
Whether missing autoplace names for this type should be default enabled.

### settings
- **Type:** dictionary<[[EntityID (type)]] | [[TileID (type)]] | [[DecorativeID (type)]] → [[FrequencySizeRichness]]>
- **Optional**
Overrides the FrequencySizeRichness provided to the [[AutoplaceSpecification (type)|AutoplaceSpecification]] of the entity/tile/decorative. Takes priority over the FrequencySizeRichness set in the [[AutoplaceSpecification (type)#control|autoplace control]].
