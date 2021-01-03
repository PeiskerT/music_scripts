from Instruments import Harmonica
import utils.Music_Theory as music


def call_DiatonicHarmonica():

    harp = Harmonica.DiationicHarmonica("C")
    print(harp.get_tab([music.Note("C5"), music.Note("C5"), music.Note("C6"), music.Note("C5")])) # telekom track


def main():
    call_DiatonicHarmonica()


if __name__ == "__main__":
    main()
