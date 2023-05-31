import re
import regex
from Serializers import BaseSerializer


from Serializers import nonetype


class JsonSerializer(BaseSerializer):
    INF_LITERAL = str(1E1000)
    NAN_LITERAL = str(1E1000 / 1E1000)

    TRUE_LITERAL = "true"
    FALSE_LITERAL = "false"

    NULL_LITERAL = "null"

    INT_PATTERN = fr"[+-]?\d+"
    FLOAT_PATTERN = fr"(?:[+-]?\d+(?:\.\d+)?(?:e[+-]?\d+)?|[+-]?{INF_LITERAL}\b|{NAN_LITERAL}\b)"
    BOOL_PATTERN = fr"({TRUE_LITERAL}|{FALSE_LITERAL})\b"
    STRING_PATTERN = fr"\"(?:(?:\\\")|[^\"])*\""
    NULL_PATTERN = fr"\b{NULL_LITERAL}\b"

    ELEMENTARY_TYPES_PATTERN = fr"{FLOAT_PATTERN}|{INT_PATTERN}|{BOOL_PATTERN}|{STRING_PATTERN}|{NULL_PATTERN}"

    # This regex use recursive statements to be able to capture nested lists and objects.
    ARRAY_PATTERN = r"\[(?R)?(?:,(?R))*\]"
    OBJECT_PATTERN = r"\{(?:(?R):(?R))?(?:,(?R):(?R))*\}"

    VALUE_PATTERN = fr"\s*({ELEMENTARY_TYPES_PATTERN}|" + \
                    fr"{ARRAY_PATTERN}|{OBJECT_PATTERN})\s*"

    def dumps(self, obj) -> str:
        obj = DictSerializer.to_dict(obj)
        return self.__dumps_from_dict(obj)



