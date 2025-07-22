import os

LORA_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "models", "loras")


class LoRAExamplePrompt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "lora_name": (cls.get_lora_names(),),
                "model_hint": (
                    ["auto", "SD1.5", "SD2.1", "SDXL", "Illustrious", "Flux", "Other"],
                    {"default": "auto"},
                ),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt", "model_target", "trigger_words")
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

        if any(keyword in name for keyword in ["illustrious", "illubase", "illu", "illust"]):
            return "Illustrious"
        elif "xl" in name or "sdxl" in name or "v1-5-xl" in name or "xl_base" in name:
            return "SDXL"
        elif "1.5" in name or "v1-5" in name or "sd15" in name:
            return "SD1.5"
        elif "2.1" in name or "v2" in name or "sd21" in name:
            return "SD2.1"
        elif "flux" in name:
            return "Flux"
        elif "other" in name or "misc" in name:
            return "Other"
        else:
            return "Unknown"

    def get_trigger_words(self, lora_name):
        txt_file = os.path.join(LORA_PATH, lora_name + ".txt")
        if os.path.exists(txt_file):
            with open(txt_file, "r", encoding="utf-8") as f:
                return f.read().strip()
        else:
            return "No trigger words found."

    def generate_prompt(self, lora_name, model_hint):
        model_type = self.detect_model(lora_name) if model_hint == "auto" else model_hint
        trigger_words = self.get_trigger_words(lora_name)

        if "anime" in lora_name.lower():
            pos = f"masterpiece, best quality, anime style, 1girl, {{{{lora:{lora_name}:0.7}}}}"
            neg = "lowres, bad anatomy, extra limbs"
        elif "real" in lora_name.lower() or "photo" in lora_name.lower():
            pos = f"photo-realistic, sharp details, cinematic lighting, {{{{lora:{lora_name}:0.6}}}}"
            neg = "cartoon, low detail, distorted face"
        else:
            pos = f"concept art, stylized, dramatic lighting, {{{{lora:{lora_name}:0.5}}}}"
            neg = "bad composition, noisy background"

        return (pos, neg, model_type, trigger_words)


NODE_CLASS_MAPPINGS = {
    "LoRAExamplePrompt": LoRAExamplePrompt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoRAExamplePrompt": "LoRA Example Prompt",
}
