class Note():
    def __init__(self, name):
        self.name = name
        self.piano_id = letter_keynum(name)  # 1-88
        self.octave, self.note = get_octave_and_note(self.piano_id)  # C = 1, Db = 2, ..., B = 12
        self.freq = "{:.2f}".format(get_freq(self.piano_id))

    def higher(self, semitones):
        return get_relative_note(self, int(semitones))

    def lower(self, semitones):
        return get_relative_note(self, -int(semitones))


letters = {  # the twelve semitones of an octave in letter notation
        1: "C",
        2: "Db",
        3: "D",
        4: "Eb",
        5: "E",
        6: "F",
        7: "Gb",
        8: "G",
        9: "Ab",
        10: "A",
        11: "Bb",
        12: "B"
    }


def keynum_letter(i):
    octave, note = get_octave_and_note(i)
    keyname = str(letters[note]) + str(octave)
    return keyname


def letter_keynum(l):
    note = 0
    for num, letter in letters.items():
        if l[:-1] == letter:
            note = num
    num = 12 * int(l[-1]) - 9 + note
    return num


def get_octave_and_note(piano_id):
    piano_id += 8  # the pianos lowest key is A0, which is 9 semitones above C0  # TODO: explain why 8 and not 9. It doesn't work with the mod underneath otherwise. There is a plus one further down to get back to the original transposition of 9
    quo, rem = divmod(piano_id, 12)
    return quo, rem+1


def get_freq(piano_id):
    f = 440 * (2 ** (1 / 12.0)) ** (piano_id - 49)  # compute frequency of ith key
    return f


def put_in_flat_notation(note):  # convert all # to b for internal processing, e.g. F# => Gb
    switcher = {  # figure out the lowest note
        "G": "G",
        "G#": "Ab",
        "Ab": "Ab",
        "A": "A",
        "A#": "Bb",
        "Bb": "Bb",
        "B": "B",
        "C": "C",
        "C#": "Db",
        "Db": "Db",
        "D": "D",
        "D#": "Eb",
        "Eb": "Eb",
        "E": "E",
        "F": "F",
        "F#": "Gb",
        "Gb": "Gb"
    }
    return switcher.get(note,"Invalid note")

def put_in_sharp_notation(note):  # convert all b to # for internal processing, e.g. Gb => F#
    switcher = {
        "G": "G",
        "G#": "G#",
        "Ab": "G#",
        "A": "A",
        "A#": "A#",
        "Bb": "A#",
        "B": "B",
        "C": "C",
        "C#": "C#",
        "Db": "C#",
        "D": "D",
        "D#": "D#",
        "Eb": "D#",
        "E": "E",
        "F": "F",
        "F#": "F#",
        "Gb": "F#"
    }
    return switcher.get(note, "Invalid note")


def get_relative_note(base_note, semitones):
    new_tone_id = base_note.piano_id + semitones
    letter = keynum_letter(new_tone_id)
    return Note(letter)
