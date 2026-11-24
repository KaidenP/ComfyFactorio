---
title: FootprintParticle
tags: [factorio-api, prototype, type]
---
# FootprintParticle

## Properties

### tiles
- **Type:** array<[[TileID (type)]]>
The tiles this footprint particle is shown on when the player walks over them.

### particle_name
- **Type:** [[ParticleID (type)]]
- **Optional**
The name of the particle that should be created when the character walks on the defined tiles.

### use_as_default
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether this footprint particle should be the default particle that is used for `tiles` that don't have an associated footprint particle.
