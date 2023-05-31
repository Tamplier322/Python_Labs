import inspect
from Serializers import nonetype, moduletype, codetype, celltype, \
                          functype, bldinfunctype, \
                          mapproxytype, wrapdesctype, metdesctype, getsetdesctype, \
                          CODE_PROPS, UNIQUE_TYPES

class DictSerializer:
    TYPE_KW = "type"
    SOURCE_KW = "source"

    CODE_KW = "__code__"
    GLOBALS_KW = functype.__globals__.__name__
    NAME_KW = "__name__"
    DEFAULTS_KW = "__defaults__"
    CLOSURE_KW = functype.__closure__.__name__

    BASES_KW = "__bases__"
    DICT_KW = "__dict__"

    CLASS_KW = "__class__"

    OBJECT_KW = "object"

    @classmethod
    def to_dict(cls, obj, is_inner_func=False):
        if type(obj) in (int, float, bool, str, nonetype):
            return obj

        if type(obj) is list:
            return [cls.to_dict(o) for o in obj]

        if type(obj) is dict:
            # Since the key in the dictionary can be a hashable object, which will be represented as a non-hashable
            # dictionary, it is easier to represent the dictionary as a list of key-value pairs
            return {cls.TYPE_KW: dict.__name__,
                    cls.SOURCE_KW: [[cls.to_dict(item[0]), cls.to_dict(item[1])] for item in obj.items()]}

        if type(obj) in (set, frozenset, tuple, bytes, bytearray):
            return {cls.TYPE_KW: type(obj).__name__,
                    cls.SOURCE_KW: cls.to_dict([*obj])}

        if type(obj) is complex:
            return {cls.TYPE_KW: complex.__name__,
                    cls.SOURCE_KW: {complex.real.__name__: obj.real,
                                    complex.imag.__name__: obj.imag}}

        if type(obj) is moduletype:
            return {cls.TYPE_KW: moduletype.__name__,
                    cls.SOURCE_KW: obj.__name__}

        if type(obj) is codetype:
            code = {cls.TYPE_KW: codetype.__name__}
            source = {}

            for (key, value) in inspect.getmembers(obj):
                if key in CODE_PROPS:
                    source[key] = cls.to_dict(value)

            code.update({cls.SOURCE_KW: source})
            return code

        if type(obj) is celltype:
            return {cls.TYPE_KW: celltype.__name__,
                    cls.SOURCE_KW: cls.to_dict(obj.cell_contents)}

        if type(obj) in (staticmethod, classmethod):
            return {cls.TYPE_KW: type(obj).__name__,
                cls.SOURCE_KW: cls.to_dict(obj.__func__, is_inner_func)}

        if inspect.isroutine(obj):
            source = {}

            # Code
            source[cls.CODE_KW] = cls.to_dict(obj.__code__)

            # Global vars
            gvars = cls.__get_gvars(obj, is_inner_func)
            source[cls.GLOBALS_KW] = cls.to_dict(gvars)

            # Name
            source[cls.NAME_KW] = cls.to_dict(obj.__name__)

            # Defaults
            source[cls.DEFAULTS_KW] = cls.to_dict(obj.__defaults__)

            # Closure
            source[cls.CLOSURE_KW] = cls.to_dict(obj.__closure__)

            return {cls.TYPE_KW: functype.__name__,
                    cls.SOURCE_KW: source}

        elif inspect.isclass(obj):
            source = {}

            # Name
            source[cls.NAME_KW] = cls.to_dict(obj.__name__)

            # Bases
            source[cls.BASES_KW] = cls.to_dict(tuple(b for b in obj.__bases__ if b != object))

            # Dict
            source[cls.DICT_KW] = cls.__get_obj_dict(obj)

            return {cls.TYPE_KW: type.__name__,
                    cls.SOURCE_KW: source}

        else:
            source = {}

            # Class
            source[cls.CLASS_KW] = cls.to_dict(obj.__class__)

            # Dict
            source[cls.DICT_KW] = cls.__get_obj_dict(obj)

            return {cls.TYPE_KW: cls.OBJECT_KW,
                    cls.SOURCE_KW: source}


