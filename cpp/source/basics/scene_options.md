These are settings which affect the visual display of the scene. It is often convenient to set them just before calling `polyscope::init`, but they may set be anywhere.

```cpp
#include "polyscope/polyscope.h"

// a few options
polyscope::options::autocenterStructures = true;
polyscope::options::autoscaleStructures = true;

// initialize
polyscope::init();
```

??? func "`#!cpp bool options::autocenterStructures`"
    
    ##### autocenter structures

    If true, all structures will have their transform set to center their bounding box immediately after being registered.

    This centers the content nicely in view, but obscures any important absolute world positions.

    Default: `false`.

??? func "`#!cpp bool options::autoscaleStructures`"
    
    ##### autoscale structures

    If true, all structures will have their transform set to rescale their length to 1 immediately after being registered.

    This scales the content nicely in view, but obscures any important absolute world positions.

    Default: `false`.


## Extents

By default, Polyscope computes a bounding box and length scale for the structures in the scene, and uses them to adjust the rendered view. For instance, the camera view is initially pointed at the center of the bounding box, and the length scale is used to set reasonable values for the radii of points, curves, and vectors.

However, sometimes it important to fix these extents rather than automatically computing them from data. One such case is producing precisely consistent visualizations across many inputs which might have slightly different extents. Another is when outlier data makes the automatically-computed extents egregiously large. The settings below can be used to manually adjust these extents.

These parameters can be adjust in the UI under `[View] --> [Scene Extents]`.

**Example: ** fix the length scale to the unit bounding box
```cpp
polyscope::init()
polyscope::options::automaticallyComputeSceneExtents = false;
polyscope::state::lengthScale = 1.;
polyscope::state::boundingBox = 
    std::tuple<glm::vec3, glm::vec3>{ {-1., -1., -1.}, {1., 1., 1.} };
```

??? func "`#!cpp float state::lengthScale`"

    A representative length scale for the scene. 

    When Polyscope automatically computes this, most structures simply use the length of the diagonal of the bounding box.

??? func "`#!cpp std::tuple<glm::vec3, glm::vec3> state::boundingBox`"

    A bounding box for the scene, in world coordinates. The first and second elements of the tuple are the lower and upper corners of the bounding box, respectively.
  
??? func "`#!cpp bool options::automaticallyComputeSceneExtents`"
    
    ##### automatically compute extents

    If true, the `lengthScale` and `boundingBox` parameters will be automatically computed from the registered structures, and updated whenever a a structure is added or changed.

    If false, these parameters will be left unchanged.  If set to false before the first structure is registered, you are **required** to set the bounding box and length scale manually.

    Default: `true`.
