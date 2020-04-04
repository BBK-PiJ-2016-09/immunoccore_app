from setuptools import setup, find_packages

setup(
    name='immunocore',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'Django',
        'factory-boy',
        'djangorestframework',
        'coreapi',
	'psycopg2-binary',
    ],
    tests_require=[
        'factory-boy',
    ],
    test_suite='nose.collector',
    license='',

    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Dev/Ops',
        'Topic :: Software Development :: Test',

        # Pick your license as you wish (should match "license" above)
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='django app',
    author='Enric Serra Sanz',
    author_email='enricserrasanz@gmail.com',
    description='A very basic django app'
)
