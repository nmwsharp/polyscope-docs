Polyscope stands on the shoulders of many outstanding open-source projects. These dependencies are all [permissively licensed]([[url.prefix]]/about/license), and [bundled with the project]([[url.prefix]]/building); we just list them here to give due credit!


| Name | Purpose | Link |
--- | --- | ---
GLFW | Window and input management with openGL | [glfw.org](http://www.glfw.org)
Dear ImGui | GUI interface (buttons, text boxes, etc) | [github.com/ocornut/imgui](https://github.com/ocornut/imgui)
ImPlot | Extension of ImGui for 2D plots (lines, scatter, etc) | [github.com/epezent/implot](https://github.com/epezent/implot)
glad | OpenGL loader (used on Windows/Linux) | [github.com/Dav1dde/glad](https://github.com/Dav1dde/glad)
glm | Vector math and glsl utilities | [glm.g-truc.net](https://glm.g-truc.net/)
stb | Header-only libraries, esp. image loading | [github.com/nothings/stb](https://github.com/nothings/stb)
json | Read/write json text | [github.com/nlohmann/json](https://github.com/nlohmann/json)
MC.h | adapted for marching cubes | [github.com/aparis69/MarchingCubeCpp](https://github.com/aparis69/MarchingCubeCpp)
mkdocs | Doc generation | [mkdocs.org](https://mkdocs.org)
mkdocs-material | Doc generation | [squidfunk.github.io/mkdocs-material/](https://squidfunk.github.io/mkdocs-material/)
googletest | Unit testing | [github.com/google/googletest](https://github.com/google/googletest)
pybind11 | (Python only) Python bindings  | [github.com/pybind/pybind11](https://github.com/pybind/pybind11)
Eigen | (Python only) numpy interop for bindings | [eigen.tuxfamily.org](http://eigen.tuxfamily.org/)

Additionally Polyscope may optionally load EGL at runtime, functionality which must be enabled by a compile flag for [headless rendering]([[url.prefix]]/features/headless_rendering). EGL is not shipped with Polyscope, and it is not linked statically nor dynamically; it is loaded at runtime from the user's system only if the headless EGL backend is initialized, akin to a plugin.

Polyscope includes a few public-domain / permissively licensed assets. Some of the built-in [matcaps]([[url.prefix]]/features/materials) are from the Blender project, and others were rendered using Blender.  The built-in colormaps come from several sources as detailed on the [colormap page]([[url.prefix]]/features/colormaps), including [Smith et. al.](https://github.com/BIDS/colormap/blob/master/colormaps.py), [cmocean](http://tos.org/oceanography/assets/docs/29-3_thyng.pdf), and [matplotlib](https://matplotlib.org/).  The concrete texture on the ground is from [cc0textures.com](https://cc0textures.com/). Thank you, artists!