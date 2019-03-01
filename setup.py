import setuptools


def get_long_description():
    with open("README.md", "r") as readme:
        return readme.read()


setuptools.setup(
    name="pyduinocli",
    version="0.0.1",
    author="Renaud Gaspard",
    author_email="gaspardrenaud@hotmail.com",
    description="Wrapper library around arduino-cli",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://gitlab.com/Renaud11232/pyduino_cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
