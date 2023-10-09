# The Python minibook

This repository contains the files for "The Python minibook".

The live version of the book is [here](https://uhasker.github.io/the-python-minibook).

## Building the Book

You will need to install the requirements:

```sh
python -m pip install -r requirements.txt
```

To build the book as HTML execute the following command:

```sh
python -m jupyter book build .
```

To build the book as PDF install the `pyppeteer` package and execute the build command:

```sh
python -m pip install pyppeteer
python -m jupyter book build --builder pdfhtml .
```

To build as LaTeX you will need to install the required packages and then run the build command:

```sh
sudo apt-get install texlive-latex-extra texlive-fonts-extra texlive-xetex latexmk
python -m jupyter book build . --builder pdflatex
# OR python -m jupyter book build . --builder latex if you only want the LaTeX file
```

## Creating a Pull Request

If you find a spelling or grammar mistakes or you want to suggest an improvement, you're welcome to create a PR!

Don't forget to clear all notebooks before doing so, otherwise your code cell outputs will be included in the PR, which you don't want:

```sh
find src -type f -name "*.ipynb" -exec jupyter nbconvert --clear-output --inplace {} \;
```
