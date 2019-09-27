Polyscope supports the following color maps (set via the enum `polyscope::gl::ColorMapID`).

Different color maps are appropriate for different situations:

- *sequential* maps data in to a linear range (when it doesn't fall in to one of the more specific categories below).
- *diverging* maps data in to a linear range, when the center value "neutral" and the endpoints of the range are opposite and symmetric. Examples include a rate of change, or difference from a central value; in both cases `0` semantially means "nothing", and the endpoints have opposite meaning.
- *cyclic* maps data defined on the circle, like a direction in 2D
- *decorative* maps should generally not be used to encode numerical data, but may be useful for other visualization purposes

<!--TODO render images of these-->

| **Name** | **Type** | **Enum** | 
--- | --- | ---
viridis | sequential | `VIRIDIS`
blues | sequential | `BLUES`
reds | sequential | `REDS`
coolwarm | diverging | `COOLWARM`
pink-green | diverging | `PIYG`
phase | cyclic | `PHASE`
spectral | decorative | `SPECTRAL`
rainbow | decorative | `RAINBOW`
jet | decorative | `JET`


[^1]: Viridis is by Nathaniel J. Smith, Stefan van der Walt, and Eric Firing. [link](https://github.com/BIDS/colormap/blob/master/colormaps.py)

[^2]: Phase is from the `cmocean` package. [link](http://tos.org/oceanography/assets/docs/29-3_thyng.pdf)

[^3]: The other color maps have unclear origins or are simple linear ramps, and are implemented in [matplotlib](https://matplotlib.org/).
