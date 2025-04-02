from .TT_StoryCombiner import TT_StoryCombiner
from .TT_TextInput import TT_TextInput
from .TT_TextFileSelectorNode import TT_TextFileSelectorNode
from .TT_TextReplacer import TT_TextReplacer

NODE_CLASS_MAPPINGS = {
    "TT_StoryCombiner": TT_StoryCombiner,
    "TT_TextInput": TT_TextInput,
    "TT_TextFileSelectorNode": TT_TextFileSelectorNode,
    "TT_TextReplacer": TT_TextReplacer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TT_StoryCombiner": "TT_StoryCombiner",
    "TT_TextInput": "TT_TextInput",
    "TT_TextFileSelectorNode": "TT_TextFileSelectorNode",
    "TT_TextReplacer": "TT_TextReplacer",
}