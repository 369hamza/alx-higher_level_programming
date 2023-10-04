#!/usr/bin/python3
def magic_string(H=[]):
    H.append("BestSchool" + "$" * len(H))
    return (", ".join(H))
