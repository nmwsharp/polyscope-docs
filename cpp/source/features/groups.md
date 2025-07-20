To manage large numbers of structures, or manage structures which are related to each other, you can gather them in **groups**. A group is a collection of structures which can be enabled/disabled together and hidden from the UI if needed. A structure can be in 0, 1, or many groups. Groups can also hold other groups, allowing nested organization.

<video width=100% autoplay muted loop>
  <source src="/media/groups_demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Example**: Basic usage of groups

```cpp
#include "polyscope/polyscope.h"
#include "polyscope/point_cloud.h"
#include "polyscope/curve_network.h"

polyscope::init();

// make a point cloud
std::vector<glm::vec3> points;
for (size_t i = 0; i < 300; i++) {
    points.push_back(glm::vec3{polyscope::randomUnit() - .5, polyscope::randomUnit() - .5, polyscope::randomUnit() - .5}); 
}
polyscope::PointCloud* psCloud = polyscope::registerPointCloud("my cloud", points);
psCloud->setPointRadius(0.02);
psCloud->setPointRenderMode(polyscope::PointRenderMode::Quad);

// make a curve network
std::vector<glm::vec3> nodes;
std::vector<std::array<size_t, 2>> edges;
nodes = { {1, 0, 0}, {0, 1, 0}, {0, 0, 1}, {0, 0, 0}, };
edges = {{1, 3}, {3, 0}, {1, 0}, {0, 2}};
polyscope::CurveNetwork* psCurve = polyscope::registerCurveNetwork("my network", nodes, edges);

// create a group for these two objects
std::string groupName = "my group";
polyscope::Group* group = polyscope::createGroup(groupName);
psCurve->addToGroup(*group);    // add by group ref
psCloud->addToGroup(groupName); // add by name

// toggle enabled for everything in the group
group->setEnabled(false);

// hide items in group from displaying in the UI
// (useful if you are registering huge numbers of structures you don't always need to see)
group->setHideDescendantsFromStructureLists(true);
group->setShowChildDetails(false);

// nest groups inside of other groups
std::string superGroupName = "my parent group";
polyscope::Group* superGroup = polyscope::createGroup(superGroupName);
superGroup->addChildGroup(*group);

polyscope::show(3);
```

### Create, get, and remove groups

??? func "`#!cpp Group* createGroup(std::string name)`"
    
    ##### create group
    
    Create a new group and return it. Group name must be a unique string (no other group may have that name).

    As always, the returned pointer is non-owning. Don't delete it.

??? func "`#!cpp Group* getGroup(std::string name)`"
    
    ##### get group
    
    Get an existing group by name. 

    As always, the returned pointer is non-owning. Don't delete it.

??? func "`#!cpp void removeGroup(std::string name, bool errorIfAbsent=true)`"
    
    ##### remove group by name
    
    Remove an existing group by name

??? func "`#!cpp void removeGroup(Group* group, bool errorIfAbsent=true)`"
    
    ##### remove group by reference
    
    Remove an existing group by reference


??? func "`#!cpp void removeAllGroups()`"
    
    ##### remove all groups

    Removes all existing groups.


### Group membership

??? func "`#!cpp void Structure::addToGroup(Group& group)`"
    
    ##### add structure to group

    Add a structure as a member of a group.

    Note that this is a member function of a **structure** object, like `pointCloud->addToGroup(group)`.

??? func "`#!cpp void Structure::addToGroup(std::string groupName)`"
    
    ##### add structure to group

    Add a structure as a member of a group, via the string name of the group.

    Note that this is a member function of a **structure** object, like `pointCloud->addToGroup(groupName)`.

??? func "`#!cpp void Group::addChildStructure(Structure& newChild)`"
    
    ##### add child structure

    Add a structure as a member of this group


??? func "`#!cpp void Group::removeChildStructure(Structure& child)`"
    
    ##### remove child structure

    Remove a structure as a member of this group


??? func "`#!cpp void Group::addChildGroup(Group& newChild)`"
    
    ##### add child group

    Add a group as a (nested) member of this group

??? func "`#!cpp void Group::removeChildGroup(Group& child)`"
    
    ##### remove child group

    Remove a group as a (nested) member of this group


### Iterate over children in a group

You can iterate over the children in a group via the `childrenStructures` and `childrenGroups` members. These members only hold top-level children, any recursion into nested children of nested groups must be done manually.

The lists are lists of `WeakHandle`s, which are a life-tracking references (in-case the underlying structure is unexpectedly deleted).

**Example:**
```cpp
polyscope::Group& group = *polyscope::getGroup("my group");

// Iterate over child structures
for(polyscope::WeakHandle<polyscope::Structure>& wh : group.childrenStructures) {
    if(wh.isValid()) {
        polyscope::Structure& myStructure = wh.get();
        /* do stuff */
    }
}

// Iterate over child groups
for(polyscope::WeakHandle<polyscope::Group>& wh : group.childrenGroups) {
    if(wh.isValid()) {
        polyscope::Group& myGroup = wh.get();
        /* do stuff */
    }
}
```


### Group settings

??? func "`#!cpp Group* Group::setEnabled(bool newEnabled)`"
    
    ##### set enabled

    Set all descendants of a group to be enabled or disabled (applies to direct members of a group, as well as recursively to all members-of-members for nested groups).

??? func "`#!cpp Group* Group::setShowChildDetails(bool newVal)`"
    
    ##### show UI details

    If true, the Groups section of the ImGui UI panel will show each childs structure info as a submenu under the group. If false, only the group name and toggle checkbox will be shown.

    (Default: true)
    
    There is also a corresponding `getShowChildDetails()`.

??? func "`#!cpp Group* Group::setHideDescendantsFromStructureLists(bool newVal)`"
    
    ##### hide from structure list

    If true, the structures which are members of this group (or descendants in any nested groups) will be hidden from the ImGui UI panel structure list.

    (Default: false)
    
    There is also a corresponding `getHideDescendantsFromStructureLists()`.

