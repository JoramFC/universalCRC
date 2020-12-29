import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="universal-crc",
    version="0.8",
    author="Joram Fillol-Carlini",
    author_email="joram.fillolcarlini@laposte.net",
    description="A universal CRC (8, 16, 32 or 64) computation tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoramFC/universalCRC",
    packages=["universalCRC"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6,<4',
)