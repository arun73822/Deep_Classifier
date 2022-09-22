from encodings import utf_8
import setuptools

with open("README.md","r",encoding="utf_8") as f:
    LONG_DESCRIPTION=f.read()

__VERSION__="0.0.0"

REPO_NAME="Deep_Classifier"
AUTHOR_USER_NAME="arun73822"
SRC_REPO="deep_classifier"
AUTHOR_EMAIL="arun73822@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__VERSION__,
    description="A Small Python Package for CNN application",
    long_description=LONG_DESCRIPTION,
    lonng_description_content="text/markdown",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
