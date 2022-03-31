from setuptools import setup, find_namespace_packages


setup(
    name="proforma",
    packages=find_namespace_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "python = 3.9"
        "numpy = 1.22.3",
        "pandas = 1.4.1",
        "jinja2 = 3.0.3"
    ],
)
