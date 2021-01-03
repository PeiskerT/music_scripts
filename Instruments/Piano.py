"""
Since the piano is the central instrument of western music, we use this instrument for an intermediate step in the
mapping process.
"""


import math
import numpy as np
import utils.Music_Theory as music

class Piano():

    def __init__(self):
        self.layout = self.create_layout()
        self.layout_names = [tone.name for tone in self.layout]

    def create_layout(self):
        return [music.Note(music.keynum_letter(i)) for i in range(1, 89)]  # loop over all 88 piano keys

    def print_freqs(self):

        for i in range(1,89):  # loop over all 88 piano keys
            f = 440* (2 ** (1/12.0)) ** (i-49)  # compute frequency of ith key
            l = music.keynum_letter(i)  # letter name of ith piano key
            print(l + ": \"" + "{:.2f}".format(f) + "\",")

