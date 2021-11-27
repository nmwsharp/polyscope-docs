These are general settings which affect polyscope's behavior as a library. It is often convenient to set them just before calling `polyscope::init`, but they may set be anywhere.

```cpp
#include "polyscope/polyscope.h"

// a few options
polyscope::options::programName = "important app";
polyscope::options::verbosity = 0;
polyscope::options::usePrefsFile = false;

// initialize
polyscope::init();
```

### Options

??? func "`#!cpp std::string options::programName`"

    ##### program name 
   
    A general name to use when referring to the program in window headings, etc. Default: `Polyscope`.

    Example:
    ```cpp
    polyscope::options::programName = "important app";
    ```


??? func "`#!cpp int options::verbosity`"

    ##### verbosity
   
    How much useful info should polyscope print to `std::cout`? Default: `1`.

    - `0` print nothing
    - `1` print occasionally
    - `>= 2` print a lot

    Example:
    ```cpp
    polyscope::options::verbosity = 1;
    ```

??? func "`#!cpp std::string options::printPrefix`"
    
    ##### print prefix
    
    A string used as a prefix for all messages printed to the terminal by polyscope.  Default: `[polyscope] `.

    Example:
    ```cpp
    polyscope::options::printPrefix = "[MYAPP] ";
    // prints now look like "[MYAPP] loaded openGL"
    ```

??? func "`#!cpp bool options::errorsThrowExceptions`"
    
    ##### errors throw execptions
   
    If true, errors in polyscope throw execptions. If false, a `polyscope::error` is shown in the UI, but processing attempts to continue. Default: `false`.


??? func "`#!cpp bool options::enableRenderErrorChecks`"
    
    ##### render error checks

    If true, the rendering subsystem will eagerly check for and report errors. This comes at some small performance cost, but can help catch problems.

    Default: `true` when compiled in `Debug` mode, `false` in `Release` mode.
    

??? func "`#!cpp int options::ssaaFactor`"
    
    ##### SSAA anti-aliasing factor

    Enable super-sampling anti-aliasing for a prettier rendered scene. SSAA renders the scene at multiple samples for each pixel, then averages them to resolve final pixel values. 

    Cost scales quadratically with the value of this parameter, so it will quickly become expensive. Reasonable values are in the range `1` to `4`. Using `2` is generally sufficient for anti-aliasing.

    Default: `1` (no anti-aliasing)

??? func "`#!cpp int options::maxFPS`"
    
    ##### max fps

    The main loop will not run at more than `maxFPS` iterations per second. `-1` disables, running the loop as fast as possible. Default: `60`.


??? func "`#!cpp bool options::usePrefsFile`"
    
    ##### use prefs file

    Polyscope can read and write to a preferences file to save state between invocations. For now, this is primarily used to restore the window position on the desktop. The preference file is a `json`-formatted plaintext file called `.polyscope.ini`.

    This option controls the use of the preferences file. If `false`, if will be neither written nor read. Default: `true`.


??? func "`#!cpp bool options::alwaysRedraw`"
    
    ##### always redraw

    Polyscope is designed to use lazy rendering: the scene is only re-drawn if it has changed since the last time it was drawn. This can dramatically reduce resource consumption, and keeps the immediate GUI responsive even on scenes which are irresponsibly large for the machine's graphics capabilities.

    If this option is `true`, the scene will be redrawn on every main loop iteration no matter what, circumventing the lazy drawing features. Default: `false`.

??? func "`#!cpp bool options::buildGui`"
    
    ##### build gui

    This option can be used to disable all of Polyscope's ImGui UI elements, which may be useful for advanced applications which wish to build a fully-custom UI on top of Polyscope.

    If false, Polyscope will not create any ImGui UIs at all, but will still set up ImGui and invoke its render steps each frame. The allows advanced users to create their own UIs totally from scratch and circumvent the standard Polyscope UIs.

    If desired, the functions `buildStrctureGui()`, etc can be manually invoked to build pieces of the UI, but know that these are internal details which may change without warning in future verisons.

    Default: `true`.


??? func "`#!cpp bool options::openImGuiWindowForUserCallback`"
    
    ##### open imgui window for user callback

    If true, an ImGui window will be created and docked to the side of the UI when the [user callback function](../../features/callbacks_and_UIs) is invoked. This means you can immediately start making ui calls like `ImGui::Button("do stuff")`. 
    
    If false, no ImGui anything will be pushed on the stack when the callback is invoked, and the user is entirely responsible for making any ImGui calls (or not making any).

    Default: `true`.

??? func "`#!cpp bool options::invokeUserCallbackForNestedShow`"
    
    ##### invoke user callback for nested show

    Suppose you call `polyscope::show()`, and within your callback, another instance of `polyscope::show()` is called---this is a nested show.

    Depending on the situation, you might or might not want your `userCallback` to continue being executed on each render loop iteration of this nested viewer; this setting exposes the option.

    If true, your callback will be executed as normal for every main loop iteration, even in nested show windows.

    If false, your callback will only be executed for initial, outermost calls to `polyscope::show()`.

    Default: `false`.

??? func "`#!cpp bool options::giveFocusOnShow`"
    
    ##### give focus on show

    If true, the Polyscope window will request focus from the window manager whenever `show()` is called. If false, the focus state will be left unchanged.

    Default: `false`.
