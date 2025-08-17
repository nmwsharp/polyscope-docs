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

    Default: `True` when compiled in `Debug` mode, `False` in `Release` mode (

??? func "`#!python set_warn_for_invalid_values(b)`"
    
    ##### warn for invalid values

    If true, polyscope will give warnings when any added values are `inf` or `NaN`. Most (but not quite all) floating-point buffers of data such as vertex positions, scalar/color/vector quantities, etc are checked.

    Default: `True` 
    

??? func "`#!python set_SSAA_factor(n)`"
    
    ##### SSAA anti-aliasing factor

    Enable super-sampling anti-aliasing for a prettier rendered scene. SSAA renders the scene at multiple samples for each pixel, then averages them to resolve final pixel values. 

    Cost scales quadratically with the value of this parameter, so it will quickly become expensive. Reasonable values are in the range `1` to `4`. Using `2` is generally sufficient for anti-aliasing.

    Default: `1` (no anti-aliasing)

??? func "`#!python set_max_fps(f)`"
    
    ##### max fps

    The main loop will not run at more than `maxFPS` iterations per second. `-1` disables, running the loop as fast as possible. Default: `60`.
    
    This behavior may be affected by the [`set_frame_tick_limit_fps_mode()` setting]([[url.prefix]]/basics/flow/#frame_tick_limit_fps_mode).

??? func "`#!python set_enable_vsync(b)`"
    
    ##### enable vsync

    VSync synchronizes the rendering process with your display's framerate, which may fix some visual artifacts. It also typically causes rendering to block to match the refresh rate of your monitor.

    Default: `False` on Windows and `True` on other platforms.
    
    This behavior may be affected by the [`set_frame_tick_limit_fps_mode()` setting]([[url.prefix]]/basics/flow/#frame_tick_limit_fps_mode).


??? func "`#!python set_use_prefs_file(b)`"
    
    ##### use prefs file

    Polyscope can read and write to a preferences file to save state between invocations. For now, this is primarily used to restore the window position on the desktop. The preference file is a `json`-formatted plaintext file called `.polyscope.ini`.

    This option controls the use of the preferences file. If `False`, if will be neither written nor read. Default: `False`.
    
    !!! note
    
        Dec 2024 this setting was changed to _disabled_ by default. It is a cause of rare-but-tricky bugs on some platforms, such as saving a window location from one monitor, then attempting to re-load the setting on a smaller monitor causing the window to be placed offscreen.


??? func "`#!python set_always_redraw(b)`"
    
    ##### always redraw

    Polyscope is designed to use lazy rendering: the scene is only re-drawn if it has changed since the last time it was drawn. This can dramatically reduce resource consumption, and keeps the immediate GUI responsive even on scenes which are irresponsibly large for the machine's graphics capabilities.

    If this option is `True`, the scene will be redrawn on every main loop iteration no matter what, circumventing the lazy drawing features. Default: `False`.

??? func "`#!python set_build_gui(b)`"
    
    ##### build gui

    This option can be used to disable all of Polyscope's ImGui UI elements, which may be useful for advanced applications which wish to build a fully-custom UI on top of Polyscope.

    If false, Polyscope will not create any ImGui UIs at all, but will still set up ImGui and invoke its render steps each frame. The allows advanced users to create their own UIs totally from scratch and circumvent the standard Polyscope UIs.

    Default: `True`.


??? func "`#!python set_open_imgui_window_for_user_callback(b)`"
    
    ##### open imgui window for user callback

    If true, an ImGui window will be created and docked to the side of the UI when the [user callback function](../../features/callbacks_and_UIs) is invoked. This means you can immediately start making ui calls like `polyscope.imgui.Button("do stuff")`. 
    
    If false, no ImGui anything will be pushed on the stack when the callback is invoked, and the user is entirely responsible for making any ImGui calls (or not making any).

    Default: `True`.

??? func "`#!python set_invoke_user_callback_for_nested_show(b)`"
    
    ##### invoke user callback for nested show

    Suppose you call `polyscope.show()`, and within your callback, another instance of `polyscope.show()` is called---this is a nested show.

    Depending on the situation, you might or might not want your user callback to continue being executed on each render loop iteration of this nested viewer; this setting exposes the option.

    If true, your callback will be executed as normal for every main loop iteration, even in nested show windows.

    If false, your callback will only be executed for initial, outermost calls to `polyscope.show()`.

    Default: `False`.

??? func "`#!python set_give_focus_on_show(b)`"
    
    ##### give focus on show

    If true, the Polyscope window will request focus from the window manager whenever `show()` is called. If false, the focus state will be left unchanged.

    Default: `False`.
