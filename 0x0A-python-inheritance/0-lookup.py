#!/usr/bin/python3
# 0-lookup.py
https://www.archspm.org/faith-and-discipleship/catholic-faith/how-do-i-avoid-misusing-gods-name/
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
