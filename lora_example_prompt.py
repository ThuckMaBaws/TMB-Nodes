# lora_example_prompt.py

LORA_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "models", "lora")

class lora_example_prompt:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "lora_name": ("STRING", {"default": "anime_style_lora_sdxl"}),
                "model_hint": (
                    ["auto", "SD1.5", "SDXL", "Flux", "Other"],
                    {"default": "auto"},
                ),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt", "model_target")
    FUNCTION = "generate_prompt"
    CATEGORY = "TMB Nodes"

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
        # Detect or use user-specified model type
        model_type = self.detect_model(lora_name) if model_hint == "auto" else model_hint

        # Suggest prompt based on style
        if "anime" in lora_name.lower():
            pos = f"masterpiece, best quality, anime style, 1girl, {lora_name}:0.7"
            neg = "lowres, bad anatomy, extra limbs"
        elif "real" in lora_name.lower() or "photo" in lora_name.lower():
            pos = f"photo-realistic, sharp details, cinematic lighting, {lora_name}:0.6"
            neg = "cartoon, low detail, distorted face"
        else:
            pos = f"concept art, stylized, dramatic lighting, {lora_name}:0.5"
            neg = "bad composition, noisy background"

        return (pos, neg, model_type)

NODE_CLASS_MAPPINGS = {
    "lora_example_prompt": lora_example_prompt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "lora_example_prompt": "LoRA Example Prompt",
}
