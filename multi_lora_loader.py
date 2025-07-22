
import os
import folder_paths
from nodes import LoraLoader

LORA_PATH = os.path.join(folder_paths.models_dir, "loras")

class MultiLoRALoader:
    @classmethod
    def INPUT_TYPES(cls):
        lora_names = cls.get_lora_names()
        lora_dropdown = lora_names
        num_options = list(range(1, 6))  # 1 to 5

        input_types = {
            "required": {
                "model": ("MODEL",),
                "clip": ("CLIP",),
                "number_of_loras": (num_options, {
                    "default": 1,
                    "label": "Number of LoRAs"
                }),
            }
        }

        # Add all LoRA dropdowns and weights with clarifying labels
        for i in range(1, 6):
            label = f"LoRA {i} Name{' (active)' if i == 1 else f' (used if number_of_loras ≥ {i})'}"
            weight_label = f"LoRA {i} Weight{' (active)' if i == 1 else f' (used if number_of_loras ≥ {i})'}"

            input_types["required"][f"lora_name_{i}"] = (lora_dropdown, {"label": label})
            input_types["required"][f"lora_weight_{i}"] = ("FLOAT", {
                "default": 0.5,
                "min": 0.0,
                "max": 2.0,
                "step": 0.05,
                "label": weight_label
            })

        return input_types

    RETURN_TYPES = ("MODEL", "CLIP")
    FUNCTION = "load_loras"
    CATEGORY = "TMB_Nodes"

    @staticmethod
    def get_lora_names():
        if not os.path.exists(LORA_PATH):
            return ["No LoRAs Found"]
        files = os.listdir(LORA_PATH)
        loras = [f for f in files if f.endswith((".safetensors", ".pt", ".ckpt"))]
        return sorted([os.path.splitext(f)[0] for f in loras]) or ["No LoRAs Found"]

    def load_loras(self, model, clip, number_of_loras,
                   lora_name_1, lora_weight_1,
                   lora_name_2, lora_weight_2,
                   lora_name_3, lora_weight_3,
                   lora_name_4, lora_weight_4,
                   lora_name_5, lora_weight_5):

        lora_data = [
            (lora_name_1, lora_weight_1),
            (lora_name_2, lora_weight_2),
            (lora_name_3, lora_weight_3),
            (lora_name_4, lora_weight_4),
            (lora_name_5, lora_weight_5),
        ]

        for i in range(number_of_loras):
            name, weight = lora_data[i]
            if name and name != "No LoRAs Found":
                lora_path = folder_paths.get_full_path("loras", name + ".safetensors")
                model, clip = LoraLoader.load_lora(model, clip, lora_path, weight)

        return (model, clip)

NODE_CLASS_MAPPINGS = {
    "MultiLoRALoader": MultiLoRALoader,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MultiLoRALoader": "Multi-LoRA Loader",
}
