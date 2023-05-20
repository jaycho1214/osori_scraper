from osori_scraper.models.song import Song


def test_song_eq():
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
