Package Sample ReadMe

Details to run:

Clean Previous Builds:
rm -rf build dist ft_package.egg-info

pip install wheel  # If you haven't installed it already

Build the Package:
python setup.py sdist bdist_wheel

Install the Package:
pip install ./dist/ft_package-0.0.1-py3-none-any.whl

Run tester.py:
python tester.py

