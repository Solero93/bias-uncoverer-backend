from setuptools import setup

setup(
    install_requires=[
        'Flask',
        'pika',
        'pymongo'
    ],
    python_requires='>=3.7'
)
