Polyscope includes simple functionality for saving screenshots from the current camera view to disk. The ImGUI interface windows will be automatically hidden when taking a screenshot.

Screenshots can be taken manually by pressing the `[screenshot]` button in the options GUI window, or programmatically using the functions below. Clicking the GUI button generates a numbered screenshot file in the current directory; the arrow to the side of the button can be used to adjust file format and transparency settings for these screenshots.

It is **not** necessary to call `polyscope::show()` before taking screenshots. You can set up you scene and programmatically [configure the camera view]([[url.prefix]]/basics/camera_controls), then call `polyscope::screenshot()` to save a rendered image to disk, all without any user interaction.

**Example:** Register a mesh, position the camera, and take a screenshot
```cpp 
#include "polyscope/polyscope.h"
#include "polyscope/surface_mesh.h"

// Initialize Polyscope
polyscope::init();

// Register your mesh with Polyscope
polyscope::registerSurfaceMesh("input mesh", /* your verts */, /* your faces */);

// Position the camera
polyscope::view::lookAt(glm::vec3{10., 10., 0.}, glm::vec3{0., 2., 0.});

// Adjust some screenshot default settings if you'd like
polyscope::screenshotExtension = ".jpg";

// Take a screenshot
// It will be written to your current directory as screenshot_000000.jpg, etc
polyscope::screenshot();

// Set some options and save a named screenshot
polyscope::ScreenshotOptions opts;
opts.transparentBackground = false;
polyscope::screenshot("my_scene.jpg", opts);

// Get the pixels as a raw buffer
std::vector<unsigned char> img = polyscope::screenshotToBuffer(opts);
```

Options can be set using the `ScreenshotOptions` struct
```cpp
struct ScreenshotOptions {
  bool transparentBackground = true; // is the background transparent
  bool includeUI = false;            // are ImGUI UI elements (panels, buttons, etc) visible
};
```

- If `transparentBG` is `true`, the background will be rendered as transparent, and set as transparency alpha in the saved image if the file format supports it.
- If `includeUI` is `true`, the screenshot will be captured with the ImGui UI elements (panels, buttons, etc) visible.

???+ func "`#!cpp void screenshot(const ScreenshotOptions& options)`"
    
    ##### numbered screenshot

    Saves a screenshot to the current directory, with file named like `screenshot_000000.png`, numbered automatically in increasing order. The numbering is reset to `0` for each run of the program; existing files will be silently overwritten.

    Se the options struct above for available options.

??? func "`#!cpp void screenshot(std::string filename, const ScreenshotOptions& options)`"
    
    ##### named screenshot

    Saves a screenshot to the path given as `filename`, with format inferred from the file extension. 

    The extension should be `.png`, or `.jpg`.
    
    Se the options struct above for available options.

??? func "`#!cpp std::vector<unsigned char> screenshotToBuffer(const ScreenshotOptions& options)`"
    
    ##### screenshot to buffer

    Take a screenshot from the current view and return it as a buffer. The dimensions are `view::bufferWidth` * `view::bufferHeight`, with entries RGBA at 1 byte each.
    
    Se the options struct above for available options.

??? func "`#!cpp std::string options::screenshotExtension`"
    
    ##### screenshot extension

    Set the extension used when taking automatically-numbered screenshots, either with `screenshot()` or by clicking the GUI button.

    The extension should be `.png`, or `.jpg`.
