from setuptools import setup

import versioneer

with open('README.md') as f:
    readme = f.read()

setup(
    name='goldensphinx',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    long_description=readme,
    packages=['goldensphinx'],
    url='https://github.com/yoavram/goldensphinx',
    license='MIT',
    author='Yoav Ram',
    author_email='yoav@yoavram.com',
    description='Build and serve Sphinx',
    install_requires=[
        'click>=5'
        'sphinx>=1.3.0',
        'numpydoc',
        'sphinx_rtd_theme',
        'static',
        'gevent>=0.13.6',
        'greenlet>=0.3.1',
        'gunicorn>=0.13.4',
        'static>=0.4'
    ],
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            'goldensphinx=goldensphinx.cli:cli',
        ],
    }, 
)

