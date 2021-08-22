Polyscope is primarily focused on 3D data, but can also be used for 2D visualization. This section descibes a few helpers which make it easier to do so.

### Adding 2D data

Functions which accept 3D positions (or vectors) as input can alternately takes 2D positions, and append a 0 z-coordinate.  In Python (unlike the C++ api), we can use 2D data by simply passing it as the argument of a function which would otherwise take 3D data. For instance, `register_point_cloud(name, data)` normally expects `data` to be a `Nx3` array of 3D positions, but passing an `Nx2` array also works just fine.  Any other functions which don't take 3D positions can be used as normal, like `add_scalar_quantity()`.

### Planar camera mode

The Polyscope camera can be "locked-in" to a 2D view by setting the mode to `Planar`. In the UI, this option is in the main Polyscope window, set to `Turntable` by default. Setting the camera mode to `Planar` will also hide the ground plane.

![planar view setting]({{url.prefix}}/media/view_planar.png){: style="height:200px;"}

To set this option programmatically, use:
```
ps.set_navigation_style("planar")
```

