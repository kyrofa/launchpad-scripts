from setuptools import setup, find_packages
setup(
    name='cla-check',
    version='0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cla-check = cla_check.__main__:run',
        ],
    },
)
