### Categorical Scalars

Scalar quantities can also be used to visualize integer-valued labels such as categories, classes, segmentations, flags, etc.

Add the labels as a scalar quantity where the values just happen to be integers (each integer represents a particular class or label), and set `DataType::CATEGORICAL`. This will change the visualization to a different set of defaults, adjust some shading rules, and use a distinct color from the colormap for each label.

### Scalar Quantity Options

These options and behaviors are available for all types of scalar quantities on any structure.

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the quantity enabled? | `#!cpp bool isEnabled()` | `#!cpp setEnabled(bool newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
color map | the [color map]([[url.prefix]]/features/color_maps) to use | `#!cpp std::string getColorMap()` | `#!cpp setColorMap(std::string newMap)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
map range | the lower and upper limits used when mapping the data in to the color map| `#!cpp std::pair<double,double> getMapRange()` | `#!cpp setMapRange(std::pair<double,double>)` and `#!cpp resetMapRange()`| no
isolines enabled | are isolines shaded (default=`false`) | `#!cpp bool getIsolinesEnabled()` | `#!cpp setIsolinesEnabled(bool newVal)`| [yes]([[url.prefix]]/basics/parameters/#persistent-values)
isoline style | stripes or thin contour lines | `#!cpp IsolineStyle getIsolineStyle()` | `#!cpp setIsolineStyle(IsolineStyle newVal)`|  [yes]([[url.prefix]]/basics/parameters/#persistent-values)
isoline period | period of isoline stripes, in data units | `#!cpp float getIsolinePeriod()` | `#!cpp setIsolinePeriod(float newVal)`|  [yes]([[url.prefix]]/basics/parameters/#persistent-values)
isoline darkness | darkness of isoline stripes (default=`0.7`) | `#!cpp float getIsolineDarkness()` | `#!cpp setIsolineDarkness(float newVal)`| [yes]([[url.prefix]]/basics/parameters/#persistent-values)
contour thickness | thickness of isoline contour lines (default=`0.3`) | `#!cpp float getIsolineContourThickness()` | `#!cpp setIsolineContourThickness(float newVal)`| [yes]([[url.prefix]]/basics/parameters/#persistent-values)


_(all setters return `this` to support chaining. setEnabled() returns generic quantity, so chain it last)_

