import random
from typing import List
import comfy.model_management as model_management

class TT_StoryCombiner:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text1": ("STRING", {"multiline": True}),
                "text2": ("STRING", {"multiline": True}),
                "text3": ("STRING", {"multiline": True}),
                "text4": ("STRING", {"multiline": True}),
                "text5": ("STRING", {"multiline": True}),
                "text6": ("STRING", {"multiline": True}),
                "text7": ("STRING", {"multiline": True}),
                "text8": ("STRING", {"multiline": True}),
                "text9": ("STRING", {"multiline": True}),                
                "separator": ("STRING", {"default": ". "}),
                "seed": ("INT", {"default": 0}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    CATEGORY = "TT_TextTools"
    
    def process(self, text1: str, text2: str, text3: str, text4: str, text5: str, text6: str, text7: str, text8: str, text9: str, separator: str, seed: int) -> List[str]:
        random.seed(seed)
        
        def get_random_line(text):
            lines = [line.strip() for line in text.split("\n") if line.strip()]
            return random.choice(lines) if lines else ""
        
        selected_lines = [
            get_random_line(text1),
            get_random_line(text2),
            get_random_line(text3),
            get_random_line(text4),
            get_random_line(text5),
            get_random_line(text6),
            get_random_line(text7),
            get_random_line(text8),
            get_random_line(text9)
        ]
        
        filtered_lines = [line for line in selected_lines if line]
        
        result = separator.join(filtered_lines)
        
        return (result,)

def register_nodes():
    return {"TT_StoryCombiner": TT_StoryCombiner}

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "TT_StoryCombiner": TT_StoryCombiner
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "TT_StoryCombiner": "TT_StoryCombiner"
}
