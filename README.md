# Pyckage

Quick boilerplate for a new python package

# Description

Project URL : <https://github.com/LucasGuillaume/Pyckage>

# Installation

```console
user@computer:$ git clone https://github.com/LucasGuillaume/Pyckage
user@computer:$ pip install -e ./Pyckage
```

# Usage

```console
user@computer:$ pyckage -h
usage: pyckage [-h] [--verbosity {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [--version VERSION] [--year YEAR] [--author AUTHOR] [--email EMAIL] [--description DESCRIPTION] [--long_description LONG_DESCRIPTION]
               [--URL URL] --requirements REQUIREMENTS
               name

Creates the boilerplate of a python package in the current directory.

positional arguments:
  name                  Package name

optional arguments:
  -h, --help            show this help message and exit
  --verbosity {DEBUG,INFO,WARNING,ERROR,CRITICAL}, -v {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Choose your verbosity. Default: INFO
  --version VERSION     Initial version (DEFAULT: 0.1)
  --year YEAR, -y YEAR  Choose your verbosity. Default: current year
  --author AUTHOR, -a AUTHOR
                        Author name
  --email EMAIL, -e EMAIL
                        Your email address
  --description DESCRIPTION, -d DESCRIPTION
                        Project description (short)
  --long_description LONG_DESCRIPTION, -l LONG_DESCRIPTION
                        Project description (long)
  --URL URL, -u URL     Project's URL
  --requirements REQUIREMENTS, -r REQUIREMENTS
                        pip requirements, as a python list between quotes. Exemple : "[python>=3.7,tqdm]"


```

# Requirements

Pure python.

# Credits

DELEVOYE Guillaume - 2021
delevoye.guillaume@gmail.com

# License


See "License" for more infos
