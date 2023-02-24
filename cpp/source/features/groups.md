It can be useful to group structures together, in order to quickly hide/show them, and establish hierarchy.
Groups can be created and show up in the UI under the structures menu.

<video width=100% autoplay muted loop>
  <source src="/media/groups_demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


**Example**: enabling and disabling nested groups

```cpp
#include "polyscope/polyscope.h"
#include "polyscope/point_cloud.h"
#include "polyscope/curve_network.h"

polyscope::init();

// make a point cloud
std::vector<glm::vec3> points;
for (size_t i = 0; i < 3000; i++) {
points.push_back(
    glm::vec3{polyscope::randomUnit() - .5, 
                polyscope::randomUnit() - .5, 
                polyscope::randomUnit() - .5});
}
polyscope::PointCloud* psCloud = polyscope::registerPointCloud("my cloud", points);
psCloud->setPointRadius(0.02);
psCloud->setPointRenderMode(polyscope::PointRenderMode::Quad);

// make a curve network
std::vector<glm::vec3> nodes;
std::vector<std::array<size_t, 2>> edges;
nodes = {
{1, 0, 0},
{0, 1, 0},
{0, 0, 1},
{0, 0, 0},
};
edges = {
{1, 3},
{3, 0},
{1, 0},
{0, 2}
};
polyscope::CurveNetwork* psCurve = polyscope::registerCurveNetwork("my network", nodes, edges);

// group them together
std::string groupName = "my group";
polyscope::registerGroup(groupName);
polyscope::setParentGroupOfStructure(psCloud, groupName);
polyscope::setParentGroupOfStructure(psCurve, groupName);

// put that group in another group
std::string parentGroupName = "my parent group";
std::string emptyGroupName = "my empty group";
polyscope::registerGroup(parentGroupName);
polyscope::registerGroup(emptyGroupName);
polyscope::setParentGroupOfGroup(groupName, parentGroupName);
polyscope::setParentGroupOfGroup(emptyGroupName, parentGroupName);

polyscope::show();

polyscope::removeAllGroups();
polyscope::removeAllStructures();
```


### Creating groups and establishing hierarchy

??? func "`#!cpp bool registerGroup(std::string name)`"
    
    ##### add a group
    
    Add a new group and return it. Group name must be a unique string (no other group may have that name). The new group is a root group by default (no parent).


??? func "`#!cpp bool setParentGroupOfGroup(std::string child, std::string parent)`"
    
    ##### set the parent group of a group

    Set the parent group of a group

      - `child`: name of the child group
      - `group`: name of the parent group

??? func "`#!cpp bool setParentGroupOfStructure(std::string typeName, std::string child, std::string parent)`"
    
    ##### set the parent group of a structure

    Set the parent group of a structure

      - `typeName`: name of the structure type
      - `child`: name of the child structure
      - `group`: name of the parent group


??? func "`#!cpp bool setParentGroupOfStructure(Structure* child, std::string parent)`"
    
    ##### set the parent group of a structure

    Set the parent group of a structure

      - `child`: pointer to the child structure
      - `group`: name of the parent group

??? func "`#!cpp void setGroupEnabled(std::string name, bool enabled)`"
    
    ##### show/hide group

    Set the visibility of all of a group's children (recursive).
    Same effect as clicking the 'Enabled' checkbox in the Group UI

      - `group`: name of the group
      - `enabled` (bool) whether to show, or hide the group


??? func "`#!cpp void removeGroup(std::string name, bool errorIfAbsent = true)`"
    
    ##### remove group

    Removes a group. All its children which are groups become root groups. Nothing happens to its children which are structures.

      - `group`: name of the group
      - `error_if_absent` (bool) if true, requires the group to exist, otherwise an error is thrown.


??? func "`#!cpp void removeAllGroups()`"
    
    ##### remove all groups

    Removes all existing groups. Like with remove group, structures are unaffected.