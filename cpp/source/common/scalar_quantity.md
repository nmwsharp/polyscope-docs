### Categorical Scalars

Scalar quantities can also be used to visualize integer-valued labels such as categories, classes, segmentations, flags, etc.

Add the labels as a scalar quantity where the values just happen to be integers (each integer represents a particular class or label), and set `DataType::CATEGORICAL`. This will change the visualization to a different set of defaults, adjust some shading rules, and use a distinct color from the colormap for each label.

### Color Bars

Each scalar quantity has an associated color map, which linearly maps scalar values to a spectrum of colors for visualization.
See [colormaps]([[url.prefix]]/features/color_maps) for a listing of the available maps, and use `quantity->setColorMap("cmap_name")` to choose the map.

The colormap is always displayed with an inline colorbar in the structures panel, which also gives a histogram of the scalar values in your quantity.
The limits (`vminmax`) of the colormap range are given by the two numeric fields below the colored display. You can click and drag horizontally on these fields to adjust the map range, or ctrl-click (cmd-click) to enter arbitrary custom values. 

![image inline and onscreen colorbar]([[url.prefix]]/media/colorbar_options.jpg)

!!! note "onscreen colorbar"

    Optionally an additional onscreen colorbar, which is more similar to the colorbars used in other plotting libraries, can be enabled with `quantity->setOnscreenColorbarEnabled(true)`.

    By default it is positioned automatically inline with the other UI elements, or it can be manually positioned with `quantity->setOnscreenColorbarLocation(glm::vec2(xpos,ypos))`.

    You can even **export this color map to an `.svg` file** for creating figures, via the options menu, or with `quantity->exportColorbarToSVG("filename.svg")`.

### Scalar Quantity Options

These options and behaviors are available for all types of scalar quantities on any structure.

**Parameter** | **Meaning** | **Getter** | **Setter** | **Persistent?**
--- | --- | --- | --- | ---
enabled | is the quantity enabled? | `#!cpp bool isEnabled()` | `#!cpp setEnabled(bool newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
color map | the [color map]([[url.prefix]]/features/color_maps) to use | `#!cpp std::string getColorMap()` | `#!cpp setColorMap(std::string newMap)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
onscreen colorbar | additional onscreen colorbar | `#!cpp bool getOnscreenColorbarEnabled()` | `#!cpp setOnscreenColorbarEnabled(bool newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
onscreen colorbar location| where to put onscreen colorbar, `(-1,-1)` (default) means auto | `#!cpp glm::vec2 getOnscreenColorbarLocation()` | `#!cpp setOnscreenColorbarLocation(glm::vec2 newVal)` | [yes]([[url.prefix]]/basics/parameters/#persistent-values)
save colorbar to `.svg` file | export colorbar to file | `#!cpp void exportColorbarToSVG(std::string filename)` | - | -  
map range | the lower and upper limits used when mapping the data in to the color map| `#!cpp std::pair<double,double> getMapRange()` | `#!cpp setMapRange(std::pair<double,double>)` and `#!cpp resetMapRange()`| no
isolines enabled | are isolines shaded (default=`false`) | `#!cpp bool getIsolinesEnabled()` | `#!cpp setIsolinesEnabled(bool newVal)`| [yes]([[url.prefix]]/basics/parameters/#persistent-values)
isoline style | stripes or thin contour lines | `#!cpp IsolineStyle getIsolineStyle()` | `#!cpp setIsolineStyle(IsolineStyle newVal)`|  [yes]([[url.prefix]]/basics/parameters/#persistent-values)
isoline period | period of isoline stripes, in data units | `#!cpp float getIsolinePeriod()` | `#!cpp setIsolinePeriod(float newVal)`|  [yes]([[url.prefix]]/basics/parameters/#persistent-values)
isoline darkness | darkness of isoline stripes (default=`0.7`) | `#!cpp float getIsolineDarkness()` | `#!cpp setIsolineDarkness(float newVal)`| [yes]([[url.prefix]]/basics/parameters/#persistent-values)
contour thickness | thickness of isoline contour lines (default=`0.3`) | `#!cpp float getIsolineContourThickness()` | `#!cpp setIsolineContourThickness(float newVal)`| [yes]([[url.prefix]]/basics/parameters/#persistent-values)


_(all setters return `this` to support chaining. setEnabled() returns generic quantity, so chain it last)_

