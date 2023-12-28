---
hide:
  - toc
---

- **Interface**

    - [Saving and restoring camera poses](#saving-and-restoring-camera-poses)
    - [How do I take a screenshot / save an image?](#how-do-i-take-a-screenshot-save-an-image)
    - [Positioning objects in the scene and reading back results](#positioning-objects-in-the-scene-and-reading-back-results)
    - [Managing large numbers of structures and quantities](#managing-large-numbers-of-structures-and-quantities)
    - [How do I set up mouse click interactions and callbacks](#how-do-i-set-up-mouse-click-interactions-and-callbacks)

- **Appearance**

    - [Visualizing colors as exact RGB values, without any shading or tonemapping](#visualizing-colors-as-exact-rgb-values-without-any-shading-or-tonemapping)
    - [Rendering figures for papers and presentations](#rendering-figures-for-papers-and-presentations)

- **System**

    - [How do I run Polyscope on a remote or headless server?](#how-do-i-run-polyscope-on-a-remote-or-headless-server)

<!-- - **Working with Data** -->

<!-- - **Miscellaneous** -->


<!-- TODO -->
<!-- - How run polyscope in a docker container -->
<!-- - How to use floating images to visualize renders of the scene -->
<!-- - How to adjust color map limits -->
<!-- - How do I do more advanced interaction? (use imgui) -->
<!-- - How do I make sure vector lengths are consistently scaled? -->
<!-- - How do I make sure color map limits are consistent? -->
<!-- - reproducible visualizations / length scale  -->
<!-- - How do I set and restore camera poses/views (json & copy-paste) -->
<!-- - give focus on show -->
<!-- - implicits -->

### **Saving and restoring camera poses**

Use `lookAt()` and [other functions]([[url.prefix]]/basics/camera_controls/) to manually specify the viewing camera pose. 

Or, you can interactively position the camera in the scene, [copy it to your clipboard as a json string]([[url.prefix]]/basics/camera_controls/#savingrestoring-views) with `ctrl-c`, then restore it from the clipboard with `ctrl-v`. These strings can also be saved and restored programmatically.

### **How do I take a screenshot / save an image?**

See [Screenshots]([[url.prefix]]/features/screenshots/). Call `polyscope::screenshot()`, or click the `[screenshot]` button in the upper-left corner of the UI.

### **Positioning objects in the scene and reading back results**

See [Transforms]([[url.prefix]]/structures/structure_management/#transforms) for various options and to set and get per-structure transformations.
In the GUI, you can use the `[Options] --> [Transform]` menu to enable a widget to interactively transform each object within the scene.

### **Managing large numbers of structures and quantities**

Polyscope generally scales just fine with 100s or even 1000s of distinctly named structures in the scene. However, with this many structures, it may become difficult to select what you want in the UI. Polyscope has a few features which can help:

Every structure has controls in its options UI menu under `Options --> Structure Selection` and `Options --> Quantity Selection` which can be used to enable/disable all structures and quantities, or isolate to viewing a single structure.

Use [Groups]([[url.prefix]]/features/groups/) to group your structures in to categories which can be enabled/disabled all together. Notice the `hide descendants` and `show details` options on groups, which can totally hide structures from the UI while still offering some control via the group.

You can always use the [Custom UIs]([[url.prefix]]/features/callbacks_and_UIs/) to create your own interface buttons and selectors which programmatically enable or disable registered objects or adjust their settings.

### **How do I set up mouse click interactions and callbacks**

See [Mouse Interactions]([[url.prefix]]/features/callbacks_and_UIs/#mouse-interactions). There are no special callbacks for creating mouse events. Instead, you can implement almost any behavior you want via ImGui's built-in functions. There are also a few polyscope-specific functions to get information about scene at the location you clicked, such as constructing rays and querying depth.

### **Rendering figures for papers and presentations**

Several settings can be customized to give a more polished appearance. Consider:

- Adjusting the [ground plane]([[url.prefix]]/features/ground_and_shadows/) to shadow-only for ground shadows 
- Increasing [antialiasing]([[url.prefix]]/basics/program_options/#ssaa-anti-aliasing-factor) rate
- Saving [screenshots]([[url.prefix]]/features/screenshots/) with transparency for compositing

### **Visualizing colors as exact RGB values, without any shading or tonemapping**

Normally, colors are shaded and tone-mapped for rendering, which means the colors and colormapped-values you specify are not exactly the colors Polyscope renders to the screen. Use the [flat material]([[url.prefix]]/features/materials/#preserving-colors-with-the-flat-material) to circumvent these effects, and ensure that colors are flat-shaded to the screen with exactly the RGB values specified.

### **How do I run Polyscope on a remote or headless server?**

It may not not be possible to use Polyscope on a remote headless machine which does not have a physical monitor. 

If the machine _does_ have a display attached, there should be no problem. You can run and initialize Polyscope, and even if you are working remotely via script or SSH you can programmatically capture screenshots of the rendered scene. 

However, Polyscope will only work if it can create an operating system-level display window, which generally means having a physical monitor attached. Various virtual windowing systems and X-servers exist as a hypothetical workaround, however users have reported limited success with these tools, usually because they use software openGL renderers which do not support the openGL features required by Polyscope.

In implementation terms, this limitation comes from needing to initialize an OpenGL 3.3 core-profile context using [GLFW](https://www.glfw.org/). Currently, GLFW can only create an openGL context when a display is present. If you find a good workaround for Polyscope on headless machines, please share! One day, we hope to implement an alternate EGL backend, which would support headless machines.

