from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    page_description = f.read()

with open("requirements.txt", 'r') as f:
    requirements = f.read().splitlines()

setup(
    name="kalinvolution",
    version="0.0.1",
    author="Wallace Rocha - Kalingth",
    author_email="wallace13@hotmail.com.br",
    description="Um breve estudo sobre convoluções",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kalingth/Kalinvolution",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8"
)