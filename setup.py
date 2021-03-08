import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="obis-laser-controller",
    version="0.0.1",
    author="Brian Carlsen",
    author_email="carlsen.bri@gmail.com",
    description="Controller for OBIS Lasers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Development Status :: 3 - Alpha"
    ],
    install_requires=[
        'easy_scpi>=0.0.9'
    ],
    package_data={
    }
)