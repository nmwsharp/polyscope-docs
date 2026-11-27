Polyscope supports Python 3.9-3.14 with prebuilt binaries on all major operating systems. At runtime, your environment must support OpenGL >= `3.3 core`, and have the ability to open windows in a display. This includes nearly all modern desktop/laptop computers, but not all headless servers and virtual machines.

## Installing with uv or conda

=== "uv"

    With [uv](https://docs.astral.sh/uv/), add Polyscope to your project:
    ```sh
    uv add polyscope
    ```

=== "conda"

    Install from PyPI using `pip` inside your conda environment:
    ```sh
    python -m pip install polyscope
    ```

Ideally, this install will resolve to a precompiled package for your platform---see [troubleshooting](#troubleshooting) if not. If there is no precompiled wheel on PyPI for your platform, the installer will compile the Polyscope C++ library from source, which may take a few minutes, and requires a suitable C++ toolchain (see [building from source](#building-from-source)).

#### Troubleshooting

On common platforms, installation should always be able to use a precompiled binary. A source build instead means long install times, or compilation errors if your toolchain is not configured.

Here are some common fixes: 

- Ensure you're targeting the latest Polyscope (see the commands below).
- Precompiled binaries are only available for supported Python versions (3.9-3.14), so check yours, and update your Python install if needed.

=== "uv"

    ```sh
    uv sync --upgrade-package polyscope
    ```
    To check your Python version, use `uv run python --version`.

=== "conda"

    ```sh
    python -m pip install --upgrade polyscope
    ```
    To check your Python version, use `python --version`.

#### Source installs from PyPI

Despite our best efforts, the precompiled binaries still may not work on some platforms. You can intentionally build the library from source using:

=== "uv"

    In a project, add this to your `pyproject.toml`:
    ```toml
    [tool.uv]
    no-binary-package = ["polyscope"]
    ```
    then run:
    ```sh
    uv sync --reinstall-package polyscope
    ```

=== "conda"

    Inside your conda environment:
    ```sh
    python -m pip install polyscope --no-binary polyscope --force-reinstall --no-deps
    ```

This may take a few minutes, and requires a suitable C++ toolchain (see [building from source](#building-from-source)).

## Installing manually

To manually download the sources:

```sh
git clone --recursive https://github.com/nmwsharp/polyscope-py.git
cd polyscope-py
```

Polyscope can then be installed from this directory:

=== "uv"

    To use your local copy from a uv project, run this in that project:
    ```sh
    uv add /path/to/polyscope-py
    ```
    and set `package = true` on the source which this adds to the project's `pyproject.toml`, then run `uv sync`:
    ```toml
    [tool.uv.sources]
    polyscope = { path = "/path/to/polyscope-py", package = true }
    ```

=== "conda"

    With your conda environment activated:
    ```sh
    python -m pip install .
    ```

## Building from source

If a precompiled binary is not available, the installer will need to compile the underlying C++ library. Your system must have a suitable C++ compiler available to build Polyscope, as well as build tools like CMake installed. The [Polyscope C++ repository](https://polyscope.run/building/) has a few more details about compiling. Polyscope is a 3D graphics program, so it may be difficult to build on servers without graphics support, or extremely old machines. In particular, OpenGL >= `3.3 core` is a strict requirement.

## Development builds

To compile Polyscope locally without installing it (e.g., if you are developing the library), first download the sources:

```sh
git clone --recursive https://github.com/nmwsharp/polyscope-py.git
cd polyscope-py
```

Then build with CMake:

=== "uv"

    ```sh
    uv sync
    uv run cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
    uv run cmake --build build --parallel 12
    ```
    Then run the tests, or your own script:
    ```sh
    uv run test/polyscope_test.py
    PYTHONPATH=src:build uv run my_script.py
    ```

=== "conda"

    ```sh
    conda create -n polyscope-dev python=3.12
    conda activate polyscope-dev
    python -m pip install numpy typing_extensions cmake
    cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
    cmake --build build --parallel 12
    ```
    Then run the tests, or your own script:
    ```sh
    python test/polyscope_test.py
    PYTHONPATH=src:build python my_script.py
    ```

The build generates a file something like `polyscope_bindings.cpython-312-x86_64-linux-gnu.so` (the particular name depends on your platform) in the `build` directory, which contains the low-level bindings to C++ Polyscope. This is a [nanobind](https://nanobind.readthedocs.io/en/latest/) build, which targets whichever Python CMake finds. A `build` directory keeps using the Python it was first configured with, so delete it when switching environments.

The actual Polyscope python library lives in `src/polyscope`, which is a wrapper around these low-level bindings. You can `import polyscope` so long as both the compiled bindings and `src/polyscope` can be found on your `PYTHONPATH`.
