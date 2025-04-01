import comfy.model_management

class TT_TextInput:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"text": ("STRING", {"multiline": True, "default": ""})}}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    CATEGORY = "TT_TextTools"

    def process(self, text):
        return (text,)

# Register the node
NODE_CLASS_MAPPINGS = {"TT_TextInput": TT_TextInput}
NODE_DISPLAY_NAME_MAPPINGS = {"TT_TextInput": "TT_TextInput"}
