#!/bin/sh
cd cpp
python -m mkdocs build
cd ..
cd py
python -m mkdocs build
cd ..
#git rm -rf docs/*
rm -rf docs/*
cp CNAME docs/
cp -r cpp/site_build/* docs/
cp -r py/site_build docs/py/
git add docs/
git commit -m "rebuild"
git push
