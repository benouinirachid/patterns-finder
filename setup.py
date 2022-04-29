import pathlib
from setuptools import setup
from setuptools import find_packages

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")
description = "A patterns finder by regex."
install_requires = ["regex"]
setup_requires = []
tests_require = []


setup(
    name="Patterns Finder",
    version="0.0.1",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
    ],
    description=description,
    long_description=long_description,
    url="https://github.com/benouinirachid/patterns-finder",
    author="Rachid Benouini",
    keywords="regex",
    author_email="benouini.rachid@gmail.com",
    license="Apache License 2.0",
    install_requires=install_requires,
    setup_requires=setup_requires,
    test_suite="tests",
    include_package_data=True,
    tests_require=tests_require,
    packages=find_packages(),
    zip_safe=False,
)
