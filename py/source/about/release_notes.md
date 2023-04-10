- **Version 2.0.0** Apr, 2023  
    - **Breaking:** Rename `intrinsic` vector quantities to `tangent`. Change interpretation of symmetric data. Track bases per-quantity rather than per-structure.
    - **Breaking:** Remove ability to set vertex- and face- permutations for surface meshes.
    - Add `set_front_dir` to set the default front-facing camera view direction. Change the default to be +Z front.
    - Add bindings for several small view & camera related functions

- **v1.3.0** Dec 1, 2021 Adds callbacks in Python and imgui bindings, high-performance mode for big point clouds, volume mesh inspection with slice planes, more slice plane config options, better control of structure transformations and scene extents, orthographic view, back face coloring options, advanced options for customizing ImGui, support for shared linking, and bug fixes.
- **v1.2.0** July 29, 2021: Update to latest cpp version, moving forward major and minor version will be synced between the core cpp library and these bindings. Add volume meshes, slice planes, and transparent rendering. Support soft ground shadows, point clouds with variable radius, and back face culling options for surface meshes. Better programmatic camera controls. Generalize isoline support for all scalar quantities. Change the font.  Overhaul to a more flexible shader system, internally, change default screenshot format back to `png`, fix size validation bugs with surface mesh, require explicit tangent spaces.
- **v0.1.1** Sept 27, 2020: Update to latest cpp. Bind reset camera function. Bindings at cpp version `v1.1.1`.
- **v0.1.0** Apr 11, 2020: Initial release of Python bindings. Bindings at cpp version `v1.1`.
