---
title: ProcessionLayer
tags: [factorio-api, prototype, type]
---
# ProcessionLayer

Describes one aspect of a procession. Animation and picture are interchangeable for types that require it.

Loaded as one of the procession layers, based on the value of the `type` key.

## Type

[[PodDistanceTraveledProcessionLayer]] — Loaded when the `type` is `"pod-distance-traveled"`. Add to distance traveled by the pod. Used by other visual layers. single layer of this type is allowed per ProcessionPrototype. | [[PodMovementProcessionLayer]] — Loaded when the `type` is `"pod-movement"`. Defines the timeline for the pod movement and rotation. A single layer of this type is allowed per ProcessionPrototype. | [[PodOpacityProcessionLayer]] — Loaded when the `type` is `"pod-opacity"`. Defines the outside and cutscene opacity of the pod and strength of surface lighting. A single layer of this type is allowed per ProcessionPrototype. | [[SingleGraphicProcessionLayer]] — Loaded when the `type` is `"single-graphic"`. Paints a sprite over the cargo pod. | [[CoverGraphicProcessionLayer]] — Loaded when the `type` is `"cover-graphic"`. Paints a tiling sprite over the entire screen. Optionally can mask nearby area or far area. | [[TintProcessionLayer]] — Loaded when the `type` is `"tint"`. Tints the whole surface with a color. | [[PodAnimationProcessionLayer]] — Loaded when the `type` is `"pod-animation"`. Defines an override graphic for the pod within the given range.

## Examples

```
{
  type = "pod-movement",
  frames =
  {
    { timestamp = 700 , tilt = 0.0               , tilt_t = 0 },
    { timestamp = 700 , offset = {0, 0 - 500}    , offset_t = {0, -40} },
    { timestamp = 900 , offset = {15, -60 - 500} , offset_t = {-10, -10} },
    { timestamp = 900 , opacity = 1.0 },
    { timestamp = 960 , tilt = 0.05              , tilt_t = -0.03 },
    { timestamp = 1050, tilt = 0.25              , tilt_t = 0 },
    { timestamp = 1050, offset = {40, -70 - 500} , offset_t = {-1, 0} },
    { timestamp = 1050, opacity = 0.0 },
    { timestamp = 700 , offset_rate = 0 },
    { timestamp = 1050, offset_rate = 1.0 }
  }
}
```
