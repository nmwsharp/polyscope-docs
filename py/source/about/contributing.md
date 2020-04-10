Polyscope is an open-source project, and you are encouraged to contribute!

Polyscope is first and foremost a C++ library; this Python bindings are just wrappers. Any significant new features should first be implemented in C++, then wrapped in Python.

A few high-level guidelines:

  - All contributions must be released under Polyscope's MIT license.

  - Significant new features need to be documented! This documentation lives in [polyscope-docs](https://github.com/nmwsharp/polyscope-docs). You can and should submit a request there at the same time as adding code to Polyscope.
    - The documentation uses markdown. Modifying the docs amounts to editing a source file and rebuilding the site source. The the nodes there in `README.md`.
    - To add a new page to the documentation, edit `mkdocs.yml`.

  - Be sure to run the unit tests and add tests for any new features.

  - Add a blurb to the [release notes](../release_notes)!


We'll expand these guidelines as Polyscope grows.
