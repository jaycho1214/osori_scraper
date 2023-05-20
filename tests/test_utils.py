import pytest
from pathlib import Path

SAMPLES_DIR = Path(__file__).resolve().parent / "samples"

from osori_scraper.models.song import Song
from osori_scraper.utils.json import JSONParser
from osori_scraper.core.exceptions import *


def test_check_json():
    parser = JSONParser(SAMPLES_DIR / "invalid_song_data1.json", Song)
    with pytest.raises(MissingFieldValue):
        parser.validate()
    parser = JSONParser(SAMPLES_DIR / "invalid_song_data2.json", Song)
    with pytest.raises(DuplicatedValue):
        parser.validate()
