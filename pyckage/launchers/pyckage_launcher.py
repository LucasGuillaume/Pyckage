#!/usr/bin/env python

import pyckage
import argparse
import os
import sys
import logging

import datetime

import os


def main():

    LAUNCHER_DIR = os.path.join(os.path.dirname(__file__))
    PYCKAGE_RESOURCES_DIR = os.path.join(os.path.abspath(os.path.join(LAUNCHER_DIR,os.pardir)),"resources")


    parser = argparse.ArgumentParser(description='Creates the boilerplate of a python package in the current directory.')

    parser.add_argument('--verbosity',"-v",
                            help='Choose your verbosity. Default: INFO',
                            required=False,
                            default="DEBUG",
                            choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])

    parser.add_argument('name',
                            help='Package name. Must be a valid python variable name',
                            type=str)

    parser.add_argument('--version',
                            help='Initial version (DEFAULT: 0.1)',
                            required=False,
                            type=str)

    parser.add_argument('--year',"-y",
                            help='Choose your verbosity. Default: current year',
                            required=False,
                            type=int,
                            default=    datetime.datetime.now().year)

    parser.add_argument('--author',"-a",
                            help='Author name',
                            required=False,
                            default="None",
                            type=str)

    parser.add_argument('--email',"-e",
                            help='Your email address',
                            default="None",
                            required=False,
                            type=str)

    parser.add_argument('--description',"-d",
                            help='Project description (short)',
                            required=False,
                            default="Enter your project description here (short)",
                            type=str)

    parser.add_argument('--long_description',"-l",
                            help='Project description (long)',
                            default = "Enter your project description here (long)",
                            required=False,
                            type=str)

    parser.add_argument('--URL',"-u",
                            help="Project's URL",
                            required=False,
                            default="None",
                            type=str)

    parser.add_argument('--requirements',"-r",
                            help="pip requirements, as a python list between quotes. Exemple : \"[python>=3.7,tqdm]\". Default = '[python>=3.7]'",
                            required=False,
                            type=str,
                            default="[python>=3.7]")

    args = parser.parse_args()


    verboselevel = "logging."+str(args.verbosity)
    logging.basicConfig(level=eval(verboselevel),
                        format='%(asctime)s %(message)s',
                        stream=sys.stdout)


    pyckage.only_module.transform(loglevel = verboselevel, resources = PYCKAGE_RESOURCES_DIR, args = vars(args))

if __name__ == "__main__":
    main()
