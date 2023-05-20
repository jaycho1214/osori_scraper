import random


def generate_chord_set(limit: int):
    """랜덤 코드 세트를 줌"""
    root_notes = [
        "C",
        "C#",
        "Db",
        "D",
        "D#",
        "Eb",
        "E",
        "F",
        "F#",
        "Gb",
        "G",
        "G#",
        "Ab",
        "A",
        "A#",
        "Bb",
        "B",
    ]
    chord_sets = []

    for _ in range(limit):
        start_chord = random.choice(root_notes) + str(random.randint(1, 6))

        root = start_chord[:-1]
        octave = int(start_chord[-1])

        next_root_index = root_notes.index(root) + random.randint(1, 3)
        next_root = root_notes[next_root_index % len(root_notes)]

        next_octave = octave + random.randint(1, 3)

        next_chord = f"{next_root}{next_octave}"

        chord_sets.append([start_chord, next_chord])

    return chord_sets
