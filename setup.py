from setuptools import setup

setup(name='df_fuzzy_merge',
      version='1.0',
      description='fuzzy merges two dataframes',
      url='https://lamplightlab.com',
      author='Matthew McElhaney',
      author_email='matt@lamplightlab.com',
      license='MIT',
      packages=['df_fuzzy_merge'],
      install_requires=['nltk', 'fuzzywuzzy', 'pandas', 'python-Levenshtein'],
      zip_safe=False)
