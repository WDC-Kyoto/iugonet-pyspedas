import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iugonet_wdc",
    version="0.1.0",
    author="WDC, Kyoto",
    author_email="koike@kugi.kyoto-u.ac.jp",
    description="This is a pySPEDAS package for loading geomagnetic data from World Data Center for Geomagnetism, Kyoto.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WDC-Kyoto/iugonet-pyspedas",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['']
    },
    install_requires = [
        'pyspedas'
    ],
    python_requires='>=3.7',
)
