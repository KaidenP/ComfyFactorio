---
title: log
tags: [factorio-api, runtime, global-function]
---
# log

`log()` can print [[LocalisedString|LocalisedStrings]] to the Factorio [log file](https://wiki.factorio.com/Log_file). This, in combination with the serpent library, makes debugging in the data stage easier because it allows the inspection of entire prototype tables. For example, printing all properties of the sulfur item prototype can be done like so: `log(serpent.block(data.raw["item"]["sulfur"]))`

**Parameters:**
- **`string`** — [[LocalisedString]]
