These are settings which affect the visual display of the scene.  It is often convenient to set them just before calling `polyscope.init()`, but they may generally be set anywhere.


```python
import polyscope as ps

# enable auto centering and scaling
ps.set_autocenter_structures(True)
ps.set_autoscale_structures(True)

# initialize
ps.init()
```

??? func "`#!python set_autocenter_structures(b)`"
    
    ##### autocenter structures

    If true, all structures will have their transform set to center their bounding box immediately after being registered.

    This centers the content nicely in view, but obscures any important absolute world positions.

    Default: `False`.

??? func "`#!python set_autoscale_structures(b)`"
    
    ##### autoscale structures

    If true, all structures will have their transform set to rescale their length to 1 immediately after being registered.

    This scales the content nicely in view, but obscures any important absolute world positions.

    Default: `False`.

## Extents

By default, Polyscope computes a bounding box and length scale for the structures in the scene, and uses them to adjust the rendered view. For instance, the camera view is initially pointed at the center of the bounding box, and the length scale is used to set reasonable values for the radii of points, curves, and vectors.

However, sometimes it important to fix these extents rather than automatically computing them from data. One such case is producing precisely consistent visualizations across many inputs which might have slightly different extents. Another is when outlier data makes the automatically-computed extents egregiously large. The settings below can be used to manually adjust these extents.

These parameters can be adjust in the UI under `[View] --> [Scene Extents]`.

**Example: ** fix the length scale to the unit bounding box
```python
import polyscope as ps

ps.init()
ps.set_automatically_compute_scene_extents(False)
ps.set_length_scale(1.)
low = np.array((-1, -1., -1.)) 
high = np.array((1., 1., 1.))
ps.set_bounding_box(low, high)
```

??? func "`#!python get_length_scale()`"

    Get the current representative length scale for the scene. Returns a float.

??? func "`#!python set_length_scale(s)`"

    Set a representative length scale for the scene. Takes a float.

    When Polyscope automatically computes this, most structures simply use the length of the diagonal of the bounding box.

??? func "`#!python get_bounding_box()`"

    Get the current bounding box for the scene, in world coordinates. Returns a tuple of length-3 numpy vectors. The first and second elements of the tuple are the lower and upper corners of the bounding box, respectively.

??? func "`#!python set_bounding_box(low, high)`"

    Set a bounding box for the scene, in world coordinates. Takes two length-3 numpy vectors, which are the lower and upper corners of the bounding box, respectively.
  
??? func "`#!python set_automatically_compute_scene_extents(b)`"

    If true, the length scale and bounding box parameters will be automatically computed from the registered structures, and updated whenever a a structure is added or changed.

    If false, these parameters will be left unchanged.  If set to false before the first structure is registered, you are **required** to set the bounding box and length scale manually.

    Takes a boolean.  Default: `true`.
