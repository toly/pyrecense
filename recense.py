#!/usr/bin/env python
# coding: utf-8
__author__ = 'toly'

import sys
import argparse


def main():
    """
        entry point
    """
    arg_parser = create_argparser()
    args = arg_parser.parse_args()




def create_argparser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-d', '--project-directory', type=str, help="Project directory for recense", required=True)
    return arg_parser


if __name__ == '__main__':
    sys.exit(main())