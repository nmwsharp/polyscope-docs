# Example scripts

Quick-and-dirty scripts that generated the screenshots/videos/etc used in the docs, saved so the examples can be regenerated or tweaked later. They don't need to be pretty.

- The generated assets themselves (images, videos) are **not** tracked here; scripts write to wherever you point them (usually `shared/media/`).
- Scripts may refer to local data (e.g. meshes in `~/mesh/`) that is not in this repo; check the defaults at the top of each script.
- Run with the Python bindings from your dev checkout of polyscope-py, e.g. `PYTHONPATH=<polyscope-py>/src:<polyscope-py>/build python <script>.py ...`

| script | used in |
| --- | --- |
| `viewports_screenshot.py` | Multiple Viewports section of Camera Controls (`media/viewports_demo.jpg`) |
