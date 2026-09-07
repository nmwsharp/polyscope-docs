# polyscope-docs
Documentation for polyscope

To contribute, check out the [instructions here](https://polyscope.run/about/contributing/).

The underlying docs engine is mkdocs and mkdocs-material stack. 


### Building the docs locally

The easiest way to install the dependencies and run the build is with [uv](https://docs.astral.sh/uv/) — install it once with `curl -LsSf https://astral.sh/uv/install.sh | sh`. Package versions are pinned in `uv.lock`.

E.g. to preview locally, run from the `cpp/` or `py/` directory:
```
uv run mkdocs serve
```

NOTE: versions of mkdocs packages are pinned because new releases (esp. mkdocs-material) break our docs fairly often, in part because of our custom-overridden html. When bumping versions, make sure nothing breaks.

### Deploying new versions

To build and deploy (from the repo root):
```
./build_commit_push.sh
```
this internally invokes the build commands and pushes to the hosting repo. The gnomes will promptly get to work building the website, and content at polyscope.run will update in a few minutes.
