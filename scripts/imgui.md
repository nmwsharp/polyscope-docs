# ImGui API Reference

All functions are in the `polyscope.imgui` namespace. Please see the [ImGui project](https://www.github.com/ocornut/imgui) for full documentation of ImGui functions and features.

These Python bindings are a 1:1 mapping of the C++ ImGui API, with concessions only for syntax that is not possible in Python. For example, C++ functions that take pointers and modify their arguments in-place instead return a Python tuple of `(is_changed, new_value)`.

See [here for an example UI]([[url.prefix]]/basics/interactive_UIs_and_animation/#sample-custom-ui).