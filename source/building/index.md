Polyscope uses CMake to configure its build system. 

### Unix-like environments (macOS,Linux,WSL)

If you're using CMake in a Unix-like environment, integrating Polyscope in to your codebase should be as simple as running
```sh
git clone --recurse-submodules https://github.com/nmwsharp/polyscope.git
```
and adding
```
add_subdirectory("polyscope")

...

target_link_libraries(YOUR_TARGET polyscope)
```
to your `CMakeLists.txt`.

See these repositories for some simple examples of using Polyscope with an existing codebase or library:

- with [geometry-central](http://geometry-central.net) -- [example project](https://github.com/nmwsharp/gc-polyscope-project-template)
- with [libIGL](https://libigl.github.io/) -- [example project](https://github.com/nmwsharp/libigl-polyscope-project-template)


### Building in Windows

If you are using Cygwin, WSL, or some other unix-emulation environment on Windows, just follow the Unix instructions above. Additionally, Polyscope builds out of the box on Visual Studio 2019 (earlier versions have not been tested). Simply run CMake (either with the GUI or terminal interface) on Polyscope's CMakeLists.txt to generate Visual Studio project and solution files. 

To integrate Polyscope with an existing Visual Studio project:

 - **(if the project uses CMake):** add Polyscope to your projects `CMakeLists.txt` as in the Unix instructions above
 - **(otherwise):** first generate the Polyscope project with its `CMakeLists.txt`, then manually add the `polyscope` project to your existing Visual Studio solution


Polyscope has been verified to compile in Visual Studio 2019 & 2017; older versions may work but have not been tested! Polyscope uses only C++11 language features, but does make advanced use of templates (for instance, SFINAE), with which some past version of MSVC have struggled.  To test Polyscope on your machine, you can compile the demo app with `examples/demo-app/CMakeLists.txt`.

### Dependencies

Polyscope packages all of its source code dependencies with the repository.

On Ubuntu and friends, you may want to `apt-get install xorg-dev libglu1-mesa-dev freeglut3-dev mesa-common-dev` to pull graphics and windowing related headers to build.
