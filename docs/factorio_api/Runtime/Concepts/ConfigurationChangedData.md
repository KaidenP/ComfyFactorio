---
title: ConfigurationChangedData
tags: [factorio-api, runtime, concept]
---
# ConfigurationChangedData

## Fields

### old_version
- **Type:** [[string]]
- **Optional**
Old version of the map. Present only when loading map version other than the current version.

### new_version
- **Type:** [[string]]
- **Optional**
New version of the map. Present only when loading map version other than the current version.

### mod_changes
- **Type:** dictionary<[[string]] → [[ModChangeData]]>
Dictionary of mod changes. It is indexed by mod name.

### mod_startup_settings_changed
- **Type:** [[boolean]]
`true` when mod startup settings have changed since the last time this save was loaded.

### migration_applied
- **Type:** [[boolean]]
`true` when mod prototype migrations have been applied since the last time this save was loaded.

### migrations
- **Type:** dictionary<[[IDType]] → dictionary<[[string]] → [[string]]>>
Dictionary of prototype changes due to [[migrations]]. The inner dictionary maps the old prototype name to the new prototype name. The new name will be an empty string if the prototype was removed. Entries are omitted if the old and new prototype name are the same.
