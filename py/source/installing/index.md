## Installing from PyPi

Polyscope is registered on PyPi, so you can install with:
```sh
pip install polyscope
```
(as always this `pip` should match the version of python you intend to use; you might want `pip3` on your system to install for Python 3.)

Polyscope supports Python 2.7+ and Python 3.5+.

Ideally, this install will resolve to a precompiled wheels for your platform. If not, the setup script will compile the Polyscope C++ library from source, which may take a few mintues. This process requires a suitable C++ toolchain; see [building from source](#building-from-source).

## Installing manually

To manually download the sources:

```sh
git clone --recursive https://github.com/nmwsharp/polyscope-py.git
cd polyscope-py
```

Polyscope can then by installed with pip as
```sh
pip install .
```

Or manually installed with the setup script using
```sh
python setup.py install
```

## Building from source

If a pre-compiled wheel is not available, the setup scripts (either run automatically via `pip` or manually with `setup.py`) will need to compile the underlying C++ library. Your system must have a suitable C++ compiler available to build Polyscope, as well as build tools like CMake installed. See the main Polyscope C++ repository for more details about compiling. Polyscope is a 3D graphics program, so it may be difficult to build on servers without graphics support, or extremely old machines. In particular, OpenGL 3.3 is a hard requirement.

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
