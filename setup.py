from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class my_build_ext(build_ext):
    def build_extensions(self):
        if self.compiler.compiler_type == 'unix':
            for e in self.extensions:
                e.extra_compile_args = ['-msse4.2', '-mavx2']

        build_ext.build_extensions(self)

    def finalize_options(self):
        build_ext.finalize_options(self)
        __builtins__.__NUMPY_SETUP__ = False
        import numpy
        self.include_dirs.append(numpy.get_include())

ext_modules = [
    Extension('mysample.sample',
        ['mysample/sample.pyx',
         "src/sample.cpp"],
        language='c++',
        include_dirs = ["src"]),
]

setup(
    name='ty_github-actions-sample',
    version='0.0.7',
    packages=['mysample'],
    ext_modules=ext_modules,
    cmdclass={'build_ext': my_build_ext},
    author='Tadao Yamaoka',
    url='https://github.com/TadaoYamaoka/github-actions-sample',
    description = 'github-actions-sample',
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License (GPL)',
        "Operating System :: OS Independent",
    ],
)