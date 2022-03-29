from setuptools import setup, find_namespace_packages


setup(
    name="proforma",
    packages=find_namespace_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # Add any requirements here, in `requirements.txt` format.
        # e.g.,
        # "bozo ==1.2.3",
    ],
)
