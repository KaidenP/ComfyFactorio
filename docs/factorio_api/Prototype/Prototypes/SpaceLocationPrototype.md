---
title: SpaceLocationPrototype
tags: [factorio-api, prototype]
---
# SpaceLocationPrototype

> **Parent:** [[Prototype]] · **Type name:** `space-location`

A space location, such as a planet or the solar system edge.

## Properties

### gravity_pull
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
A value which modifies platform speed; is subtracted when traveling from this location and added when traveling to this location.

### origin
- **Type:** [[MapPosition (type)]]
- **Optional**
- **Default:** `{0, 0}`
The location that this space location orbits in the space map.

### distance
- **Type:** [[double (type)]]
Distance from the origin in map coordinates.

### orientation
- **Type:** [[RealOrientation (type)]]
Angle in relation to the origin.

### magnitude
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1.0`
The apparent size of the space location in map coordinates.

### parked_platforms_orientation
- **Type:** [[RealOrientation (type)]]
- **Optional**
- **Default:** same as orientation
The orientation where parked space platforms will be drawn.

### label_orientation
- **Type:** [[RealOrientation (type)]]
- **Optional**
- **Default:** `0.25`
The orientation where the location's name will be drawn.

### draw_orbit
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If `false`, the orbital ring around the origin will not be drawn for this location.

### solar_power_in_space
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1.0`

### asteroid_spawn_influence
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.1`
If greater than 0, `asteroid_spawn_definitions` will be used on space connections of this location, interpolated based on distance. The number specifies the percentage of the route where the location stops spawning its asteroids.

### fly_condition
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When set to true, it means that this connection offers fly condition rather than wait condition at the destination

### auto_save_on_first_trip
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### procession_graphic_catalogue
- **Type:** [[ProcessionGraphicCatalogue]]
- **Optional**

### procession_audio_catalogue
- **Type:** [[ProcessionAudioCatalogue]]
- **Optional**

### platform_procession_set
- **Type:** [[ProcessionSet (type)]]
- **Optional**
These transitions are used for any platform stopped at this location.

### planet_procession_set
- **Type:** [[ProcessionSet (type)]]
- **Optional**
These transitions are used for anything traveling from the surface associated with this location.

### icons
- **Type:** array<[[IconData]]>
- **Optional**
Can't be an empty array.

### icon
- **Type:** [[FileName]]
- **Optional**
Path to the icon file.

Only loaded, and mandatory if `icons` is not defined.

### icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

Only loaded if `icons` is not defined.

### starmap_icons
- **Type:** array<[[IconData]]>
- **Optional**
- **Requires:** `space_age`
Can't be an empty array.

### starmap_icon
- **Type:** [[FileName]]
- **Optional**
- **Requires:** `space_age`
Path to the icon file.

Only loaded if `starmap_icons` is not defined.

### starmap_icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
- **Requires:** `space_age`
The size of the starmap icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

Only loaded if `starmap_icons` is not defined.

### starmap_icon_orientation
- **Type:** [[RealOrientation (type)]]
- **Optional**
Orientation of the starmap icon, defaults to pointing towards the origin.

### asteroid_spawn_definitions
- **Type:** array<[[SpaceLocationAsteroidSpawnDefinition (type)]]>
- **Optional**

### hidden
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Overrides parent**
Hides the space location from the planet selection lists and the space map.

### platform_surface_render_parameters
- **Type:** [[SurfaceRenderParameters (type)]]
- **Optional**
Render parameters that influence platforms orbiting this space location.
