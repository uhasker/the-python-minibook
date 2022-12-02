# The Python minibook

This repository contains the files for "The Python minibook".

The live version of the book is [here](https://uhasker.github.io/the-python-minibook).

## Useful commands

Clear all notebooks:

```sh
find . -maxdepth 1 -type f -name "*.ipynb" -exec jupyter nbconvert --clear-output --inplace {} \;
```
