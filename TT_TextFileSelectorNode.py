import os
import random
from typing import List
from nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

class TT_TextFileSelectorNode:
    @classmethod
    def INPUT_TYPES(cls):
        """
        Defines the input types for the node. The user only provides the 'file_path' and 'seed'.
        No 'selection' input is provided.
        """
        file_path = os.path.join(os.path.dirname(__file__), "DefaultList.txt")  # Relative path to the .txt file
        return {
            "required": {
                "seed": ("INT", {"default": 42}),
                "file_path": ("STRING", {"default": file_path}),
            }
        }

    RETURN_TYPES = ("STRING",)  # The output will be a string
    FUNCTION = "output_selection"  # Function that will process the data
    CATEGORY = "TT_TextTools"  # Category for organization in the UI

    @staticmethod
    def load_options(file_path: str = "DefaultList.txt") -> List[str]:
        """
        Loads options from a specified .txt file and forces reload on every call.
        """
        # Check if the file exists and is not empty
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return ["No options available"]  # Default message if file is empty or missing
        
        # Open and read the file fresh every time
        with open(file_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines() if line.strip()]

    def output_selection(self, seed: int, file_path: str):
        """
        Processes the selection and returns either a random choice from the file or a specific choice.
        """
        options = self.load_options(file_path)  # Force reload of the options from the file
        
        if options == ["No options available"]:
            return ("No options available",)
        
        random.seed(seed)  # Set the random seed for reproducibility
        
        # Return a random choice from the options
        return (random.choice(options),)

# Register the new node class
NODE_CLASS_MAPPINGS["TT_TextFileSelectorNode"] = TT_TextFileSelectorNode
NODE_DISPLAY_NAME_MAPPINGS["TT_TextFileSelectorNode"] = "Text File Selector Node"  # Friendly name for UI
