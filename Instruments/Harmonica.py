from pathlib import Path
import utils.Music_Theory as music
import numpy as np


class Harmonica():  # Todo: make the other two classes implement from here
    def show(self):
        print("under development")


class DiationicHarmonica():  # TODO add bending notes
    def __init__(self, harpkey):
        self.key = harpkey
        self.layout = self.create_layout(harpkey)
        self.layout_names = [[tone.name for tone in row] for row in self.layout]
        self.extra_notes = self.get_extra_notes(self.get_lowest_harp_note(harpkey))
        self.extra_notes_names = [tone.name for _,tone in self.extra_notes.items()]
        print("A new harp in the key of " + harpkey + " was created")
        print(self.layout_names)
        print(self.extra_notes_names)

    def get_lowest_harp_note(self, n):
        switcher = {  # figure out the lowest note
            "G": "G3",
            "Ab": "Ab3",
            "A": "A3",
            "Bb": "Bb3",
            "B": "B3",
            "C": "C4",
            "Db": "Db4",
            "D": "D4",
            "Eb": "Eb4",
            "E": "E4",
            "F": "F",
            "Gb": "Gb4",
        }
        return switcher.get(n, "Invalid key")

    def create_layout(self, key):

        base_letter = self.get_lowest_harp_note(music.put_in_flat_notation(key))
        base_note = music.Note(base_letter)

        layout = [  # blow notes, draw notes
            [base_note, base_note.higher(4), base_note.higher(7), base_note.higher(12), base_note.higher(16),
             base_note.higher(19), base_note.higher(24), base_note.higher(28), base_note.higher(31),
             base_note.higher(36)],
            [base_note.higher(2), base_note.higher(7), base_note.higher(11), base_note.higher(14), base_note.higher(17),
             base_note.higher(21), base_note.higher(23), base_note.higher(26), base_note.higher(29),
             base_note.higher(33)]
        ]
        return layout

    def get_extra_notes(self, basenote_name):
        base_note = music.Note(basenote_name)
        notes = {"-1b": base_note.higher(1),
         "-2b": base_note.higher(6),
         "-2bb": base_note.higher(5),
         "-3b": base_note.higher(10),
         "-3bb": base_note.higher(9),
         "-3bbb": base_note.higher(8),
         "-4b": base_note.higher(13),
         "-6b": base_note.higher(20),
         "8b": base_note.higher(27),
         "9b": base_note.higher(30),
         "10b": base_note.higher(35),
         "10bb": base_note.higher(34)
         }
        return notes

    def get_tab(self, piano_notes):
        def get_harp_equivalent(
                note):  # for now, we will always choose the first note if there are duplicates TODO: add option to select
            harp_note = ""
            positions = np.where(np.array(self.layout_names) == str(note.name))
            row = positions[0][0]
            hole = positions[1][0]
            if row == 1:
                harp_note += "-"  # draw reed
            harp_note += str(hole + 1)  # +1 because harps start counting at one and not zero
            return harp_note

        tab = [get_harp_equivalent(note) for note in piano_notes]

        return tab


class Chromonica:
    # assuming 12hole chromatic harmonica in the key of C
    def __init__(self):
        self.layout_names = self.create_layout()

    def create_layout(self):
        layout = [  # blow, draw, blow (slide-in), draw (slide-in)
            ["C4", "E4", "G4", "C5", "C5", "E5", "G5", "C6", "C6", "E6", "G6", "C7"],
            ["D4", "F4", "A4", "B4", "D5", "F5", "A5", "B5", "D6", "F6", "A6", "B6"],
            ["Db4", "F4", "Ab4", "Db5", "Db5", "F5", "Ab5", "Db6", "Db6", "F6", "Ab6", "Db7"],
            ["Eb4", "Gb4", "Bb4", "C5", "Eb5", "Gb5", "Bb5", "C6", "Eb6", "Gb6", "Bb6", "C7"]
        ]
        return layout

