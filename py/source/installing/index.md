Polyscope supports Python 2 and 3 on Linux, macOS, and Windows. At runtime, your environment must support OpenGL >= `3.3 core`, and have the ability to open windows in a display. This includes nearly all modern desktop/laptop computers, but not all headless servers and virtual machines.

## Installing from PyPi

```sh
python -m pip install polyscope
```
Using `python -m pip install` rather than just `pip install` helps when your system has multiple version of Python installed, ensuring the correct `pip` is used. Just be sure `python` refers to the install of Python you intend to use.

Ideally, this install will resolve to a precompiled wheel for your platform---see [troubleshooting](#troubleshooting) if not. Otherwise, the setup script will compile the Polyscope C++ library from source, which may take a few minutes, and requires a suitable C++ toolchain (see [building from source](#building-from-source)).

#### Troubleshooting

On common platforms, `pip` should always be able to install from a binary `.whl` file. If it fails to select a binary wheel, it will try to compile from source, leading to long install times or compilation errors if your toolchain is not configured.

Here are some common fixes: 

- Ensure you're targeting the latest Polyscope `python -m pip install polyscope --upgrade`
- Very old versions of `pip` may not be able to use the precompiled wheels. Upgrade `pip` with `python -m pip install pip --upgrade`.
- Precompiled wheels are available on pip for Python 2.7 and 3.5-3.8 (aka most common versions), check yours with `python --version`, and update your Python install if needed.


## Installing from Conda

```sh
conda install -c conda-forge polyscope
```

!!! note 
    
    Windows Python 2.7 builds on conda may have dependency problems; the issue will be resolved soon.
    
    Remember that that you can still use `pip` in conjuction with conda, like `python -m pip install polyscope`.


## Installing manually

To manually download the sources:

```sh
git clone --recursive https://github.com/nmwsharp/polyscope-py.git
cd polyscope-py
```

Polyscope can then by installed with pip as
```sh
python -m pip install .
```

Or manually installed with the setup script using
```sh
python setup.py install
```

## Building from source

If a pre-compiled wheel is not available, the setup scripts (either run automatically via `pip` or manually with `setup.py`) will need to compile the underlying C++ library. Your system must have a suitable C++ compiler available to build Polyscope, as well as build tools like CMake installed. The [Polyscope C++ repository](https://polyscope.run/building/) has a few more details about compiling. Polyscope is a 3D graphics program, so it may be difficult to build on servers without graphics support, or extremely old machines. In particular, OpenGL >= `3.3 core` is a strict requirement.

## Development builds

To compile Polyscope locally without `setup.py` (e.g., if you are developing the library) use

```sh
git clone --recursive https://github.com/nmwsharp/polyscope-py.git
cd polyscope-py
mkdir build && cd build
cmake ..
make -j4
```

this will generate a file something like `polyscope_bindings.cpython-36m-x86_64-linux-gnu.so` (the particular name depends on your platform), which contains the low-level bindings to C++ Polyscope. This is a [pybind11](https://pybind11.readthedocs.io/en/stable/) build; it can be further customized using any pybind11 CMake options, for instance to choose which version of Python is used.

The actual Polyscope python library lives in `src/polyscope`, which is a wrapper around these low-level bindings. You are now ready to `import polyscope`, so long as both the compiled bindings and `src/polyscope` can be found on your `PYTHONPATH`.
