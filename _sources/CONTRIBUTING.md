# Contributing

## Setup

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

## Guidelines

### Commits

Please adhere to https://www.conventionalcommits.org/en/v1.0.0/ when writing commit messages.

If you are working on a particular chapter the scope should always be of the form `C1`. For example if you make some minor improvements in chapter 1, your commit message should look like this:

```
chore(C1): minor improvements
```

### Branches

Branch names should be `lisp-case` and should start with the chapter name the feature of fix applies to.

For example if you fix a typo in Chapter 1, the branch name should be `c-01-fix-typo`.

### Pull Requests

Don't forget to clear all notebooks before creating a PR, otherwise your code cell outputs will be included in the PR, which you don't want:

```sh
find src -type f -name "*.ipynb" -exec jupyter nbconvert --clear-output --inplace {} \;
```
