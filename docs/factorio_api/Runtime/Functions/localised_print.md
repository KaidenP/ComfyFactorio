---
title: localised_print
tags: [factorio-api, runtime, global-function]
---
# localised_print

`localised_print()` allows printing [[LocalisedString]] to stdout without polluting the Factorio [log file](https://wiki.factorio.com/Log_file). This is primarily useful when communicating with external tools that launch Factorio as a child process.

**Parameters:**
- **`string`** — [[LocalisedString]]
