To manage large numbers of structures, or manage structures which are related to each other, you can gather them in **groups**. A group is a collection of structures which can be enabled/disabled together and hidden from the UI if needed. A structure can be in 0, 1, or many groups. Groups can also hold other groups, allowing nested organization.

<video width=100% autoplay muted loop>
  <source src="[[url.prefix]]/media/groups_demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


**Example**: Basic usage of groups

```python
import polyscope as ps
import numpy as np

ps.init()

# make a point cloud
pts = np.zeros((300,3))
psCloud = ps.register_point_cloud("my cloud", pts)

# make a curve network
nodes = np.zeros((4,3))
edges = np.array([ [1, 3], [3, 0], [1, 0], [0, 2] ])
psCurve = ps.register_curve_network("my network", nodes, edges)

# create a group for these two objects
group = ps.create_group("my group")
psCurve.add_to_group(group) # you also say psCurve.add_to_group("my group")
psCloud.add_to_group(group)

# toggle the enabled state for everything in the group
group.set_enabled(False)

# hide items in group from displaying in the UI
# (useful if you are registering huge numbers of structures you don't always need to see)
group.set_hide_descendants_from_structure_lists(True)
group.set_show_child_details(False)

# nest groups inside of other groups
super_group = ps.create_group("py parent group")
super_group.add_child_group(group)

ps.show(3)
```

### Create, get, and remove groups

??? func "`#!python create_group(name)`"
    
    ##### create group
    
    Create a new group and return it. Group name must be a unique string (no other group may have that name).

    Returns the new group object.

??? func "`#!python get_group(name)`"
    
    ##### get group
    
    Get an existing group by name. 

    Returns the group object.

??? func "`#!python remove_group(group, error_if_absent=true)`"
    
    ##### remove group
    
    Remove an existing group. 

    The `group` argument can be either a group object or a group name string.


??? func "`#!python removeAllGroups()`"
    
    ##### remove all groups

    Removes all existing groups.


### Group membership

??? func "`#!python Structure.add_to_group(group)`"
    
    ##### add structure to group

    Add a structure as a member of a group.

    The `group` argument can be either a group object or a group name string.

    Note that this is a member function of a **structure** object, like `pointCloud.add_to_group(group)`.


??? func "`#!python Group.add_child_structure(newChild)`"
    
    ##### add child structure

    Add a structure as a member of this group


??? func "`#!python Group.remove_child_structure(child)`"
    
    ##### remove child structure

    Remove a structure as a member of this group


??? func "`#!python Group.add_child_group(newChild)`"
    
    ##### add child group

    Add a group as a (nested) member of this group
    
    The `group` argument can be either a group object or a group name string.

??? func "`#!python Group.remove_child_group(child)`"
    
    ##### remove child group

    Remove a group as a (nested) member of this group
    
    The `group` argument can be either a group object or a group name string.


### Iterate over children in a group

??? func "`#!python Group.get_child_structure_names()`"
    
    ##### get child structure names

    Get a list of the string names of all structures contained in the group.

    Only returns top-level children, does not recurse into sub-groups.

    You can get the underlying structures like `get_surface_mesh(structure_name)`, etc, and process as desired.

??? func "`#!python Group.get_child_group_names()`"
    
    ##### get child group names

    Get a list of the group names of all nested groups contained in the group.

    Only returns top-level children, does not recurse into sub-groups.

    You can get the underlying groups like `get_group(group_name)`, etc, and process as desired.

### Group settings

??? func "`#!python Group.set_enabled(newVal)`"
    
    ##### set enabled

    Set all descendants of a group to be enabled or disabled (applies to direct members of a group, as well as recursively to all members-of-members for nested groups).

    The `newVal` argument is a bool.

??? func "`#!python Group.set_show_child_details(newVal)`"
    
    ##### show UI details

    If true, the Groups section of the ImGui UI panel will show each childs structure info as a submenu under the group. If false, only the group name and toggle checkbox will be shown.

    The `newVal` argument is a bool.
    
    (Default: true)

??? func "`#!python Group.set_hide_descendants_from_structure_lists(newVal)`"
    
    ##### hide from structure list

    If true, the structures which are members of this group (or descendants in any nested groups) will be hidden from the ImGui UI panel structure list.
    
    The `newVal` argument is a bool.

    (Default: false)
    
