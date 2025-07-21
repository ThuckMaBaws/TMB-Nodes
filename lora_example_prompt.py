# lora_example_prompt.py

import os

LORA_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "models", "lora")

class LoRAExamplePrompt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "lora_name": (cls.get_lora_names(),),
                "model_hint": (
                    ["auto", "SD1.5", "SDXL", "Flux", "Other"],
                    {"default": "auto"},
                ),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt", "model_target")
    FUNCTION = "generate_prompt"
    CATEGORY = "TMB_Nodes"

    @staticmethod
    def get_lora_names():
        if not os.path.exists(LORA_PATH):
            return ["No LoRAs Found"]
        files = os.listdir(LORA_PATH)
        loras = [f for f in files if f.endswith((".safetensors", ".pt", ".ckpt"))]
        return sorted([os.path.splitext(f)[0] for f in loras]) or ["No LoRAs Found"]

    def detect_model(self, name):
        name = name.lower()
        if "xl" in name or "sdxl" in name:
            return "SDXL"
        elif "1.5" in name or "sd15" in name or "sd1.5" in name:
            return "SD1.5"
        elif "flux" in name:
            return "Flux"
        else:
            return "Unknown"

    def generate_prompt(self, lora_name, model_hint):
        model_type = self.detect_model(lora_name) if model_hint == "auto" else model_hint

        if "anime" in lora_name.lower():
            pos = f"masterpiece, best quality, anime style, 1girl, {{{{lora:{lora_name}:0.7}}}}"
            neg = "lowres, bad anatomy, extra limbs"
        elif "real" in lora_name.lower() or "photo" in lora_name.lower():
            pos = f"photo-realistic, sharp details, cinematic lighting, {{{{lora:{lora_name}:0.6}}}}"
            neg = "cartoon, low detail, distorted face"
        else:
            pos = f"concept art, stylized, dramatic lighting, {{{{lora:{lora_name}:0.5}}}}"
            neg = "bad composition, noisy background"

        return (pos, neg, model_type)

NODE_CLASS_MAPPINGS = {
    "LoRAExamplePrompt": LoRAExamplePrompt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoRAExamplePrompt": "LoRA Example Prompt",
}