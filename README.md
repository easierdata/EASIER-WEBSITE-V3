## **EASIER-WEBSITE-V3**

The EASIER Data Initiative Website

---

## Install Prerequisites

You can install all necessary libraries through the following command in the root directory.

```bash
$ pip install -r requirements.txt
```

## Running locally

To view the website locally, run the following command in the root directory (it should automatically open up localhost in a browser)

```bash
$ ablog clean && ablog build && ablog serve
```

## Deploying to Netlify

Edit Netlify project settings to point to this repository, and set the build command to `make html`. Set the build directory to `_build/html`.

### Notes

1.  Built with Python 3