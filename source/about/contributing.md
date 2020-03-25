Polyscope is an open-source project, and you are encouraged to contribute!

A few high-level guidelines:

  - All contributions must be released under Polyscope's MIT license.

  - Significant new features need to be documented! This documentation lives in [polyscope-docs](https://github.com/nmwsharp/polyscope-docs). You can and should submit a request there at the same time as adding code to Polyscope.
    - The documentation uses markdown. Modifying the docs amounts to editing a source file and rebuilding the site source. The the nodes there in `README.md`.
    - To add a new page to the documentation, edit `mkdocs.yml`.

  - If adding a new structure or quantity, be sure to make use of the [data adaptors](../../data_adaptors/) for all user inputs. See `point_cloud.h` for an example.

  - Be sure to run the unit tests (see [building](/building)), and add tests for any new features.

  - Add a blurb to the [release notes](../release_notes)!


We'll expand these guidelines as Polyscope grows.
