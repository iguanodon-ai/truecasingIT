import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
	name="truecasingIT",
	version="1.0.6",
	author="Simon Hengchen",
	author_email="simon@iguanodon.ai",
	description="This package allows you to truecase Italian.",
	long_description = long_description,
	long_description_content_type = "text/markdown",
    url = "https://github.com/iguanodon-ai/truecasingIT",
	classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages = setuptools.find_packages(where="."),
    python_requires = ">=3.6",
    include_package_data=True
)