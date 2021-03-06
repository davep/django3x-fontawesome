import os
from setuptools  import setup
from fontawesome import __version__

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django3x-fontawesome',
    version=__version__,
    packages=['fontawesome'],
    include_package_data=True,
    license='BSD License',
    description='a django app that provides a couple of fontawesome/django related utilities.',
    long_description=README,
    url='https://github.com/davep/django3x-fontawesome',
    author='Redouane Zait',
    author_email='redouanezait@gmail.com',
    install_requires=['PyYAML'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
)
