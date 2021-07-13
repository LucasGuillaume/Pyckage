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

Détails : 

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

# Example

```console
user@computer:$ pyckage my_super_package
user@computer:$ pip install -e ./my_super_package
Obtaining file:///home/my_super_package
Installing collected packages: my-super-package
  Running setup.py develop for my-super-package
Successfully installed my-super-package
user@computer$: my_super_package -h
usage: my_super_package [-h] [--verbosity {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [--progress_bar]

optional arguments:
  -h, --help            show this help message and exit
  --verbosity {DEBUG,INFO,WARNING,ERROR,CRITICAL}, -v {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Choose your verbosity. Default: INFO
  --progress_bar, -p    Displays a progress bar
user@computer:$ tree my_super_package/
my_super_package/
├── LICENSE.txt
├── METADATA.in
├── my_super_package
│   ├── app_module1.py
│   ├── __init__.py
│   ├── launchers
│   │   ├── __init__.py
│   │   ├── my_super_package_launcher.py
│   │   └── __pycache__
│   │       ├── __init__.cpython-38.pyc
│   │       └── my_super_package_launcher.cpython-38.pyc
│   ├── __pycache__
│   │   ├── app_module1.cpython-38.pyc
│   │   └── __init__.cpython-38.pyc
│   └── resources
│       └── EMPTY
├── my_super_package.egg-info
│   ├── dependency_links.txt
│   ├── entry_points.txt
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   └── top_level.txt
├── README.md
└── setup.py

6 directories, 18 files

```

# Tip for the resources dir

Each created package contains a constant variable that refers to the emplacement of its resources: 

```python
import mysuperpackage
print(mysuperpackage.RESOURCES_DIR)
```

# Requirements

Pure python.

# Credits

DELEVOYE Guillaume - 2021
delevoye.guillaume@gmail.com

# License


See "License" for more infos
