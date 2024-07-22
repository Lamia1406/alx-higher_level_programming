#!/usr/bin/python3
""" find the peak in list of integers"""


def find_peak(list_of_integers):
    """find the peak in a list of integers """
    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        peaks = []
        for i in range(len(list_of_integers) - 1):
            peak = list_of_integers[i]
            successor = list_of_integers[i + 1]
            ancestor = list_of_integers[i - 1]
            if peak >= successor and peak >= ancestor:
                peaks.append(peak)
        return find_peak(peaks)
