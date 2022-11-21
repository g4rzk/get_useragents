from distutils.core import setup, Extension

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setup(
	name = "get_useragents",
	packages = ["get_useragents"],
	version = "0.8",
	license ="MIT",
	description = "This library is used to make it easier for developers or users to get random user agents",
	long_description = long_description,
	long_description_content_type = "text/markdown", 
	author = "Angga Kurniawan",
	author_email = "g4rzkurniawan@gmail.com",
	url = "https://github.com/g4rzk/get_useragents",
	download_url = "https://github.com/g4rzk/get_useragents/archive/get_useragents.tar.gz", 
	keywords = [
		"get_useragents", 
		"get-useragents", 
		"useragent random", 
		"fake-useragent", 
		"user-agent"
	], 
	install_requires = [
		"bs4==0.0.1",
		"requests==2.28.1", 
		"cloudscraper==1.2.65", 
	],
	classifiers = [
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Build Tools",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3.10",
	],
)