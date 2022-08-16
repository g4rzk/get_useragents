from distutils.core import setup, Extension

with open("README", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = "get_useragents",
  packages = ["get_useragents"],
  version = "0.1",
  license ="MIT",
  description = "This library is used to make it easier for developers or users to get random user agents from https://useragents.io.",
  long_description = long_description,
  author = "Angga Kurniawan",
  author_email = "g4rzkurniawan@gmail.com",
  url = "https://github.com/g4rzk/get_useragents",
  download_url = "https://github.com/g4rzk/get_useragents/archive/get_useragents_v01.tar.gz", 
  keywords = ["get useragents", "get-useragents", "useragent random"], 
  install_requires = [
          "requests",
          "bs4", 
      ],
  classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
  ],
)
