These are general settings which affect polyscope's behavior as a library. It is often convenient to set them just before calling `polyscope.init()`, but they may generally be set anywhere.

```python
import polyscope as ps

# a few options
ps.set_program_name("important app")
ps.set_verbosity(0)
ps.set_use_prefs_file(False)

# initialize
ps.init()
```

### Options

??? func "`#!python set_program_name(name)`"

    ##### program name 
   
    A general name to use when referring to the program in window headings, etc. Default: `Polyscope`.

    Example:
    ```python
    import polyscope as ps
    ps.set_program_name("important app")
    ```


??? func "`#!python set_verbosity(v)`"

    ##### verbosity
   
    How much useful info should polyscope print to stdout? Default: `1`.

    - `0` print nothing
    - `1` print occasionally
    - `>= 2` print a lot

    Example:
    ```python
    import polyscope as ps
    ps.set_verbosity(0)
    ```

??? func "`#!python set_print_prefix(p)`"
    
    ##### print prefix
    
    A string used as a prefix for all messages printed to the terminal by polyscope.  Default: `[polyscope] `.

    Example:
    ```python
    import polyscope as ps
    ps.set_print_prefix("[MYAPP] ");
    # prints now look like "[MYAPP] loaded openGL"
    ```

??? func "`#!python set_errors_throw_exceptions(b)`"
    
    ##### errors throw execptions
   
    If true, errors in polyscope raise execptions. If false, a polyscope error is shown in the UI, but processing attempts to continue. Default: `False`.


??? func "`#!python set_enable_render_error_checks(b)`"
    
    ##### render error checks

    If true, the rendering subsystem will eagerly check for and report errors. This comes at some small performance cost, but can help catch problems.

    Default: `True` when compiled in `Debug` mode, `False` in `Release` mode (this python library is generally compiled in release mode)

??? func "`#!python set_SSAA_factor(n)`"
    
    ##### SSAA anti-aliasing factor

    Enable super-sampling anti-aliasing for a prettier rendered scene. SSAA renders the scene at multiple samples for each pixel, then averages them to resolve final pixel values. 

    Cost scales quadratically with the value of this parameter, so it will quickly become expensive. Reasonable values are in the range `1` to `4`. Using `2` is generally sufficient for anti-aliasing.

    Default: `1` (no anti-aliasing)

??? func "`#!python set_max_fps(f)`"
    
    ##### max fps

    The main loop will not run at more than `maxFPS` iterations per second. `-1` disables, running the loop as fast as possible. Default: `60`.


??? func "`#!python set_use_prefs_file(b)`"
    
    ##### use prefs file

    Polyscope can read and write to a preferences file to save state between invocations. For now, this is primarily used to restore the window position on the desktop. The preference file is a `json`-formatted plaintext file called `.polyscope.ini`.

    This option controls the use of the preferences file. If `False`, if will be neither written nor read. Default: `True`.


??? func "`#!python set_always_redraw(b)`"
    
    ##### always redraw

    Polyscope is designed to use lazy rendering: the scene is only re-drawn if it has changed since the last time it was drawn. This can dramatically reduce resource consumption, and keeps the immediate GUI responsive even on scenes which are irresponsibly large for the machine's graphics capabilities.

    If this option is `True`, the scene will be redrawn on every main loop iteration no matter what, circumventing the lazy drawing features. Default: `False`.
