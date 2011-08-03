from setuptools import setup, find_packages

setup(
    name = "django-twitter-roulette",
    version = "1.0",
    url = 'https://github.com/ixc/django-colorfield',
    license = 'BSD',
    description = "An app driving a twitter roulette game",
    author = 'Chris Sinchok',
    packages = find_packages('roulette'),
    package_dir = {'django-twitter-roulette': 'roulette'},
    install_requires = ['setuptools'],
)