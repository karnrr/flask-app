from setuptools import setup
from Cython.Build import cythonize

setup(
    name="flask_app",
    ext_modules=cythonize(r"app/*.py", build_dir="build", language_level=3)
)

