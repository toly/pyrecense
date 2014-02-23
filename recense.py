#!/usr/bin/env python
# coding: utf-8
__author__ = 'toly'

import os
import sys
import argparse


def main():
    """
        entry point
    """
    arg_parser = create_argparser()
    args = arg_parser.parse_args()

    functions = []
    classes = []

    functions_calls = []
    classes_using = []

    project_files = get_python_files(args.project_directory)
    for file_index, filename in enumerate(project_files):
        for line in get_file_lines(filename):
            # getting functions, classes and their calls
            pass

    # output statistics


def get_python_files(folder):
    """
        return full paths of python files in <folder>
    """
    fullpath = os.path.abspath(folder)
    for (dirpath, dirnames, filenames) in os.walk(fullpath):
        for filename in filenames:
            if filename[-3:] != '.py':
                continue
            if 'migrations' in dirpath:
                continue
            yield os.path.join(dirpath, filename)


def get_file_lines(filename):
    """
        generator lines from file
    """
    pass


def create_argparser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-d', '--project-directory', type=str, help="Project directory for recense", required=True)
    return arg_parser


if __name__ == '__main__':
    sys.exit(main())