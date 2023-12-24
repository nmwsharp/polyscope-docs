This page describes the basic control flow to initialize Polyscope and invoke it from you program. See the _structures and quantities_ sections on the left for the various kinds of data you can add to Polyscope.

Polyscope needs to be initialized exactly once by calling `init()`, typically near the beginning of your program. You can then register structures to the scene, and show the window using either of two methods.

## Program Structure

There are two separate ways to structure your program's control flow with polyscope.

**Option 1: show()** The simpler, and more-common approach is to call `show()`, which will run Polyscope's window continuously. The `show()` function will not return until the window is closed. If you want to execute your own code while the Polyscope window is active, you must do so via [the `userCallback`]([[url.prefix]]/features/callbacks_and_UIs).

```cpp
#include "polyscope/polyscope.h"
polyscope::init();

/* 
 * ... your code ...
 * ... add visualizations to Polyscope, etc ...
 */

// if desired, set up a userCallback to execute your code each
// frame and add ImGui UI elements

polyscope::show(); // shows the UI, blocks until the UI exits

// If desired, add more visualizations, then show the UI again.
// Data is preserved between calls to show() unless explicitly removed.
// ... your code ...
polyscope::show();
```

**Option 2: frameTick()** An alternate approach is to manually call `frameTick()` in a tight loop to run the UI. This is useful to quickly integrate Polyscope into existing programs which already have a main loop. [The `userCallback`]([[url.prefix]]/features/callbacks_and_UIs) is still necessary to add ImGui UI elements.

```cpp
#include "polyscope/polyscope.h"
polyscope::init();

// if desired, set up a userCallback to add ImGui UI elements

while(/* program runs */) {

    /* 
     * ... your code ...
     * ... add visualizations to Polyscope, etc ...
     */

    polyscope::frameTick(); // renders one UI frame, returns immediately
}
```

Either way, `init()` must be called before you do anything with Polyscope.

!!! info "Where to make ImGui calls"

    Polyscope includes ImGui, allowing you to build custom UI elements like buttons and fields. 

    Regardless of which control flow method you use, ImGui calls can _only_ be make within [the `userCallback` function]([[url.prefix]]/features/callbacks_and_UIs). Making ImGui calls elsewhere will lead to errors and crashes.

## Functions

`#!cpp #include "polyscope/polyscope.h"`

??? func "`#!cpp init(std::string backend="")`"

    ##### init()

    Initialize polyscope. Should be called exactly once, generally at the beginning of a program. Will throw an error if anything goes wrong during initialization.

    Performs one-time work like setting up openGL and creating a window.

    `backend` is an optional specifier for which [rendering backend]([[url.prefix]]/building#backends) to use, passing `""` selects a reasonable default backend. Generally, you should not need to manually set the backend.


??? func "`#!cpp show()`"
    
    ##### show()

    Give control to the polyscope GUI. Blocks until the user returns control via the GUI, possibly by exiting the window.

    This function can be called anywhere, and can be called multiple times to re-open the GUI after it has been closed. Existing data will be preserved between calls to `frameTick()` and `show()`.

    You can even nest calls to `show()`---for instance, if the user clicks a button in your callback which executes some function, you can invoke `show()` again within that function for immediate debugging. Closing the nested window will then "pop back" to continue displaying the previously shown GUI.
    
    If desired, register a `userCallback` which will be internally executed by Polyscope within each frame, you may **not** make ImGui calls arbitrarily throughout your code.

    Several options are available which affect the behavior of `show()`, such as whether the window is automatically brought to the front and given focus. See the options listing for details.

??? func "`#!cpp unshow()`"
    
    ##### unshow()

    The opposite of `show()`. If `show()` is currently active, this closes the window and causes the call to `show()` to return. This is equivalent to manually closing the Polyscope window by clicking the window manager's close button.

    Generally it is not necessary to call this function; the user can exit by closing the window. However, `unshow()` may be useful to programmatically close the window when a condition is met, or via a custom ImGui element.

     `unshow()` does _not_ deinitialize Polyscope. You can still call `show()` again after.

??? func "`#!cpp frameTick()`"
    
    ##### frameTick()

    Render one frame of the polyscope UI. This function needs to be called in a tight loop by your code, like:

    ```cpp
    polyscope::init();

    while(/* program runs */) {

        /* 
         * ... your code ...
         */

        polyscope::frameTick();
    }
    ```

    If `frameTick()` is not called often enough, the interface will be unresponsive.

    This function can be called anywhere, and can be called multiple times to re-open the GUI after it has been closed.  Existing data will be preserved between calls to `frameTick()` and `show()`.

    If any ImGui UI elements are to be created, they must be created inside of a `userCallback()` (which will be internally executed by Polyscope within each `frameTick()`, you may **not** make ImGui calls arbitrarily throughout your code.

    The `frameTick()` function can be called anywhere within your program's control flow, including from multiple call sites. You may also interleave or nest calls to `frameTick()` and `show()` to use both kinds of control flow within a program.
