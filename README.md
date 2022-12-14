# The Python minibook

This repository contains the files for "The Python minibook".

The live version of the book is [here](https://uhasker.github.io/the-python-minibook).

## Useful commands

Clear all notebooks:

```sh
find src -type f -name "*.ipynb" -exec jupyter nbconvert --clear-output --inplace {} \;
```

Build the book as HTML:

```sh
pip install -r requirements.txt
jupyter-book build .
```

Build the book as PDF:

```sh
jupyter-book build --builder pdfhtml .
```

### TeX build

Install required packages:

```sh
sudo apt-get install texlive-latex-extra \
                     texlive-fonts-extra \
                     texlive-xetex latexmk
```

Build the book:

```sh
jupyter-book build . --builder pdflatex
```

To generate only the LaTeX file:

```
jupyter-book build . --builder latex
```
