import json


class Codable:
    @staticmethod
    @classmethod
    def from_json(cls, json):
        return cls(**json)

    def to_json(self):
        return json.dumps(self.__dict__)
