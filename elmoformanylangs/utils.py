#!/usr/bin/env python
from __future__ import unicode_literals
import collections
import itertools


def flatten(lst):
  return list(itertools.chain.from_iterable(lst))


def deep_iter(x):
  if isinstance(x, (list, tuple)):
    for u in x:
      yield from deep_iter(u)
  else:
    yield


def dict2namedtuple(dic):
  return collections.namedtuple('Namespace', dic.keys())(**dic)