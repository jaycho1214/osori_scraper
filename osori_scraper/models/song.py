import uuid
from dataclasses import dataclass
from typing import Optional

from .codable import Codable


@dataclass
class Song(Codable):
    name: str
    composer: str
    highest_note: str
    lowest_note: str
    id: Optional[str] = None

    def __eq__(self, __value: object) -> bool:
        """id가 같으면 같은 거임"""
        pass

    def __post_init__(self):
        """모든 attributes의 변수 타입이 맞는지 확인"""
        for name, field_type in self.__annotations__.items():
            if not isinstance(self.__dict__[name], field_type):
                current_type = type(self.__dict__[name])
                raise TypeError(f"`{name}`값이 `{field_type}`대신 `{current_type}`로 설정됨")
        """만약 id설정 안되있으면 uuid4 id로 설정"""
        if self.id is None:
            self.id = uuid.uuid4()
