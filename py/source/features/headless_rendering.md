Polyscope supports headless rendering on linux machines which do not have displays, such as remote servers and clusters.

For a variety of legacy reasons, openGL-based rendering systems often require a display attached to function. In particular Polyscope's default backend uses GLFW, which can essentially only render on machines which have a physical display attached. It does not matter if the machine has a GPU or not, and connecting via remote SSH with graphical capabilities is generally not sufficient due to required openGL capabilities. This prevents performing any kind of rendering on remote clusters and servers without out a display. This limitation would prevent workflows like running compute jobs on remote clusters and logging images or saving videos rendered via Polyscope---headless rendering offers a solution.

!!! warning "What is headless rendering not?"

    Headless rendering just means that Polyscope can run its rendering engine and render images to buffers or files. You can save them, store them, or even log them to viewers like Tensorboard.

    Headless rendering is _not_ the same as displaying the interactive window inside of an iPython notebooks, or remotely running the interactive Polyscope UI in a browser window. There is currently no support for either of these uses (although local iPython always works; the window will be opened outside of the notebook).

    Note also that the headless rendering backend is _not_ necessary if you are remotely connecting to a machine which has some kind of display attached; for instance, when remotely connecting to macOS or Windows machines with displays.

!!! note "Unix only"

    Headless rendering is only supported on Unix/Linux, because EGL is only available there.

    

## Using headless rendering
    
Headless rendering requires compiling with- and initializing a separate EGL backend.  

Fortunately, the linux Polyscope wheels published on `pip` are already built with support for EGL.

??? note "For developers: compiling with EGL support"

    If you are manually compiling Polyscope's python bindings, you must ensure EGL support is enabled. The default CMake settings enable it only if you are on Linux and EGL headers seem to be present on your system.
    
    Set the CMake variable `POLYSCOPE_BACKEND_OPENGL3_EGL=ON` to force-enable building with EGL support. 

    ```cmake
    cmake .. -DPOLYSCOPE_BACKEND_OPENGL3_EGL=ON
    ```


At runtime, you must tell Polyscope to initialize with the EGL engine. The simplest way to do this is to specify it explicitly when you call `init()`. Alternately, the default automatic initialization scheme will select the EGL headless backend if no others are available, but only if you enable the headless backends option first.

**Example:** headless usage
```python
import polyscope as ps

# explicit initialization
ps.init("openGL3_egl")
# OR
ps.set_allow_headless_backends(True)  # enable headless backends
ps.init() # automatic initialization will use the EGL backend
          # if it is available and there is no display

# ... add structures and quantities to polyscope as usual ...

ps.screenshot() # save screenshots, render movies, etc
```

Once you have initialized the backend and added your data as usual, you can preform rendering operations such as saving rendered screenshots to disk or to buffer.

Unless you really know what you are doing, you probably do not want to call `show()` -- by default this would initiate a render loop which spins endlessly with no effect. However it is still permitted to do so, e.g. if you set a user callback which has side effects.

## Options

??? func "`#!python is_headless()`"
    
    ##### is_headless()

    Returns `True` if polyscope is currently running in headless mode. May only be called after initialization.


??? func "`#!python set_allow_headless_backends(b)`"
    
    ##### set_allow_headless_backends

    If `True` default automatic initialization is allowed to initialize with a headless backend, if that is the only option.

    Default: `False`

    This is set to `False` by default, because sometimes misconfigured or low-capability machines will have no di

