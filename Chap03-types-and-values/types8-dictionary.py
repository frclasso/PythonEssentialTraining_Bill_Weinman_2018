#!/usr/bin/env python3

x = {'one': 1, 'two': 2, 'tree': 3, 'four': 4, 'five': 5}
x['tree'] = 42
for k, v in x.items():
    print('Key {} and Value {}'.format(k, v))