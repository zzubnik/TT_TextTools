import comfy.model_management

class TT_TextReplacer:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_text_1": ("STRING", {"multiline": True}),
                "find_word": ("STRING", {"multiline": False}),
                "replace_word": ("STRING", {"multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_text",)
    FUNCTION = "run"
    CATEGORY = "TT_TextTools"

    def run(self, input_text_1, find_word, replace_word):
        # Replace the search word with the replace word in the first input text
        output_text = input_text_1.replace(find_word, replace_word)
        return (output_text,)

NODE_CLASS_MAPPINGS = {"TT_TextReplacer": TT_TextReplacer}
NODE_DISPLAY_NAME_MAPPINGS = {"TT_TextReplacer": "TT_TextReplacer"}


