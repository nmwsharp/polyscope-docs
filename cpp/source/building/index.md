Polyscope uses CMake to configure its build system. 

## Adding Polyscope to your CMake


### Subdirectory method

First clone Polyscope's source code, using the following commands, or equivalent actions in a GUI. (Be sure to get the submodules, or you will have problems with empty directories! The `--recurse-submodules` below is important.)

```sh
git clone --recurse-submodules https://github.com/nmwsharp/polyscope.git
```

Then, add the following lines to your `CMakeLists.txt`:
```
add_subdirectory("path/to/polyscope")

...

target_link_libraries(YOUR_TARGET polyscope)
```
If you place polyscope outside of your project's source tree, you may need `add_subdirectory("path/to/polyscope" "polyscope")` to also set a library build directory.

See these repositories for some simple examples of using Polyscope with an existing codebase or library:

- with [geometry-central](http://geometry-central.net) -- [example project](https://github.com/nmwsharp/gc-polyscope-project-template)
- with [libIGL](https://libigl.github.io/) -- [example project](https://github.com/nmwsharp/libigl-polyscope-project-template)

### FetchContent 

Alternately, CMake's `FetchContent` functionality can be used to automatically download dependencies at configure-time as-needed, so you do not need to manually . You can use it by adding this to your `CMakeLists.txt`:

```
include(FetchContent)

FetchContent_Declare(
   polyscope
   GIT_REPOSITORY https://github.com/nmwsharp/polyscope.git
   GIT_TAG        master
)

FetchContent_MakeAvailable(polyscope)
target_link_libraries(YOUR_TARGET_NAME polyscope)
```

### Building in Windows

If you are using Cygwin, WSL, or some other unix-emulation environment on Windows, just follow the instructions above (though be wary that these tools often do not have good openGL and windowing support, which can be a problem at runtime for a graphical application like Polyscope). 

Additionally, Polyscope builds out of the box on Visual Studio 2019 (earlier versions have not been tested). Simply run CMake (either with the GUI or terminal interface) on Polyscope's CMakeLists.txt to generate Visual Studio project and solution files. 

To integrate Polyscope with an existing Visual Studio project:

 - **(if the project uses CMake):** add Polyscope to your projects `CMakeLists.txt` as in the Unix instructions above
 - **(otherwise):** first generate the Polyscope project with its `CMakeLists.txt`, then manually add the `polyscope` project to your existing Visual Studio solution


Polyscope has been verified to compile in Visual Studio 2019 & 2017; other versions should work but have not been tested! Polyscope uses only C++11 language features, but does make advanced use of templates (for instance, SFINAE), which some older versions of MSVC do not fully support.  To test Polyscope on your machine, you can compile the demo app with `examples/demo-app/CMakeLists.txt`.

### Dependencies

Polyscope packages all of its source code dependencies with the repository.

#### Ubuntu

On Ubuntu and friends, you may want to `apt-get install xorg-dev libglu1-mesa-dev freeglut3-dev mesa-common-dev` to pull graphics and windowing related headers to build.

#### MacOS

On MacOS it may be necessary to install X11 dependencies, this can be done using Homebrew and [xquartz](https://www.xquartz.org/) package with the command: `brew install --cask xquartz`. If you are not using CMake you will need to link against the `OpenGL`, `CoreVideo`, `Cocoa` and `IOKit` MacOS frameworks explicitly. A sample command to link your application with `g++` on MacOS is:

```sh
g++ <object files> -framework OpenGL -framework CoreVideo -framework Cocoa -framework IOKit \
     -L/opt/X11/lib/ <Other Unix Linking flags (libraries + directories)>
```

### Backends

Internally, Polyscope has (very preliminary) support for changing the rendering backend. At compile time, CMake flags control which backends Polyscope will be built with, and at runtime one of the available backends can be selected during `init()`.

Currently, only a single "real" backend is supported. However, an additional "mock" backend enables testing on headless machines.

| **Backend** | **CMake option** | **String name** | **Description**
--- | --- | --- | ---
OpenGL3 & GLFW |  `POLYSCOPE_BACKEND_OPENGL3_GLFW` | `openGL3_glfw` | The standard rendering engine for Polyscope
mock |  `POLYSCOPE_BACKEND_OPENGL_MOCK` | `openGL_mock` | Fake backend which stubs out all calls to the rendering engine, but still performs many useful internal checks.

By default the CMake script builds all (both) backends. But for instance, the OpenGL3 backend could be excluded from the build with
```sh
cmake -DPOLYSCOPE_BACKEND_OPENGL3_GLFW=OFF ..
```
and the mock backend could be used at runtime with `#!cpp polyscope::init("openGL_mock")`.

### Tests

Unit test live in the `/test/` directory, and cover most of the core functionality of Polyscope. Polyscope uses googletest, which will be downloaded automatically when you build the tests.

To build and run the tests, use:

```sh
cd test
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Debug ..
make -j4 && ./bin/polyscope-test --gtest_catch_exceptions=0
```
The backend can be set for the test script by passing an additional argument:
```sh
./bin/polyscope-test --gtest_catch_exceptions=0 backend=openGL_mock
```
