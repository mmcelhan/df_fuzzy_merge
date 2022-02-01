import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="df_fuzzy_merge",
    version="0.0.4",
    install_requires=['pandas','python-Levenshtein','fuzzywuzzy','ntlk'],
    author="Matthew McElhaney",
    author_email="matt@lamplightlab.com",
    description="Package that fuzzy merges two dataframes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mmcelhan/df_fuzzy_merge",
    project_urls={
        "blog post": "https://lamplightlab.com/2022/01/12/dataframe-fuzzy-matching/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)