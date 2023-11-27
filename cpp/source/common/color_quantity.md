### Color Quantity Options

These options and behaviors are available for all types of color quantities on any structure.

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the quantity enabled? | `#!cpp bool isEnabled()` | `#!cpp setEnabled(bool newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)

_(all setters return `this` to support chaining. setEnabled() returns generic quantity, so chain it last)_

