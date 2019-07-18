Polyscope uses CMake as its build system. 

If you're using CMAKE, integrating Polyscope in to your codebase should be as simple as running
```
git clone --recurse-submodules https://github.com/nmwsharp/polyscope.git
```
and adding
```
add_subdirectory("polyscope")
```
to your `CMakeLists.txt`.

See these repositories for some simple examples of using Polyscope to an existing codebase or library:

- with [geometry-central](http://geometry-central.net) -- [example project](https://github.com/nmwsharp/gc-polyscope-project-template)
- with [libIGL](https://libigl.github.io/) -- [example project](https://github.com/nmwsharp/libigl-polyscope-project-template)


### Dependencies

Polyscope packages all of its source code dependencies with the repository.

On Ubuntu and friends, you may want to `apt-get install xorg-dev libglu1-mesa-dev freeglut3-dev mesa-common-dev` to pull graphics and windowing related headers to build.

### Building in Windows

These instructions are unix-centric, because the project developers are mac and linux users. 

In theory, Polyscope builds just fine in Windows, though some manual effort may be required. Better instructions coming soon!
