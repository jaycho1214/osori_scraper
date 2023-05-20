import json
from typing import List, Optional
import sys

from osori_scraper.core.exceptions import MissingFieldValue
from osori_scraper.models.codable import Codable


class JSONParser:
    """
    JSON파일을 읽고 맞는지 확인함

    Attributes:
      file_name (str): 파일 이름
      data

    Methods:
      reload() -> None:
        JSON 파일을 다시 읽어옴

      validate() -> bool:
        JSON 파일에 모든 변수가 있는지 확인함
    """

    def __init__(self, file_name: str, type: Optional[Codable] = None) -> None:
        self.file_name = file_name
        self.type = type
        self._data = None
        self.reload()

    @property
    def data(self):
        """data를 직접 수정할 수 없겠금 하기 위해 property로함"""
        return self._data

    @data.setter
    def data(self, data):
        if not "pytest" in sys.modules:
            raise "data can be directly modified only on test environment"
        self._data = data

    def reload(self) -> None:
        """Reload the json file"""
        with open(self.file_name) as f:
            self.data = json.load(f)

    def validate(self) -> bool:
        """
        self.type을 이용해서 json안에 모든 list들이 모든 field를 가지고 있는지 체크
        여기서는 sample.json파일을 참고할것
        id는 없어도됨

        Errors:
          MissingFieldValue:
            만약 특정 field가 비어있으면 이 에러를 raise함
          DuplicatedValue:
            똑같은 값이 2개 있을때 오류

        Returns:
            만약 valid하면 True 반환
        """
        pass

    def to_object(self) -> List[Codable]:
        if self.data is None:
            """여기서 Raise Uninitialized Error를 raise할 것"""
            pass
        pass
