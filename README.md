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




# 🧩 Multi LoRA Loader (ComfyUI Node)

A custom ComfyUI node that allows you to apply multiple LoRA models to a base model without needing a separate stacker.

---

## ✨ Features

- 🔢 Load **1–5 LoRAs** simultaneously
- 🎚 Set individual **weights** per LoRA
- 🧠 **Auto-detects LoRA model compatibility** (e.g. SD1.5, SDXL, Illustrious, etc.)
- ⚠️ Warns if LoRA base type doesn't match model
- 🔁 Optional **reset weights** toggle
- 🧼 Cleaner and more user-friendly than stacking multiple nodes manually

---

## 🛠 Inputs

| Input         | Type    | Description                                                                 |
|---------------|---------|-----------------------------------------------------------------------------|
| `model`       | MODEL   | The base model to apply LoRAs to                                            |
| `clip`        | CLIP    | The corresponding CLIP encoder                                              |
| `num_loras`   | INT     | Number of LoRAs to apply (1 to 5)                                           |
| `reset_weights` | BOOL  | If true, all LoRA weights reset to default (0.5)                            |
| `lora_X_name` | STRING  | Dropdown to select a LoRA file (auto-loaded from `models/lora/`)           |
| `lora_X_weight` | FLOAT | Slider to set the LoRA strength (0.0 to 1.5, default = 0.5)                 |

> Replace `X` with numbers 1–5 depending on how many LoRAs you are loading.

---

## 🔁 Outputs

| Output               | Type    | Description                                   |
|----------------------|---------|-----------------------------------------------|
| `model`              | MODEL   | The updated model with all LoRAs applied      |
| `clip`               | CLIP    | The updated CLIP with all LoRAs applied       |
| `compatibility_info` | STRING  | A message with compatibility warnings or OK ✅ |

---

## 🧠 Model Compatibility Detection

This node attempts to infer the LoRA’s target base model by checking its filename for keywords like:

| Detected | Keywords                          |
|----------|-----------------------------------|
| SDXL     | `sdxl`, `xl`, `xl_base`           |
| SD1.5    | `1.5`, `v1-5`, `sd15`             |
| SD2.1    | `2.1`, `sd21`, `v2`               |
| Illustrious | `illu`, `illubase`, `illustrious`, `illust` |
| Flux     | `flux`                            |

It then compares that to the base model string to give you helpful guidance.

