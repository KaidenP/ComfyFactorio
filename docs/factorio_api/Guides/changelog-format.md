---
title: changelog-format
tags: [factorio-api, guide]
---
## Changelog Format

This is the format required to display mod changelogs in the in-game mod browsing GUI. The `changelog.txt` file needs to be located in the root of the mod folder (see [[mod-structure|Mod Structure]]).

The does *not* require this changelog format, as it will display the `changelog.txt` content as plain text.

Parsing errors are written to the , which is found in the .

It may be simpler to copy and modify the [example changelog](#example-changelog) than to start from scratch.

### Formatting rules

The changelog format consists of one or multiple version sections, which are read line by line. Each version section has to start with the [version section start](#version-section-start) line. Each version section describes exactly one mod version with an arbitrary amount of categories that each may have an arbitrary amount of entries.

Completely empty lines will be skipped by the parser, except the line after the [version section start](#version-section-start) line, which must not be empty.

Do not use tabs, and do not leave whitespace at the end of lines ("trailing spaces"). It is recommended to set up the text editor to enforce this automatically. Usage of tabs and trailing spaces is likely to result in confusing error messages.

#### Version section start

The line must be 99 dashes exactly:

`---------------------------------------------------------------------------------------------------`

The following line must be a [version](#version) line. It can not be empty.

#### Version

The line must start with exactly `Version: ` (note the space after the colon). The remaining part of the line will be parsed as the version the section is about.

The version itself is formatted as `number.number.number` (as in `major.minor.sub`), ie. `0.6.4`. Each number can range from `0` to `65535`. `0.0.0` is considered an invalid version.

This line is *mandatory*, and there may not be two version sections with the same version.

Example: `Version: 0.12.35`

#### Date

The line must start with exactly `Date: ` (note the space after the colon). The remaining part of the line will be parsed as the date the version was released. There are no restrictions for the format of the date itself.

This line is *optional*, and there may not be two date lines within the same version section.

Example: `Date: 01. 06. 2016`

#### Category

The line must start with exactly two spaces. The remaining part of the line will be parsed as the category. The line must end with a colon. When displaying the changelog, this colon is removed.

This line and the entry lines following it are *optional*. There are no restrictions for the format of the category itself.

However, some categories are recognized by the game and sorted in front of the "All" tab in the GUI:

- Major Features
- Features
- Minor Features
- Graphics
- Sounds
- Optimizations
- Balancing
- Combat Balancing
- Circuit Network
- Changes
- Bugfixes
- Modding
- Scripting
- Gui
- Control
- Translation
- Debug
- Ease of use
- Info
- Locale
- Compatibility

Example: `  Minor Features:`

#### Entry

The line must start with exactly four spaces followed by a dash followed by another space `    - ` for a single line entry. For a multiline entry, lines after the first line must start with exactly six spaces.

If an entry is used, a previous line in the version section must be a [category](#category) line. The entry is then associated with the category (see [example changelog](#example-changelog)).

Entries for the same version and the same category may not be exact duplicates. Note that individual lines in a multiline entry will be considered duplicates of other individual lines from other multiline entries in the same category if they are identical (see for context).

Example: `    - Fixed the missing title in character logistics window.`

### Example changelog

It may be simpler to copy and modify this example than to start from scratch.

``` standalone-code-block
---------------------------------------------------------------------------------------------------
Version: 1.1.60
Date: 06. 06. 2022
  Features:
    - This is an entry in the "Features" category.
    - This is another entry in the "Features" category.
    - This general section is the 1.1.60 version section.
  Balancing:
    - This is a multiline entry in the "Balancing" category.
      There is some extra text here because it is needed for the example.
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
  Bugfixes:
    - Fixed that canceling syncing mods with a save would exit the GUI.
    - Fixed a desync when fast-replacing burner generators.
---------------------------------------------------------------------------------------------------
Version: 1.1.59
Date: 06. 05. 2022
  Bugfixes:
    - This general section is the 1.1.59 version section.
    - This is an entry in the "Bugfixes" category.
    - Fixed grenade shadows.
---------------------------------------------------------------------------------------------------
Version: 0.1.0
Date: 24. 12. 2012
  Major Features:
    - Initial release.
    - This general section is the 0.1.0 version section.
```

