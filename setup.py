import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess_lvsuno',
	version = '0.0.1',
	author = 'Elvis TOGBAN',
	author_email = 'togbanelvis@yahoo.fr',
	description = 'This a preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Langage :: Python :: 3.6',
	'License :: OSI Aproved :: MIT License',
	"Operating System :: Os independent"],
	python_requires = '>=3.6')
   