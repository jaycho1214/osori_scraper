"""All Exceptions"""


class Uninitialized(Exception):
    """아직 초기화 하지 않음"""

    def __init__(self, method: str) -> None:
        self.message = f"${method}()를 불러 초기화 할 것"
        super().__init__(self.message)


class MissingFieldValue(Exception):
    """JSON파일에서 특정 변수를 발견하지 못함"""

    def __init__(self, field: str) -> None:
        self.message = f"{field}이 json 파일에서 발견되지 않음"
        super().__init__(self.message)


class DuplicatedValue(Exception):
    """JSON파일에서 중복된 값이 있을때"""

    def __init__(self, index1: int, index2: int) -> None:
        self.message = f"`{index1}`와 `{index2}`에서 중복된 값 발견"
        super().__init__(self.message)
