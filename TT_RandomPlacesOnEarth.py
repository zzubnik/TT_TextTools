import os
import json
import random
from typing import List
import comfy.model_management
from nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

class TT_RandomPlacesOnEarth:
    @classmethod
    def INPUT_TYPES(cls):
        options = cls.load_options()
        if options:
            options.insert(0, "Random Choice")  # Add 'Random Choice' at the top
        return {"required": {"selection": (options, {"default": options[0] if options else ""}), "seed": ("INT", {"default": 42})}}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "output_selection"
    CATEGORY = "TT_TextTools"

    @staticmethod
    def load_options() -> List[str]:
        file_path = os.path.join(os.path.dirname(__file__), "RandomPlacesOnEarth.txt")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return [line.strip() for line in f.readlines() if line.strip()]
        return ["No options found"]

    def output_selection(self, selection: str, seed: int):
        if selection == "Random Choice":
            options = self.load_options()
            if options and "Random Choice" in options:
                options.remove("Random Choice")  # Remove 'Random Choice' before picking
            random.seed(seed)  # Set seed for reproducibility
            return (random.choice(options) if options else "No options available",)
        return (selection,)

# Register the node
NODE_CLASS_MAPPINGS["TT_RandomPlacesOnEarth"] = TT_RandomPlacesOnEarth
NODE_DISPLAY_NAME_MAPPINGS["TT_RandomPlacesOnEarth"] = "TT_RandomPlacesOnEarth"
