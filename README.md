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
                        Choose your verbosity. Default: DEBUG
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

### Create and install a package

```console
user@computer:$ pyckage my_super_package
user@computer:$ pip install -e ./my_super_package
Obtaining file:///home/my_super_package
Installing collected packages: my-super-package
  Running setup.py develop for my-super-package
Successfully installed my-super-package
```

### Use the package from command-line

```
user@computer$: my_super_package -h
usage: my_super_package [-h] [--verbosity {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [--progress_bar]

optional arguments:
  -h, --help            show this help message and exit
  --verbosity {DEBUG,INFO,WARNING,ERROR,CRITICAL}, -v {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Choose your verbosity. Default: INFO
  --progress_bar, -p    Displays a progress bar
```

### Import your package from python and locate its resources

Each created package contains a constant variable that refers to the emplacement of its resources: 

```python
import mysuperpackage
print(mysuperpackage.RESOURCES_DIR)
```

### Build, modify your package

``` console
user@computer:$ tree my_super_package/
my_super_package/
my_super_package/
├── LICENSE.txt # Change with whatever license you want
├── METADATA.in
├── my_super_package # Your independent modules goes in this subdirectory
│   ├── app_module1.py # Replace with your own module name
    # Add your different modules here
│   ├── __init__.py # Import all your modules here
│   ├── launchers # Your CLI programs
│   │   ├── __init__.py # Don't forget to add additional launcher programs if there is any
│   │   └── my_super_package_launcher.py # Parses arguments 
            # By default, launches app_module1.appfunction_of_module1(). Change with whatever you want
│   └── resources # Put your resources here (Images, HTML, etc)
│       └── EMPTY
├── README.md # Markdown README
└── setup.py # You can add new launchers if you specify them from here

6 directories, 18 files
```

### Upload your package on PyPI

#### This requires twine (usually already installed)

```console
user@computer:$ pip install --update twine
```

#### Then you can make a distribution, and upload it on test PyPI:

```console
user@computer:$ cd my_super_package
user@computer:$ python setup.py sdist bdist_wheel
user@computer$: twine upload -r testpypi dist/* 
username: ...
password:
...
```

See [Here](https://twine.readthedocs.io/en/latest/) to upload on the real PyPI once you're ready

# Requirements

Python >=3.7

# Credits

DELEVOYE Guillaume - 2021
delevoye.guillaume@gmail.com

# License


See "License" for more infos
