#!/bin/sh

jupyter nbconvert --to html --output-dir=docs ipynb/*.ipynb
python scripts/postprocess.py
