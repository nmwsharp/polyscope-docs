---
hide:
  - toc
---

- **Interface and Camera Controls**

    - [Saving and restoring camera poses](#saving-and-restoring-camera-poses)
    - [Centering the view on an area of interest](#centering-the-view-on-an-area-of-interest)
    - [How do I take a screenshot / save an image?](#how-do-i-take-a-screenshot-save-an-image)
    - [Positioning objects in the scene and reading back results](#positioning-objects-in-the-scene-and-reading-back-results)
    - [Managing large numbers of structures and quantities](#managing-large-numbers-of-structures-and-quantities)

- **Interactions**

    - [How do I show animated data?](#how-do-i-show-animated-data)
    - [How do I create custom UIs with buttons, sliders, text boxes, etc?](#how-do-i-create-custom-uis-with-buttons-sliders-text-boxes-etc)
    - [How do I set up mouse click interactions and callbacks](#how-do-i-set-up-mouse-click-interactions-and-callbacks)

- **Appearance**

    - [Visualizing colors as exact RGB values, without any shading or tonemapping](#visualizing-colors-as-exact-rgb-values-without-any-shading-or-tonemapping)
    - [Rendering figures for papers and presentations](#rendering-figures-for-papers-and-presentations)

- **System**

    - [How do I run Polyscope remotely / on a headless server / in a notebook?](#how-do-i-run-polyscope-remotely-in-a-browser-via-a-notebook-or-on-headless-server)


<!-- - **Working with Data** -->

<!-- - **Miscellaneous** -->


### **Saving and restoring camera poses**

Use `look_at()` and [other functions]([[url.prefix]]/basics/camera_controls/) to manually specify the viewing camera pose. 

Or, you can interactively position the camera in the scene, [copy it to your clipboard as a json string]([[url.prefix]]/basics/camera_controls/#savingrestoring-views) with `ctrl-c`, then restore it from the clipboard with `ctrl-v`. These strings can also be saved and restored programmatically.

### **Centering the view on an area of interest**

See [camera controls]([[url.prefix]]/basics/camera_controls/#centering-the-view-on-scene-content). You can use ctrl+shift+click (cmd+shift+click on macOS) to orbit the view about a point of interest, as well as zooming in relative to that point.

### **How do I take a screenshot / save an image?**

See [Screenshots]([[url.prefix]]/features/screenshots/). Call `screenshot()`, or click the `[screenshot]` button in the upper-left corner of the UI.

### **Positioning objects in the scene and reading back results**

See [Transforms]([[url.prefix]]/structures/structure_management/#transforms) for various options and to set and get per-structure transformations.
In the GUI, you can use the `[Options] --> [Transform]` menu to enable a widget to interactively transform each object within the scene.

### **Managing large numbers of structures and quantities**

Polyscope generally scales just fine with 100s or even 1000s of distinctly named structures in the scene. However, with this many structures, it may become difficult to select what you want in the UI. Polyscope has a few features which can help:

Every structure has controls in its options UI menu under `Options --> Structure Selection` and `Options --> Quantity Selection` which can be used to enable/disable all structures and quantities, or isolate to viewing a single structure.

Use [Groups]([[url.prefix]]/features/groups/) to group your structures in to categories which can be enabled/disabled all together. Notice the `hide descendants` and `show details` options on groups, which can totally hide structures from the UI while still offering some control via the group.

You can always use the [Custom UIs]([[url.prefix]]/features/callbacks_and_UIs/) to create your own interface buttons and selectors which programmatically enable or disable registered objects or adjust their settings.

### **How do I show animated data**

There is no explicit built-in functionality for animated or time-series data, but it is easy and common to [do it yourself with a per-frame callback function]([[url.prefix]]/basics/interactive_UIs_and_animation/).

### **How do I create custom UIs with buttons, sliders, text boxes, etc**

Polyscope integrates with the excellent [Dear ImGui](https://github.com/ocornut/imgui) library for UI elements, and comes with its own bindings to use ImGui from Python. See the [interactions page]([[url.prefix]]/basics/interactive_UIs_and_animation/) for how to use ImGui functions within polyscope, and see the ImGui docs for everything ImGui can do.

### **How do I set up mouse click interactions and callbacks**

See [Mouse Interactions]([[url.prefix]]/basics/interactive_UIs_and_animation/#mouse-interactions). Polyscope follows an immediate-mode philosophy for interactions: rather than registering many callbacks for various IO events, you can test for mouse and keyboard state in your main loop, or in the per-frame callback (which is the only callback), to implement any behavior your would like. ImGui offers many functions for testing mouse/keyboard state, and there are also a few polyscope-specific functions to get information about scene at the location you clicked, such as constructing rays and querying depth.

### **Rendering figures for papers and presentations**

Several settings can be customized to give a more polished appearance. Consider:

- Adjusting the [ground plane]([[url.prefix]]/features/ground_and_shadows/) to shadow-only for ground shadows 
- Increasing [antialiasing]([[url.prefix]]/basics/program_options/#ssaa-anti-aliasing-factor) rate
- Saving [screenshots]([[url.prefix]]/features/screenshots/) with transparency for compositing

### **Visualizing colors as exact RGB values, without any shading or tonemapping**

Normally, colors are shaded and tone-mapped for rendering, which means the colors and colormapped-values you specify are not exactly the colors Polyscope renders to the screen. Use the [flat material]([[url.prefix]]/features/materials/#preserving-colors-with-the-flat-material) to circumvent these effects, and ensure that colors are flat-shaded to the screen with exactly the RGB values specified.

### **How do I run Polyscope remotely in a browser, via a notebook, or on headless server?**

See [headless rendering]([[url.prefix]]/features/headless_rendering/). 

In short, Polyscope _does_ support headless rendering: it can be used on remote serves with no display attached to render images and videos to files or buffers, by initializing with a special EGL backend. However, Polyscope _does not_ currently support any kind of client-server mode, or execution in the browser from remote machines, etc. It must be executing locally on the machine which you are using it from.  

Polyscope does not currently support creating interactive visualizations inline in IPython/Jupyter notebooks when the kernel is executing on a remote server. If the kernel is executing on your local machine, you _can_ use Polyscope, but the windows will be created directly on your desktop system outside of the notebook.