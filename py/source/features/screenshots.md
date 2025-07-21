Polyscope includes simple functionality for saving screenshots from the current camera view to disk. The ImGUI interface windows will be automatically hidden when taking a screenshot.

Screenshots can be taken manually by pressing the `[screenshot]` button in the options GUI window, or programmatically using the functions below. Clicking the GUI button generates a numbered screenshot file in the current directory; the arrow to the side of the button can be used to adjust file format and transparency settings for these screenshots.

It is **not** necessary to call `show()` before taking screenshots. You can set up you scene and programmatically [configure the camera view]([[url.prefix]]/basics/camera_controls), then call `screenshot()` to save a rendered image to disk, all without any user interaction.

**Example:** Register a mesh, position the camera, and take a screenshot
```python
import polyscope as ps

# Initialize
ps.init()

# Register a mesh
verts = # ... your data ...
faces = # ... your data ...
ps_mesh = ps.register_surface_mesh("my mesh", verts, faces)

# Position the camera
ps.look_at((0., 0., 5.), (1., 1., 1.))

# Adjust some screenshot default settings if you'd like
ps.set_screenshot_extension(".jpg");

# Take a screenshot
# It will be written to your current directory as screenshot_000000.jpg, etc
ps.screenshot()

# Get the screenshot image as a numpy array
img = ps.screenshot_to_buffer()
```

???+ func "`#!python screenshot(filename=None, transparent_bg=True, include_UI=False)`"

    Saves a screenshot to the path given as `filename`, with format inferred from the file extension. 

    The extension should be one of `.png`, or `.jpg`.
    
    If no name is is given, screenshots are saved to the current directory, with file named like `screenshot_000000.png` numbered automatically in increasing order. The numbering is reset to `0` for each run of the program; existing files will be silently overwritten.

    If `transparent_bg` is `true`, the background will be rendered as transparent, and set as transparency alpha in the saved image if the file format supports it.

    If `include_UI` is true, the screenshot with be captured with the ImGui UI (panels, buttons, etc) visible (default: `False`).


??? func "`#!python set_screenshot_extension(ext)`"
    
    ##### screenshot extension

    Set the extension used when taking automatically-numbered screenshots, either with `screenshot()` or by clicking the GUI button.

    The extension should be `.png`, or `.jpg`.


??? func "`#!python screenshot_to_buffer(transparent_bg=True, vertical_flip=True, include_UI=False)`"

    ##### screenshot to buffer

    Take a screenshot of the current view and return it as a numpy array of (h,w,4).

    See `screenshot()` for the meaning of most arguments.

    The openGL buffer layout is vertically-flipped from the usual image convention in Python. The if `vertical_flip=True`, the buffer is flipped vertically before returning to match the usual convention.