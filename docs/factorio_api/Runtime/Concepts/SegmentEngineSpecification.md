---
title: SegmentEngineSpecification
tags: [factorio-api, runtime, concept]
---
# SegmentEngineSpecification

A runtime representation of [[SegmentEngineSpecification (type)|SegmentEngineSpecification]].

## Fields

### segments
- **Type:** array<[[SegmentSpecification]]>
All segments (except for the head segment) that compose the body of the segmented unit.

### max_body_nodes
- **Type:** [[uint32]]
The maximum number of body nodes that a segmented unit instance can have.
