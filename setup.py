from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='blenderfoam',
    version='0.0.1',
    author='Nathan A. Rooy',
    author_email='nathanrooy@gmail.com',
    url='https://github.com/nathanrooy/BlenderFOAM',
    description='Fluid based shape optimization: Blender + OpenFOAM',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['blenderfoam'],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    entry_points={
        'console_scripts': [
            'blenderFoam = blenderfoam.blenderfoam_main:main'
        ]
    }
)
