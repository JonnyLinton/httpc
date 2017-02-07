from setuptools import setup

setup(
    name='httpc',
    py_modules=['httpc', 'lab_assignment1'],
    install_requires=[
        'docopt',
    ],
    entry_points='''
        [console_scripts]
        httpc=httpc:run
    ''',
)
