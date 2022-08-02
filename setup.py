from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in building_block_vechicle_management/__init__.py
from building_block_vechicle_management import __version__ as version

setup(
	name="building_block_vechicle_management",
	version=version,
	description="Building Block Vehicle Management",
	author="Thirvusoft",
	author_email="info@thirvusoft.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
