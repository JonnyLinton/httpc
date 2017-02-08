from setuptools import setup

setup(
    name='httpc',
    py_modules=['httpc', 'response_handler', 'http_get', 'http_post'],
    install_requires=[
        'docopt',
    ],
    entry_points='''
        [console_scripts]
        httpc=httpc:run
    ''',
)
