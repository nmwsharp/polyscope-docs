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

??? func "std::string options::programName"

    ##### program name 
   
    A general name to use when referring to the program in window headings, etc. Default: `Polyscope`.

    Example:
    ```cpp
    polyscope::options::programName = "important app";
    ```


??? func "int options::verbosity"

    ##### verbosity
   
    How much useful info should polyscope print to `std::cout`? Default: `1`.

    - `0` print nothing
    - `1` print occasionally
    - `>= 2` print a lot

    Example:
    ```cpp
    polyscope::options::verbosity = 1;
    ```

??? func "std::string options::printPrefix"
    
    ##### print prefix
    
    A string used as a prefix for all messages printed to the terminal by polyscope.  Default: `[polyscope] `.

    Example:
    ```cpp
    polyscope::options::printPrefix = "[MYAPP] ";
    // prints now look like "[MYAPP] loaded openGL"
    ```

??? func "bool options::errorsThrowExceptions"
    
    ##### errors throw execptions
   
    If true, errors in polyscope throw execptions. If false, a `polyscope::error` is shown in the UI, but processing attempts to continue. Default: `false`.


??? func "int options::maxFPS"
    
    ##### max fps

    The main loop will not run at more than `maxFPS` iterations per second. `-1` disables, running the loop as fast as possible. Default: `60`.


??? func "bool options::usePrefsFile"
    
    ##### use prefs file

    Polyscope can read and write to a preferences file to save state between invocations. For now, this is primarily used to restore the window position on the desktop. The preference file is a `json`-formatted plaintext file called `.polyscope.ini`.

    This option controls the use of the preferences file. If `false`, if will be neither written nor read. Default: `true`.


??? func "bool options::alwaysRedraw"
    
    ##### always redraw

    Polyscope is designed to use lazy rendering: the scene is only re-drawn if it has changed since the last time it was drawn. This can dramatically reduce resource consumption, and keeps the immediate GUI responsive even on scenes which are irresponsibly large for the user's graphics card capabilities.

    If this option is `true`, the scene will be redrawn on every main loop iteration no matter what, circumventing the lazy drawing features. Default: `false`.
