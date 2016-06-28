try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    'description': 'My project',
    'author': 'Being Chen',
    'url': 'TBD',
    'download_url': 'TBD',
    'author_email': 'kingcb@qq.com',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['Lesson47'],
    'scripts': [],
    'name': 'Lesson47'
}

setup(**config)
