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
