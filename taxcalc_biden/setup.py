import setuptools
import os

long_description = "placeholder"

setuptools.setup(
    name="taxcalc",
    version=os.environ.get("VERSION", "0.0.0"),
    author="Peter Metz",
    author_email="pmetzdc@gmail.com",
    description=(
        "Calculates federal tax liabilities from individual data under "
        "different policy proposals."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pslmodels/Tax-Cruncher",
    packages=setuptools.find_packages(),
    install_requires=["paramtools"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)