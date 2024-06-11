from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    description='sample package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cc/',  # Ensure this is correct or provide an actual link
    author='cc',
    author_email='cc@42.fr',
    license='MIT',
    packages=find_packages(),
)
