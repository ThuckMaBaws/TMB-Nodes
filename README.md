# TMB-Nodes

# ComfyUI - LoRA Tools

A small ComfyUI custom node bundle with utilities for LoRA users.

## ✨ Node: LoRA Example Prompt

This node helps generate example prompts when using LoRA models.

### Inputs

- `lora_name`: The name of the LoRA (e.g., `anime_girl_sdxl`)
- `model_hint`: Select `auto` to let the node guess the model (SDXL, SD1.5, Flux), or manually pick one.

### Outputs

- `positive_prompt`
- `negative_prompt`
- `model_target`: Inferred or selected base model (e.g., SDXL)

### Output Example

```text
positive_prompt: masterpiece, best quality, anime style, 1girl, {lora:anime_girl_sdxl:0.7}
negative_prompt: lowres, bad anatomy, extra limbs
model_target: SDXL
