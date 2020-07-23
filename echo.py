#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Joseph Padgett with demo/study hall video"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    # your code here
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help = 'text to echo')
    parser.add_argument('-l', '--lower', action = 'store_true', help = 'transform text to lowercase')
    parser.add_argument('-u', '--upper', action = 'store_true', help = "transform text to uppercase")
    parser.add_argument('-t', '--title', action = 'store_true', help = 'transform text to titlecase')
    parser.add_argument('-tul', action = 'store_true', help = 'transfom text to titlecase, uppercase, and lowercase')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)

    if ns.lower:
        print(ns.text.lower())
    
    if ns.upper:
        print(ns.text.upper())

    if ns.title:
        print(ns.text.title())

    if ns.tul:
        print(ns.text.title().upper().lower())

    print(ns.text)

if __name__ == '__main__':
    main(sys.argv[1:])

