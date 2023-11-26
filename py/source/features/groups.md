It can be useful to group structures together, in order to quickly hide/show them, and establish hierarchy.
Groups can be created and show up in the UI under the structures menu.

<video width=100% autoplay muted loop>
  <source src="/media/groups_demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


**Example**: enabling and disabling nested groups

```python
import polyscope as ps
import numpy as np

ps.init()

# group creation, hierarchy and structure assignment
g = ps.register_group("pretty shapes")
g1 = ps.register_group("curves")
ps.set_parent_group(g1, g)
for i in range(3):
    nodes = np.random.rand(100, 3)
    edges = np.random.randint(0, 100, size=(250,2))
    ps_net = ps.register_curve_network("my network {}".format(i), nodes, edges)
    ps.set_parent_group(ps_net, g1)
g2 = ps.register_group("points")
ps.set_parent_group(g2, g)
for i in range(3):
    points = np.random.rand(100, 3)
    ps_cloud = ps.register_point_cloud("my points {}".format(i), points)
    ps.set_parent_group(ps_cloud, g2)
g3 = ps.register_group("surfaces")
ps.set_parent_group(g3, g)
for i in range(3):
    vertices = np.random.rand(100, 3)
    faces = np.random.randint(0, 100, size=(250,3))
    ps_mesh = ps.register_surface_mesh("my mesh {}".format(i), vertices, faces)
    ps.set_parent_group(ps_mesh, g3)
g4 = ps.register_group("volumes")
ps.set_parent_group(g4, g)
for i in range(3):
    verts = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1],
        [1, 1, 1.5]
    ]) / 2.0
    cells = np.array([
    [0, 1, 2, 3, 4, 5, 6, 7],
    [7, 5, 6, 8, -1, -1, -1, -1],
    ])
    ps_vol = ps.register_volume_mesh("my volume {}".format(i), verts, mixed_cells=cells)
    ps.set_parent_group(ps_vol, g4)

# setting a group to enabled/disabled
ps.set_group_enabled(g4, False)

ps.show()

ps.remove_all_groups()
```


### Creating groups and establishing hierarchy

??? func "`#!python register_group(name)`"
    
    ##### add a group
    
    Add a new group and return it. Group name must be a unique string (no other group may have that name). The new group is a root group by default (no parent).


??? func "`#!python set_parent_group(child, group)`"
    
    ##### set the parent group of a group, or structure

    Set the parent group of a group, or structure

      - `child` is a CurveNetwork, PointCloud, SurfaceMesh, VolumeMesh, or Group object
      - `group` is a Group object or string (parent group name)


??? func "`#!python set_group_enabled(group, enabled)`"
    
    ##### show/hide group

    Set the visibility of all of a group's children (recursive).
    Same effect as clicking the 'Enabled' checkbox in the Group UI

      - `group` is a Group object or string (parent group name)
      - `enabled` (bool) whether to show, or hide the group


??? func "`#!python remove_group(group, error_if_absent=True)`"
    
    ##### remove group

    Removes a group. All its children which are groups become root groups. Nothing happens to its children which are structures.

      - `group` is a Group object or string (parent group name)
      - `error_if_absent` (bool) if true, requires the group to exist, otherwise an error is thrown.


??? func "`#!python remove_all_groups()`"
    
    ##### remove all groups

    Removes all existing groups. Like with remove group, structures are unaffected.