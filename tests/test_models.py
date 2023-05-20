import pytest
from osori_scraper.models.song import Song
from osori_scraper.core.exceptions import UnexpectedFieldValue

from .utils import generate_chord_set


def test_song_eq():
    """__eq__ 혹은 Song == Song이 잘 작동되는지 확인"""
    assert Song(
        id="1", name="test", composer="test", highest_note="test", lowest_note="test"
    ) == Song(
        id="1",
        name="test1",
        composer="test2",
        highest_note="test3",
        lowest_note="test4",
    ), "Song class should be treated equal if it has the same id"

    assert Song(
        id="1", name="test", composer="test", highest_note="test", lowest_note="test"
    ) == Song(
        id="1", name="test", composer="test", highest_note="test", lowest_note="test"
    ), "Song class are not equal"

    assert Song(
        id="1", name="test", composer="test", highest_note="test", lowest_note="test"
    ) == Song(
        id="2", name="test", composer="test", highest_note="test", lowest_note="test"
    ), "Song class should not be treated equal if it has the different id"


def test_song_compare_chord():
    # Test Cases
    assert Song.compare_chords("C4", "C4") == 0
    assert Song.compare_chords("A#2", "A#2") == 0
    assert Song.compare_chords("G3", "F#3") == -1
    assert Song.compare_chords("D5", "E4") == 1
    assert Song.compare_chords("Bb3", "Bb2") == 1
    assert Song.compare_chords("C#4", "C#5") == -1
    assert Song.compare_chords("G2", "F2") == 1
    assert Song.compare_chords("D#3", "D3") == 1
    assert Song.compare_chords("A4", "A5") == -1
    assert Song.compare_chords("F#1", "G1") == -1

    # Additional Test Cases
    assert Song.compare_chords("C4", "D#3") == -1
    assert Song.compare_chords("G#2", "G2") == 1
    assert Song.compare_chords("Bb5", "C5") == -1
    assert Song.compare_chords("E3", "Eb3") == 1
    assert Song.compare_chords("F#4", "Gb4") == 0
    assert Song.compare_chords("C#6", "C#6") == 0
    assert Song.compare_chords("A#3", "B3") == -1
    assert Song.compare_chords("D2", "D#2") == -1
    assert Song.compare_chords("G5", "G4") == 1
    assert Song.compare_chords("F4", "F#4") == -1


def test_song_chord():
    """Song Class을 만들때 note구별을 하는지 확인"""

    with pytest.raises(UnexpectedFieldValue):
        "highest_note와 lowest_note가 같으면 오류"
        Song(name="", composer="", highest_note="Fb3", lowest_note="Fb3")

    with pytest.raises(UnexpectedFieldValue):
        "lowest_note가 highest_note보다 높으면 오류"
        samples = generate_chord_set(10000)
        for sample in samples:
            Song(name="", composer="", highest_note=sample[1], lowest_note=sample[0])

    with pytest.raises(UnexpectedFieldValue):
        "note가 맞는 형태인지 확인"
        Song(name="", composer="", highest_note="Fb4 ", lowest_note="Fb 5")  # 띄어쓰기 안됨
        Song(name="", composer="", highest_note="H9", lowest_note="Z5")  # 이런거 존재 안함
        Song(name="", composer="", highest_note="hi", lowest_note="yo")  # 이런거 존재 안함
        Song(
            name="", composer="", highest_note="test", lowest_note="test1"
        )  # 이런거 존재 안함

    "잘 작동하는지 확인"
    try:
        samples = generate_chord_set(10000)
        for sample in samples:
            Song(name="", composer="", highest_note=sample[0], lowest_note=sample[1])
    except:
        pytest.fail("맞는 노트 형식인데 에러 발생")
