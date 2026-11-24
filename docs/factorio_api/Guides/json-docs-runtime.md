---
title: json-docs-runtime
tags: [factorio-api, guide]
---
## Runtime JSON Format

The runtime API documentation is available in a machine-readable [JSON format](../runtime-api.json). It allows for the creation of developer tools that provide code completion and related functionality. This page documents the structure of this format.

The current `api_version` that these docs reflect is `6`, which was introduced with Factorio `2.0.7`. See [Changelog](#Changelog).

### General notes

Some notes that apply to the format in general:

- If a member would be `null`, it is omitted from the JSON instead.
- Every list is sorted alphabetically by name. To replicate the order seen on the website, it can be sorted by the `order` property of its members.
- Text (descriptions, examples, etc.) is formatted as , which includes links, inline code, and code blocks. More on how links work right below.

### Link format

All text can contain Markdown-type links. There are two broad categories for these: hyperlinks that link to any external website, and internal links that refer to another part of this documentation. All of them will have a title that should be displayed as the link's text.

- External links work like standard Markdown links, meaning they always start with `https://`, and are followed by the URL. Example: `[Factorio](https://factorio.com)`.
- Internal links are a bit more complex. They aren't valid hyperlinks, but instead use a custom shorthand format to refer to specific parts of the API. This format has three main parts:
  - They always start with `runtime:`, `prototype:` or `auxiliary:`, indicating the stage that is linked to. The stages are separate namespaces, as there would be naming conflicts otherwise. So this first part indicates whether to look for the API member among classes and events, among prototypes and types, or among auxiliary pages.
  - The second part is the name of the API member being linked to. What this can be depends on the stage that's indicated beforehand. Examples would be `LuaGuiElement` or `on_player_created` for `runtime:`, `RecipePrototype` or `EnergySource` for `prototype:`, or `data-lifecycle` for `auxiliary:`.
    - Note that this can be the name of some stage-specific auxiliary pages instead. Namely, 'classes', 'events', 'concepts', for `runtime:`, and 'prototypes', 'types' for `prototype:`.
  - The third, optional part of an internal link can specify a certain sub-member to refer to. Its format is `::<name>`, where name is the name of a class method or attribute, or a prototype/type property. It is invalid for any other member type.

Examples:

- `[LuaGuiElement](runtime:LuaGuiElement)` links to the `LuaGuiElement` class.
- `[results](prototype:RecipePrototype::results)` links to the `results` property of the `RecipePrototype` prototype.
- `[Data Lifecycle](auxiliary:data-lifecycle)` links to the [[data-lifecycle|Data Lifecycle]] auxiliary docs page.

------------------------------------------------------------------------

### Top level members

The format has some top level members indicating the context of the format. These are:

- `application` :: [string](#string): The application this documentation is for. Will always be `"factorio"`.
- `application_version` :: [string](#string): The version of the game that this documentation is for. An example would be `"1.1.35"`.
- `api_version` :: [number](#number): The version of the machine-readable format itself. It is incremented every time the format changes. The version this documentation reflects is stated at the top.
- `stage` :: [string](#string): Indicates the stage this documentation is for. Will always be `"runtime"` (as opposed to `"prototype"`; see the [[data-lifecycle|Data Lifecycle]] for more detail).

Then, there are several top level members that contain the API documentation itself, organized by their various types. These are:

- `classes` :: array\[[Class](#Class)\]: The list of classes (LuaObjects) the API provides. Equivalent to the [[Classes|classes]] page.
- `events` :: array\[[Event](#Event)\]: The list of events that the API provides. Equivalent to the [[Events|events]] page.
- `concepts` :: array\[[Concept](#Concept)\]: The list of concepts of various types that the API uses. Equivalent to the [[Concepts|concepts]] page.
- `defines` :: array\[[Define](#Define)\]: The list of defines that the game uses. Equivalent to the [[Defines|defines]] page.
- `global_objects` :: array\[[Parameter](#Parameter)\]: The list of objects that the game provides as global variables to serve as entry points to the API. Uses the same format as parameters, but are never optional.
- `global_functions` :: array\[[Method](#Method)\]: The list of functions that the game provides as global variables to provide some specific functionality.

#### BasicMember

Several API members follow a common format for their basic fields. This is indicated by `inherits from BasicMember` in their title. It includes the following fields:

- `name` :: [string](#string): The name of the member.
- `order` :: [number](#number): The order of the member as shown in the HTML.
- `description` :: [string](#string): The text description of the member. Can be `''`, but never `null`.
- `lists` :: array\[[string](#string)\] (optional): A list of Markdown lists to provide additional information. Usually contained in a spoiler tag.
- `examples` :: array\[[string](#string)\] (optional): A list of code-only examples about the member.
- `images` :: array\[[Image](#Image)\] (optional): A list of illustrative images shown next to the member.

### Top level types

#### Class <span class="small">*inherits from BasicMember*</span>

- `visibility` :: array\[[string](#string)\] (optional): The list of game expansions needed to use this class. If not present, no restrictions apply. Possible values: `"space_age"`.
- `parent` :: [string](#string) (optional): The name of the class that this class inherits from.
- `abstract` :: [boolean](#boolean): Whether the class is never itself instantiated, only inherited from.
- `methods` :: array\[[Method](#Method)\]: The methods that are part of the class.
- `attributes` :: array\[[Attribute](#Attribute)\]: The attributes that are part of the class.
- `operators` :: array\[`Operator`\]: A list of operators on the class. They are called `call`, `index`, or `length` and have the format of either a [Method](#Method) or an [Attribute](#Attribute).

#### Event <span class="small">*inherits from BasicMember*</span>

- `data` :: array\[[Parameter](#Parameter)\]: The event-specific information that is provided.
- `filter`:: [string](#string) (optional): The name of the filter concept that applies to this event.

#### Concept <span class="small">*inherits from BasicMember*</span>

- `type` :: [Type](#Type): The type of the concept. Either a proper [Type](#Type), or the string `"builtin"`, indicating a fundamental type like `string` or `number`.

#### Define <span class="small">*inherits from BasicMember*</span>

Defines can be recursive in nature, meaning one Define can have multiple sub-Defines that have the same structure. These are singled out as `subkeys` instead of `values`.

- `values` :: array\[[DefineValue](#DefineValue)\] (optional): The members of the define.
- `subkeys` :: array\[[Define](#Define)\] (optional): A list of sub-defines.

### Common structures

Several data structures are used in different parts of the format, which is why they are documented separately to avoid repetition.

#### Type

A type field can be a [string](#string), in which case that string is the simple type. Otherwise, a type is a table:

- `complex_type` :: [string](#string): A string denoting the kind of complex type.

Depending on `complex_type`, there are additional members:

- `type`:
  - `value` :: [Type](#Type): The actual type. This format for types is used when they have descriptions attached to them.
  - `description` :: [string](#string): The text description of the type.
- `union`:
  - `options` :: array\[[Type](#Type)\]: A list of all compatible types for this type.
  - `full_format` :: [boolean](#boolean): Whether the options of this union have a description or not.
- `array`:
  - `value` :: [Type](#Type): The type of the elements of the array.
- `dictionary` or `LuaCustomTable`:
  - `key` :: [Type](#Type): The type of the keys of the dictionary or LuaCustomTable.
  - `value` :: [Type](#Type): The type of the values of the dictionary or LuaCustomTable.
- `table`:
  - `parameters` :: array\[[Parameter](#Parameter)\]: The parameters present in the table.
  - `variant_parameter_groups` :: array\[[ParameterGroup](#ParameterGroup)\] (optional): The optional parameters that depend on one of the main parameters.
  - `variant_parameter_description` :: [string](#string) (optional): The text description of the optional parameter groups.
- `tuple`:
  - `values` :: array\[[Type](#Type)\]: The types of the members of this tuple in order.
- `function`:
  - `parameters` :: array\[[Type](#Type)\]: The types of the function arguments.
- `literal`:
  - `value` :: union\[[string](#string), [number](#number), [boolean](#boolean)\]: The value of the literal.
  - `description` :: [string](#string) (optional): The text description of the literal, if any.
- `LuaLazyLoadedValue`:
  - `value` :: [Type](#Type): The type of the LuaLazyLoadedValue.
- `LuaStruct`:
  - `attributes` :: array\[[Attribute](#Attribute)\]: A list of attributes with the same properties as class attributes.

#### Parameter

- `name` :: [string](#string): The name of the parameter.
- `order` :: [number](#number): The order of the member as shown in the HTML.
- `description` :: [string](#string): The text description of the parameter.
- `type` :: [Type](#Type): The type of the parameter.
- `optional` :: [boolean](#boolean): Whether the type is optional or not.

#### ParameterGroup

- `name` :: [string](#string): The name of the parameter group.
- `order` :: [number](#number): The order of the member as shown in the HTML.
- `description` :: [string](#string): The text description of the parameter group.
- `parameters` :: array\[[Parameter](#Parameter)\]: The parameters that the group adds.

#### Method <span class="small">*inherits from BasicMember*</span>

- `visibility` :: array\[[string](#string)\] (optional): The list of game expansions needed to use this method. If not present, no restrictions apply. Possible values: `"space_age"`.
- `raises` :: array\[[EventRaised](#EventRaised)\] (optional): A list of events that this method might raise when called.
- `subclasses` :: array\[[string](#string)\] (optional): A list of strings specifying the sub-type (of the class) that the method applies to.
- `parameters` :: array\[[Parameter](#Parameter)\]: The parameters of the method. How to interpret them depends on the `format` member.
- `variant_parameter_groups` :: array\[[ParameterGroup](#ParameterGroup)\] (optional): The optional parameters that depend on one of the main parameters. Only applies if `takes_table` is `true`.
- `variant_parameter_description` :: [string](#string) (optional): The text description of the optional parameter groups.
- `variadic_parameter` :: [VariadicParameter](#VariadicParameter) (optional): The variadic parameter of the method, if it accepts any.
- `format` :: [MethodFormat](#MethodFormat): Details on how the method's arguments are defined.
- `return_values` :: array\[[Parameter](#Parameter)\]: The return values of this method, which can contain zero, one, or multiple values. Note that these have the same structure as parameters, but do not specify a name.

#### VariadicParameter

- `type` :: [Type](#Type) (optional): The type of the variadic arguments of the method, if it accepts any.
- `description` :: [string](#string) (optional): The description of the variadic arguments of the method, if it accepts any.

#### MethodFormat

- `takes_table` :: [boolean](#boolean): Whether the method takes a single table with named parameters or a sequence of unnamed parameters.
- `table_optional` :: [boolean](#boolean) (optional): If `takes_table` is `true`, whether that whole table is optional or not.

#### Attribute <span class="small">*inherits from BasicMember*</span>

- `visibility` :: array\[[string](#string)\] (optional): The list of game expansions needed to use this attribute. If not present, no restrictions apply. Possible values: `"space_age"`.
- `raises` :: array\[[EventRaised](#EventRaised)\] (optional): A list of events that this attribute might raise when written to.
- `subclasses` :: array\[[string](#string)\] (optional): A list of strings specifying the sub-type (of the class) that the attribute applies to.
- `read_type` :: [Type](#Type) (optional): The type of the attribute when it's read from. Only present if this attribute can be read from.
- `write_type` :: [Type](#Type) (optional): The type of the attribute when it's written to. Only present if this attribute can be written to.
- `optional` :: [boolean](#boolean): Whether the attribute is optional or not.

#### EventRaised

- `name` :: [string](#string): The name of the event being raised.
- `order` :: [number](#number): The order of the member as shown in the HTML.
- `description` :: [string](#string): The text description of the raised event.
- `timeframe` :: [string](#string): The timeframe during which the event is raised. One of "instantly", "current_tick", or "future_tick".
- `optional` :: [boolean](#boolean): Whether the event is always raised, or only dependant on a certain condition.

#### DefineValue

- `name` :: [string](#string): The name of the define value.
- `order` :: [number](#number): The order of the member as shown in the HTML.
- `description` :: [string](#string): The text description of the define value.

#### Image

- `filename` :: [string](#string): The name of the image file to display. These files are placed into the `/static/images/` directory.
- `caption` :: [string](#string) (optional): The explanatory text to show attached to the image.

### Basic types

#### `string`

A string, which can be an identifier for something, or a description-like text formatted in Markdown.

#### `number`

A number, which could either be an integer or a floating point number, as JSON doesn't distinguish between those two.

#### `boolean`

A boolean value, which is either `true` or `false`.

------------------------------------------------------------------------

### Changelog

- Changes for version 6, introduced with Factorio 2.0.7:

  - Replaced the `type`, `read`, and `write` fields on attributes with the `read_type` and `write_type` fields

- Changes for version 5, introduced with Factorio 1.1.108:

  - Added the `filter` field to events
  - Added the `visibility` field to classes, methods and attributes. Unused before Factorio 2.0.
  - Changed the BasicMember description-related fields, removing `notes` and adding `lists` and `images`
  - Changed the `tuple` complex type to be an array of types in order
  - Combined the `variadic_type` and `variadic_description` fields on methods into a single `variadic_parameter` field
  - Combined the `takes_table` and `table_is_optional` fields on methods into a single `format` field
  - Renamed the `table_is_optional` fields on MethodFormat to `table_optional`
  - Renamed the `base_classes` field on classes to `parent`, changing it to a single string
  - Removed the `builtin_types` top-level member, merging its members as type `"builtin"` into `concepts` instead

- Changes for version 4, introduced with Factorio 1.1.89:

  - Changed internal references to include context (either `runtime:` or `prototype:`)
  - Renamed the special `struct` concept type to `LuaStruct`

- Changes for version 3, introduced with Factorio 1.1.62:

  - Added the `abstract` field to classes
  - Added the `optional` field to attributes
  - Added `type`, `literal`, `tuple` and `struct` types
  - Added the `global_functions` top level member
  - Renamed the `variant` type to `union`
  - Replaced the `category` field on concepts with the `type` field

- Changes for version 2, introduced with Factorio 1.1.54:

  - Added `raises` field to methods and attributes
  - Replaced `return_type` and `return_description` fields on methods with the `return_values`-array
  - Removed `see_also` field from classes, events, concepts, methods and attributes

- Changes for version 1, introduced with Factorio 1.1.35:

  - First release

