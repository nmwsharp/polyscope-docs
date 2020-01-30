## Initializing

Once polyscope is a part of your project, creating visualizations is very easy. Polyscope needs to be initialized once, typically near the beginning of your program.

**Example:**
```cpp

#include "polyscope/polyscope.h"

// Initialize polyscope, creating graphics contexts and constructing a window.
// Should be called exactly once.
polyscope::init();

/*
 * build visualizations, here or in distant code
 * 
 */

// Pass control flow to polyscope, displaying the interactive window.
// Function will return when user closes the window.
polyscope::show();
```

## Functions

`#!cpp #include "polyscope/polyscope.h"`

??? func "`#!cpp init(std::string backend="")`"

    ##### init()

    Initialize polyscope. Should be called exactly once, generally at the beginning of a program. Will throw an error if anything goes wrong during initialization.

    Performs one-time work like setting up openGL and creating a window.

    `backend` is an optional specifier for which [rendering backend](/building#backends) to use, passing `""` selects a reasonable default backend. Generally, you should not need to manually set the backend.


??? func "`#!cpp show()`"
    
    ##### show()

    Give control to the polyscope GUI. Blocks until the user returns control via the GUI, possibly by exiting the window.

    This function can be called anywhere, and can be called multiple times to re-open the GUI after it has been closed. Existing data will be preserved between calls to `show()`.
