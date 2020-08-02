from setuptools import setup, find_packages

setup(
    name='dox',
    version='0.0.1',
    packages=find_packages(),
    scripts=['scripts/dox'],
    python_requires='>=3.7.0',
    install_requires=[
        line for line in open('requirements.txt', 'r').readlines()
        if line and not line.startswith('-')
    ],
    entry_points={
        'pygments.lexers': 'SylvaLexer = dox:sylva_lexer.py'
    }
)
