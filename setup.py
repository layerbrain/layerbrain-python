from setuptools import setup, find_packages

setup(
    name="layerbrain",  # The name of your package on PyPI
    version="0.1.0",
    author="Layerbrain",
    author_email="support@layerbrain.com",
    description="Python library for interacting with the Layerbrain API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/layerbrain/layerbrain-python",  # Replace with the correct GitHub repo
    packages=find_packages(),  # Finds the layerbrain package in the current directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
