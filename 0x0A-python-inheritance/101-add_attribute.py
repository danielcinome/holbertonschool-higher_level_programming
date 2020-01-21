#!/usr/bin/python3
def add_attribute(mc, name, key):
    mc.name = key
    if hasattr(mc, 'name'):
        return True
    else:
        raise TypeError("can't add new attribute")
