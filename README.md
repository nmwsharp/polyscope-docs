# polyscope-docs
Documentation for polyscope

To contribute, check out the [instructions here](https://polyscope.run/about/contributing/).

Managed using mkdocs.

To install mkdocs and theme:
```
pip install mkdocs==1.4.2 mkdocs-material==9.0.13 mkdocs-macros-plugin==0.7.0 pygments 
```

NOTE: the versions of mkdocs things are pinned above. New versions (esp. for mkdocs-material) break our docs fairly often, in part because of our custom-overridden html. When bumping these versions, make sure nothing breaks.

To preview locally:
```
python3 -m mkdocs serve
```

To build and deploy:
```
python3 -m mkdocs build
git add docs/
git commit
git push
```
the gnomes will promptly get to work building the website, and content at polyscope.run will update in a few minutes.
