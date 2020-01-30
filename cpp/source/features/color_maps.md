## Built-in color maps

Different color maps are appropriate for different situations:

- *sequential* maps data in to a linear range (when it doesn't fall in to one of the more specific categories below).
- *diverging* maps data in to a linear range, where the center value is "neutral" and the endpoints of the range are opposite and symmetric. Examples include a rate of change, or a residual; in both cases `0` semantially means "nothing", and the endpoints have opposite meaning.
- *cyclic* maps data defined on the circle, like an angle
- *decorative* maps should generally not be used to encode numerical data, but may be useful for other visualization purposes

<!--TODO render images of these-->

Polyscope supports the following built-in color maps:

| **Name** | **Type** | **String Key** | 
--- | --- | ---
viridis | sequential | `viridis`
blues | sequential | `blues`
reds | sequential | `reds`
coolwarm | diverging | `coolwarm`
pink-green | diverging | `pink-green`
phase | cyclic | `phase`
spectral | decorative | `spectral`
rainbow | decorative | `rainbow`
jet | decorative | `jet`


[^1]: Viridis is by Nathaniel J. Smith, Stefan van der Walt, and Eric Firing. [link](https://github.com/BIDS/colormap/blob/master/colormaps.py)

[^2]: Phase is from the `cmocean` package. [link](http://tos.org/oceanography/assets/docs/29-3_thyng.pdf)

[^3]: The other color maps have unclear origins or are simple linear ramps, and are implemented in [matplotlib](https://matplotlib.org/).

## Loading custom color maps

Custom colormaps can be loaded at runtime from image files and used anywhere colormaps are used. Loading can be performed with the UI from `[Appearance] --> [Color maps] --> [Load color map]`, or programatically using the function below. The input should be a horizontally-oriented image file like the one below; the centermost row of pixels will be read to generate the color map. Most common image formats are accepted (anyting `stb_image` can read).

![sample colormap](/media/sample_colormap.png)

??? func "`#!cpp void polyscope::loadColorMap(std::string cmapName, std::string filename)`"

    ##### loadColorMap 

    Load a new colormap from the image file `filename`, which will be assigned the name `cmapName`.
