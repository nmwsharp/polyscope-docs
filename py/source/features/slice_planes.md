Geometric data often has complex internal structures. Slice planes can be added to the scene to cull away parts of an object and inspect its interior. These planes can be manipulated either programmatically or manually in the GUI.

<video width=100% autoplay muted loop>
  <source src="/media/movies/slice_slide.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


**Example**: sweep a slice plane through the scene to produce the animation above

```python
import numpy as np
import polyscope as ps
ps.init()

# Read & register the mesh
vertices = # your vertices
faces = # your faces
ps_mesh = ps.register_surface_mesh("my mesh", vertices, faces)

# Add a slice plane
ps_plane = ps.add_scene_slice_plane()
ps_plane.set_draw_plane(True) # render the semi-transparent gridded plane
ps_plane.set_draw_widget(True)

# Animate the plane sliding along the scene
for t in np.linspace(0., 2*np.pi, 120):
    pos = np.cos(t) * .8 + .2
    ps_plane.set_pose((0., 0., pos), (0., 0., -1.))

    # Take a screenshot at each frame
    ps.screenshot(transparent_bg=False)
```

Slice planes can also be manipulated in the GUI under `[View] --> [Slice Planes]`, where you can add and remove slice planes and control whether they are active and widgets are visible. When a plane is active in the scene, you can drag the 3D widget to adjust its pose. Additionally, for each structure, `[Options] --> [Slice Planes]` allows you to toggle whether the slice plane effects that structure.


### Creating and modifying slice planes

??? func "`#!python SlicePlane add_scene_slice_plane()`"
    
    ##### add slice plane
    
    Add a new slice plane to the scene and return it. An arbitrary number of slices planes may be added.


??? func "`#!python remove_last_scene_slice_plane()`"
    
    ##### remove slice plane
    
    Remove the most recently created slice plane.


??? func "`#!python SlicePlane.get_name()`"
    
    ##### name

    Get the unique name of the slice plane.


??? func "`#!python SlicePlane.set_pose(plane_position, plane_normal)`"
    
    ##### set pose

    Set the position and orientation of the slice plane.

      - `plane_position` is any 3D position which the plane touches (the center of the plane)
      - `plane_normal` is a vector giving the normal direction of the plane, objects in this negative side of the plane will be culled

    These input 3D vectors can be tuples, length-3 numpy arrays, or really anything that can be indexed for three components.
    


??? func "`#!python SlicePlane.set_active(val)`"
    
    ##### active
 
    Set the slice plane to be active or not. If inactive, the slice plane will not have any effect on any structures in the scene, nor will it be shown in the GUI view.


??? func "`#!python SlicePlane.get_active()`"
    
    Test whether the slice plane is active.


??? func "`#!python SlicePlane.set_draw_plane(val)`"
    
    ##### draw plane
    
    Set the slice plane to draw its plane (as a colored, semi-transparent grid). If `False` the slice plane will still slice objects, but the plane itself will not be rendered.


??? func "`#!python SlicePlane.get_draw_plane()`"
    
    Test whether the slice plane is drawing its plane.


??? func "`#!python SlicePlane.set_draw_widget(val)`"
    
    ##### draw widget
    
    Set the slice plane to draw its control widget (a grey and colored cube with handles for translations and rotations). If `False` the slice plane will still slice objects, but the widget will not be rendered.

    Note that regardless of this setting, the widget will not be visible in any screenshots by default, because it is treated as part of the GUI interface, like the ImGUI widow panes.


??? func "`#!python SlicePlane.get_draw_widget()`"
    
    Test whether the slice plane is drawing its widget.


### Per-structure ignore slice planes

By default, every slice plane affects all content in the scene. However, we can also make a particular structure ignore a given slice plane, so that it only slices through some of the objects in the scene. This can be set in the GUI for each structure under `[Options] --> [Slice Planes]`, or programatically with the function below.

```python
ps_mesh = ps.register_surface_mesh("my mesh", vertices, faces)
ps_plane = ps.add_scene_slice_plane()
ps_mesh.set_ignore_slice_plane(ps_plane, True)
```


??? func "`#!python Structure.set_ignore_slice_plane(plane, val)`"
    
    ##### ignore plane
    
    Set a slice plane to be ignored by the structure. If `val` is `True` the slice plane will be ignored, and if `False` it will be respected.

    `plane` can be passed as a plane object or as a string giving the name of a plane.

??? func "`#!python Structure.get_ignore_slice_plane(plane)`"

    Test if a slice plane is currently being ignored by the structure.
    
    `plane` can be passed as a plane object or as a string giving the name of a plane.

### Cull whole elements

For some structures, slice planes can be set to discretely cull away whole elements, rather than slicing directly through the middle of an element.  This option can be set in the GUI for each structure under `[Options] --> [Slice Planes]`, or programatically with the function below.

![cull whole elements settings]([[url.prefix]]/media/cull_whole_elements.png)

```python
ps_mesh = ps.register_surface_mesh("my mesh", vertices, faces)
ps_plane = ps.add_scene_slice_plane()
ps_mesh.set_cull_whole_elements(False)
```

??? func "`#!python Structure.set_cull_whole_elements(val)`"
    
    ##### set cull whole elements

    If `True`, slice planes will affect this structure by culling whole elements (tets, triangles, points, etc), rather than slicing through the middle of the elements.

    Note that not all structures may support culling whole elements. If not supported, this setting will do nothing.

??? func "`#!python Structure.get_cull_whole_elements()`"

    Test whether the cull whole elements setting is applied.

