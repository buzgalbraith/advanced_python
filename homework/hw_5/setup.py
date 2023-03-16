from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "solve_heat_equation_1_1",
    ext_modules = cythonize('solve_heat_equation_1_1.pyx'),
)
