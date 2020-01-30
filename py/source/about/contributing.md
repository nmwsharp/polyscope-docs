Polyscope is an open-source project, and you are encouraged to contribute!

A few high-level guidelines:

  - All contributions must be released under Polyscope's MIT license.

  - Significant new features need to be documented! This documentation lives in [polyscope-docs](https://github.com/nmwsharp/polyscope-docs). You can and should submit a request there at the same time as adding code to Polyscope.
    - The documentation uses markdown. Modifying the docs amounts to editing a source file and rebuilding the site source. The the nodes there in `README.md`.
    - To add a new page to the documentation, edit `mkdocs.yml`.

  - If adding a new structure or quantity, be sure to make use of the [data adaptors](../../data_adaptors/) for all user inputs. See `point_cloud.h` for an example.

  - Due to the challenges of testing GUI code, Polyscope doesn't have many unit tests. However, the data adaptors _are_ unit-tested. If you modify them in any way, be sure to update and run the tests in `/test/`.

  - Add a blurb to the [release notes](../release_notes)!


We'll expand these guidelines as Polyscope grows.
