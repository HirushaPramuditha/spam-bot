import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="spam-bot",
    version="0.0.2",
    author="Hirusha Pramuditha",
    author_email="hirushapramuditha26@gmail.com",
    description="Spam anything!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HirushaPramuditha/spam-bot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)
