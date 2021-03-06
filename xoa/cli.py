#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Commandline interface for xoa
"""

import argparse

from .__init__ import (
    show_info, show_versions, show_paths, show_options)


def get_parser(formatter_class=argparse.ArgumentDefaultsHelpFormatter):

    parser = argparse.ArgumentParser(
        description="xoa interface",
        formatter_class=formatter_class)
    subparsers = parser.add_subparsers(help='sub-command help')

    parser_info = subparsers.add_parser('info', help='info about xoa')
    parser_info.add_argument('category', help='info category', nargs='?',
                             choices=('all', 'paths', 'versions', 'options'),
                             default='all')
    parser_info.set_defaults(func=main_info)

    return parser


def main(argv=None, formatter_class=argparse.ArgumentDefaultsHelpFormatter):

    parser = get_parser(formatter_class=formatter_class)
    args = parser.parse_args(argv)
    args.func(parser, args)


def main_info(parser, args):
    if args.category == "all":
        show_info()
    elif args.category == "versions":
        show_versions()
    elif args.category == "paths":
        show_paths()
    elif args.category == "options":
        show_options()
