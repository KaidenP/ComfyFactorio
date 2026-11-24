---
title: RadiusVisualisationSpecification
tags: [factorio-api, prototype, type]
---
# RadiusVisualisationSpecification

*Note: `RadiusVisualisationSpecification (type)`.*

Sprite to be shown around the entity when it is selected/held in the cursor.

## Properties

### sprite
- **Type:** [[Sprite]]
- **Optional**
The sprite to show.

This sprite is silently overwritten by prototypes with a custom radius picture: [[AgriculturalTowerPrototype#radius_visualisation_picture|AgriculturalTowerPrototype::radius_visualisation_picture]], [[AsteroidCollectorPrototype#radius_visualisation_picture|AsteroidCollectorPrototype::radius_visualisation_picture]], [[BeaconPrototype#radius_visualisation_picture|BeaconPrototype::radius_visualisation_picture]], [[CargoLandingPadPrototype#radius_visualisation_picture|CargoLandingPadPrototype::radius_visualisation_picture]], [[ElectricPolePrototype#radius_visualisation_picture|ElectricPolePrototype::radius_visualisation_picture]], [[MiningDrillPrototype#radius_visualisation_picture|MiningDrillPrototype::radius_visualisation_picture]].

### distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
Must be greater than or equal to 0.

This distance is silently overwritten by prototypes with a custom distance: [[AgriculturalTowerPrototype#radius|AgriculturalTowerPrototype::radius]], [[AsteroidCollectorPrototype#collection_radius|AsteroidCollectorPrototype::collection_radius]], [[BeaconPrototype#supply_area_distance|BeaconPrototype::supply_area_distance]], [[ElectricPolePrototype#supply_area_distance|ElectricPolePrototype::supply_area_distance]], [[MiningDrillPrototype#resource_searching_radius|MiningDrillPrototype::resource_searching_radius]].

### offset
- **Type:** [[Vector (type)]]
- **Optional**
Offset of the sprite from the position of the entity. The offset is rotated by the entity's current direction.

This offset is silently overwritten by prototypes with a custom offset: [[MiningDrillPrototype#resource_searching_offset|MiningDrillPrototype::resource_searching_offset]].

### draw_in_cursor
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_on_selection
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### distance_quality_multiplier
- **Type:** dictionary<[[QualityID (type)]] → [[double (type)]]>
- **Optional**
Each value must be >= 0.01.

If value is not provided for a quality, then `1` will be used as a multiplier instead.

This does not affect the visualisation of prototypes with a custom distance specification because their distance automatically scales based on quality: agricultural tower (no quality scaling), [[QualityPrototype#asteroid_collector_collection_radius_bonus|asteroid collector]], [[QualityPrototype#beacon_supply_area_distance_bonus|beacon]], cargo landing pad (no quality scaling), [[QualityPrototype#electric_pole_supply_area_distance_bonus|electric pole]], and [[QualityPrototype#mining_drill_mining_radius_bonus|mining drill]].

## Examples

```
radius_visualisation_specification =
{
  sprite =
  {
    filename = "__base__/graphics/entity/electric-mining-drill/electric-mining-drill-radius-visualization.png",
    size = 10
  },
  distance = 5,
  offset = {0, -5}
}
```
