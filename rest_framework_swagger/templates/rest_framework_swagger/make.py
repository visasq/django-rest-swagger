#!/usr/bin/env python
# coding=utf-8


import argparse
import os.path
import re


PROJ_NAME = 'rest_framework_swagger'


parser = argparse.ArgumentParser()
parser.add_argument('--dry-run', action='store_true')

argns = parser.parse_args()


def repl(m):
    quote = m.group(2)
    if quote == '"':
        assert(m.group(4) == '"')

    name = m.group(1)
    url = m.group(3)

    static = '{{% static "{}/{}" %}}'.format(PROJ_NAME, url)
    return '{}={}{}{}'.format(name, quote, static, quote)


here = os.path.dirname(__file__)

with open(os.path.join(here, '../../static/rest_framework_swagger/index.html')) as index_file:
    index_content = index_file.read()
    index2_content = re.sub(r'\b(href|src)\s*=\s*([\'"])(.*?)([\'"])',
                            repl,
                            index_content)

    if argns.dry_run:
        print(index2_content)
    else:
        with open(os.path.join(here, 'index2.html'), 'w') as index2_file:
            index2_file.write('{% load static %}\n')
            index2_file.write(index2_content)
