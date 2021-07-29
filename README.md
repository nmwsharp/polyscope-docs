# polyscope-docs
Documentation for polyscope


Managed using mkdocs.

To install mkdocs and theme:
```
pip install mkdocs mkdocs-material==6.2.8 pygments
```

NOTE: mkdocs-material 7.0 seems to have changed some html that breaks our custom header. Until we unbreak this, use the last 6.0 version (6.2.8)

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
