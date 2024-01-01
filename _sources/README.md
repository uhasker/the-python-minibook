# The Python Minibook

## What is this?

This is the repository for the book "The Python Minibook", a book about Python aimed primarily at beginners.

The live version of the book is [here](https://uhasker.github.io/the-python-minibook).

## Progress

Chapters on the following topics are currently planned:

- [x] Fundementals
- [x] Variables, Data Types and Operators
- [x] Functions
- [x] Classes
- [x] Iterables
- [x] Control Flow
- [x] Input and Output
- [x] Exceptions
- [x] Modules and Packages
- [x] The Project

The first draft of the book is completed and the book is currently in **alpha stage**, i.e. you can read it, but expect some minor mistakes.

## Contributing

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
