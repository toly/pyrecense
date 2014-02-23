#!/usr/bin/env python
# coding: utf-8
__author__ = 'toly'

import re
import os
import sys
import argparse
from collections import Counter


BAD_FUNCTIONS = ['__init__', '__unicode__', 'setUp', 'tearDown']

FUNCTION_DEFINE_REGEXP = re.compile(r'def (\w+)\(')
FUNCTION_CALL_REGEXP = re.compile(r'(\w+)\(')


def main():
    """
        entry point
    """
    arg_parser = create_argparser()
    args = arg_parser.parse_args()

    functions_definitions = []
    functions_calls = []

    project_files = get_python_files(args.project_directory)
    for file_index, filename in enumerate(project_files):
        for line in get_file_lines(filename):
            # getting functions, classes and their calls
            definitions = [function_name for function_name in FUNCTION_DEFINE_REGEXP.findall(line)]
            if definitions:
                has_bad_functions = False

                for bad_function in BAD_FUNCTIONS:
                    if bad_function in definitions:
                        has_bad_functions = True

                if has_bad_functions:
                    continue

                functions_definitions += definitions
                continue

            calls = [function_name for function_name in FUNCTION_CALL_REGEXP.findall(line)]
            if calls:
                functions_calls += calls

    # prepare and output statistics
    definitions_counter = Counter(functions_definitions)
    definitions_set = set(functions_definitions)

    definitions_tuples = definitions_counter.items()
    definitions_tuples = [(definition, count) for
                          (definition, count) in definitions_tuples
                          if count != 1]
    definitions_tuples.sort(key=lambda (function_definition, count_definition): -count_definition)

    print '\nrepited definitons:'
    for definition, count in definitions_tuples:
        print '   %s: %d' % (definition, count)

    calls_tuples = Counter(functions_calls).items()
    calls_tuples = [(call, count) for
                    (call, count) in calls_tuples
                    if call in definitions_set and count < 5]
    calls_tuples.sort(key=lambda (function_call, count_call): count_call)

    print '\nsmall used functions:'
    for call, count in calls_tuples:
        print '    %s: %d' % (call, count)


def get_python_files(folder):
    """
        return full paths of python files in <folder>
    """
    fullpath = os.path.abspath(folder)
    for (dirpath, dirnames, filenames) in os.walk(fullpath):
        for filename in filenames:
            if filename[-3:] != '.py':
                continue
            if filename.endswith('admin.py'):
                continue
            if 'migrations' in dirpath:
                continue
            yield os.path.join(dirpath, filename)


def get_file_lines(filename):
    """
        generator lines from file
    """
    with open(filename) as f:
        for line in f:
            yield line


def create_argparser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-d', '--project-directory', type=str, help="Project directory for recense", required=True)
    return arg_parser


if __name__ == '__main__':
    sys.exit(main())