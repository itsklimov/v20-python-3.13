# Publishing to PyPI

This document provides instructions on how to publish this package to PyPI.

## Prerequisites

1. Make sure you have the required Python packaging tools installed:
   ```
   pip install --upgrade pip build twine
   ```

2. Create an account on PyPI if you don't have one already:
   https://pypi.org/account/register/

## Building the Package

1. Navigate to the root directory of the package:
   ```
   cd /path/to/v20-python-3.13
   ```

2. Build the package:
   ```
   python -m build
   ```

   This will create both a source distribution (.tar.gz) and a wheel (.whl) in the `dist/` directory.

## Uploading to PyPI

### Testing on TestPyPI (Optional but Recommended)

1. Create an account on TestPyPI if you don't have one already:
   https://test.pypi.org/account/register/

2. Upload the package to TestPyPI:
   ```
   python -m twine upload --repository testpypi dist/*
   ```

3. Install your package from TestPyPI to verify it works:
   ```
   pip install --index-url https://test.pypi.org/simple/ v20
   ```

### Publishing to PyPI

Once you've verified the package works correctly, you can publish it to the real PyPI:

1. Upload the package to PyPI:
   ```
   python -m twine upload dist/*
   ```

2. After uploading, users can install your package with:
   ```
   pip install v20
   ```

## Updating the Package

When you want to update the package:

1. Update the version number in `setup.py`
2. Rebuild the package:
   ```
   python -m build
   ```
3. Upload to PyPI again:
   ```
   python -m twine upload dist/*
   ```

## Notes

- Make sure your package name is unique on PyPI. If "v20" is already taken, you might need to choose a different name.
- You'll need to authenticate with your PyPI credentials when uploading.
- For more details, see the official Python packaging guide: https://packaging.python.org/tutorials/packaging-projects/ 