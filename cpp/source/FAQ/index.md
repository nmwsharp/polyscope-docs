---
hide:
  - toc
---

- **System**

    - [How do I run Polyscope on a remote or headless server?](#how-do-i-run-polyscope-on-a-remote-or-headless-server)

- **Interface**

    - [How do I take a screenshot / save an image?](#how-do-i-take-a-screenshot-save-an-image)
    - [Positioning objects in the scene and reading back results](#positioning-objects-in-the-scene-and-reading-back-results)
    - [Managing large numbers of structures and quantities](#managing-large-numbers-of-structures-and-quantities)

- **Appearance**

    - [Visualizing colors as exact RGB values, without any shading or tonemapping](#visualizing-colors-as-exact-rgb-values-without-any-shading-or-tonemapping)
    - [Rendering figures for papers and presentations](#rendering-figures-for-papers-and-presentations)

- **Working with Data**

- **Miscellaneous**


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


### **How do I take a screenshot / save an image?**

TODO ANSWER


### **How do I run Polyscope on a remote or headless server?**

It may not not be possible to use Polyscope on a remote headless machine which does not have a physical monitor. 

If the machine _does_ have a display attached, there should be no problem. You can run and initialize Polyscope, and even if you are working remotely via script or SSH you can programmatically capture screenshots of the rendered scene. 

However, Polyscope will only work if it can create an operating system-level display window, which generally means having a physical monitor attached. Various virtual windowing systems and X-servers exist as a hypothetical workaround, however users have reported limited success with these tools, usually because they use software openGL renderers which do not support the openGL features required by Polyscope.

In implementation terms, this limitation comes from needing to initialize an OpenGL 3.3 core-profile context using [GLFW](https://www.glfw.org/). Currently, GLFW can only create an openGL context when a display is present. If you find a good workaround for Polyscope on headless machines, please share! One day, we hope to implement an alternate EGL backend, which would support headless machines.


### **Rendering figures for papers and presentations**

TODO ANSWER


### **Positioning objects in the scene and reading back results**

TODO ANSWER


### **Managing large numbers of structures and quantities**

Polyscope generally scales just fine with 100s or even 1000s of distinctly named structures in the scene. However, with this many structures, it may become difficult to select what you want in the UI. Polyscope has a few features which can help:

Every structure has controls in its options UI menu under `Options --> Structure Selection` and `Options --> Quantity Selection` which can be used to enable/disable all structures and quantities, or isolate to viewing a single structure.

Use [Groups]([[url.prefix]]/features/groups/) to group your structures in to categories which can be enabled/disabled all together. Notice the `hide descendants` and `show details` options on groups, which can totally hide structures from the UI while still offering some control via the group.

You can always use the [Custom UIs]([[url.prefix]]/features/callbacks_and_UIs/) to create your own interface buttons and selectors which programmatically enable or disable registered objects or adjust their settings.


### **Visualizing colors as exact RGB values, without any shading or tonemapping**

TODO ANSWER

[flat material]([[url.prefix]]/features/materials/#preserving-colors-with-the-flat-material)
