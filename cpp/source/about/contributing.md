Polyscope is an open-source project, and you are encouraged to contribute! The core library is lives in [this repository](https://github.com/nmwsharp/polyscope), with documentation [here](https://github.com/nmwsharp/polyscope-docs) and Python bindings [here](https://github.com/nmwsharp/polyscope-py).
    
All contributions will be released under Polyscope's MIT license.

**How to make a great pull request:**

:heavy_check_mark: [Implement a feature](#c-implementation) or fix a bug

:heavy_check_mark: Write a new [unit test](#unit-testing) and run tests

:heavy_check_mark: [Submit a PR](#prs-automated-tests) and ensure automated tests pass

:heavy_check_mark: Update the [documentation](#documentation) 

:heavy_check_mark: Create any new [Python bindings](#python-bindings)

Of course, contributions that only do some of the above are still welcome and appreciated! But doing all of these steps means your pull request is most likely to be merged right away.

The sections below go in to more detail on each of these steps.

### C++ implementation

!!! info "C++ vs. Python contributions"

    Polyscope is implemented as a C++ library, with a thin binding layer to Python.

    All functionality is implemented on the C++ side---pull requests which implement new features solely on the Python side or using external Python dependencies generally will not be accepted. Please file an issue asking first if you are unsure! Of course, bugfixes and additions to the Python binding layer itself are an exception.

    Conversely, any new C++ features are strongly encouraged to add corresponding Python bindings! See below.

A few general pointers:

  - The UI (menus, dialogs, buttons, etc) is managed using [Dear ImGUI](https://github.com/ocornut/imgui), which is very well-documented and has many resources available online.
  
  - Core rendering logic and shaders are implemented in the `/render` [subdirectory](https://github.com/nmwsharp/polyscope/tree/master/include/polyscope/render), particularly `engine.h`. The engine is written to abstract over rendering backends, but at the moment only openGL is supported. There is also a "mock" backend for testing; new rendering features should be mirrored in both `gl_engine.cpp` and `mock_gl_engine.cpp`.

  - Polyscope shaders use a custom in-house [shader builder](https://github.com/nmwsharp/polyscope/blob/master/src/render/shader_builder.cpp), which performs string manipulation with a simple substitution language to build shaders at runtime which support optional features like slice planes, transparency, different quantity visualization policies, etc. The shaders themselves also explicitly track some metadata like what attributes and uniforms they require. Examples of base shaders can be found e.g. [here](https://github.com/nmwsharp/polyscope/blob/master/src/render/opengl/shaders/sphere_shaders.cpp), and substitution rules [here](https://github.com/nmwsharp/polyscope/blob/master/src/render/opengl/shaders/rules.cpp). For any shader or rule to be available in Polyscope, it must be registered in `GLEngine::populateDefaultShadersAndRules()`, and also in the corresponding function of the mock engine for testing.

  - If adding a new structure or quantity, be sure to make use of the [data adaptors](/data_adaptors/) for all user inputs. See [here](https://github.com/nmwsharp/polyscope/blob/master/include/polyscope/point_cloud.ipp#L9-L10) for an example. Generally, this means functions which take user data should be templated, and the input then passed through `standardizeArray<>()` or `standardizeVectorArray<>()`, etc.

  - If adding new options or parameters to a structure/quantity. Be sure to follow proper encapsulation principles (create getters & setters), and use a [persistent values](/basics/parameters/#persistent-values). [Check out](https://github.com/nmwsharp/polyscope/blob/master/include/polyscope/point_cloud.h) `PointCloud::pointColor` for a good basic example.  Also, all length-valued quantities should use [scaled values](/basics/parameters/#scaled-values) (as in `PointCloud::pointRadius`).

### Unit testing 

Whenever possible, add a [unit test](https://github.com/nmwsharp/polyscope/blob/master/test/src/basics_test.cpp) that somehow exercises any new functionality or verifies that the bug has been fixed.  Polyscope uses the [googletest](https://github.com/google/googletest) testing framework. See documentation there for test macros, executable options, etc.

In a perfect world, we would actually test that the rendered output from Polyscope is pixel-perfect. However, this is hard for a lot of reasons, so instead most of our tests are just "smoke tests" that call functions with some dummy data and ensure no errors are thrown.

In fact, these tests are often run on headless servers, where we cannot even initialize an openGL environment. For this reason, in addition to the usual `openGL` [backend](/building/#backends), we also have an `openGL_mock` backend ([implemented here](https://github.com/nmwsharp/polyscope/blob/master/src/render/mock_opengl/mock_gl_engine.cpp)) for testing on headless servers. This backend cannot actually render anything, but still performs many rendering-related sanity checks.  If making changes to the rendering engine & shaders, you may find that changes need to be mirrored in `mock_gl_engine.cpp`.

To run unit tests locally on your own machine (here, via unix terminal commands), use

```sh
cd test
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Debug ..
make -j4 
./bin/polyscope-test backend=openGL3_glfw
```

which should create a window onscreen and run tests for a few seconds.

**Additionally**, run the tests again like

```sh
./bin/polyscope-test 
```

which will use the `openGL_mock` backend (you will not see anything onscreen). This is how testing will be performed on the headless CI servers. If both sets of tests pass without errors, you are good to go.

### PRs & automated tests
  
Once your feature seems ready and unit tests are passing, submit a pull request to the [main repository](https://github.com/nmwsharp/polyscope). This will trigger continuous integration (CI) tests via Github Actions to automatically compile the code on a collection of windows/mac/linux machines with various compilers, and verify that tests pass. If there are any issues, a failed "check" will show on the pull request page which you can click to learn more.

If this is your first contribution to Polyscope, a maintainer will need to manually approve the CI run (this is a github restriction).

You are welcome to reach out in the PR chat to sort out any problems. We may request changes! If a PR ever goes more than a few days without a response feel free to ping @nmwsharp.

### Documentation

Documentation is hosted in its own [separate repository](https://github.com/nmwsharp/polyscope-docs). Polyscope docs use the [mkdocs](https://www.mkdocs.org/) documentation engine, with the [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) theme (this theme is quite large and adds significant functionality beyond base mkdocs). The documentation is written in a large collection of markdown files; it is _not_ automatically scraped from the code, or code comments, etc, so we must manually keep it up to date.

There are two duplicate copies of all the docs for C++ and Python, stored in parallel directories `/cpp` and `/py`. A few shared files and assets are stored in the `/shared` directory, or symlinked from the `/py` subdirectory to point to a file the `/cpp` directory. We try to keep these two parallel versions in sync as much as possible, only differing where necessary between C++ and Python.

To preview the documentation while editing, first install the necessary packages with `pip install mkdocs mkdocs-material==6.2.8 mkdocs-macros-plugin pygments`. Then run `python3 -m mkdocs serve` (run this command from the `/cpp` directory to view C++ docs, and likewise for `/py`). A local address will be printed to your terminal, which you can navigate to in-browser to see the docs.

Hopefully editing the docs markdown files should be self-evident, you can mainly copy existing content & formatting. Any new files need to be added the manifests in `mkdocs.yml`.  Don't forget to add a blurb to the [release notes](../release_notes)! 

If you are not able to build the docs for any reason, it is fine to just edit the markdown files and submit a docs PR with that.

To actually update the hosted documentation files online at polyscope.run, the documentation site needs to be recompiled and committed to the to the `/docs` subdirectory. The `build_commit_push.sh` script can handle this for you, rebuilding both C++ & Python docs and committing the result to the `/docs` subdirectory:

```sh
sh build_commit_push.sh
```

If you include these built docs changes in your PR, the webpage will automatically update when it is merged. Otherwise the maintainers (usually @nmwsharp) will need to run this command and commit the update after accepting your PR.


### Python bindings

Python bindings for Polyscope are stored in their own [separate repository](https://github.com/nmwsharp/polyscope-py). We use [nanobind](https://nanobind.readthedocs.io/en/latest/index.html) to generate bindings. These bindings are kept as thin wrappers as much as possible, just doing a minimal translation between the C++ interface and typical Python calling conventions.

The bindings are actually managed internally as two separate Python packages: `polyscope_bindings` (which contains the raw bindings generated by our nanobind code), and the higher-level `polyscope` (which contains the actual, nice user-facing Python functions). The separation is because there is no way to write additional Python code in the nanobind-generated package, but we often want to do some translation and error checking on the Python side before invoking the bindings. As such, adding a binding generally means writing code in two places:

  1. Add a new nanobind C++ binding, like those [here](https://github.com/nmwsharp/polyscope-py/tree/master/src/cpp)
  2. Add a new Python wrapper function which calls the generated binding, like the ones [here](https://github.com/nmwsharp/polyscope-py/tree/master/src/polyscope)

Note that a few stylistic conventions between Python and C++. In particular, we do not expose classes for quantities, but set options via optional keyword arguments when the quantity is added. The nanobind C++ bindings take Eigen arrays as arguments, because nanobind performs automatic translation between Eigen/numpy.

Python binding unit tests are stored in `/test/polyscope_test.py`. As with C++, these are mainly just simple "smoke tests" which call the functions with dummy data and ensure no errors are thrown. All new bindings functions need a test! To build and test the bindings, first compile the bindings from the `polyscope-py` root directory like
```sh
mkdir build
cd build
cmake ..
make -j8
```
the run `python polyscope_test.py`. As you write code, these bindings must be recompiled to reflect any changes to the nanobind C++. When testing, make sure there is not another copy of Polyscope for Python installed in your system, which might unintentionally be used instead of the development version! Also, the adjacent `demo_app.py` can be used for simple testing.

Don't forget, the Python bindings have a parallel set of docs in the `/py` [directory](https://github.com/nmwsharp/polyscope-docs/tree/master/docs/py). Updates to Python should be reflected there.

When all your tests are passing, create a pull request! As with C++, submitting a pull request to the Python bindings will trigger a cloud build and some automated checks.

Actually deploying a new Python version to `pip` and `conda` package managers is a somewhat significant process, so we typically group together updates before cutting a new version.  Ping @nmwsharp to get a new version deployed.  Major and minor versions of the Python library are kept in-sync with the C++ library versions, whereas patch versions (`1.2.4` --> `1.2.5`) are used for new updates to the Python bindings only.



