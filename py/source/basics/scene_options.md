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
