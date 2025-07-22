# 📦 TMB Nodes – Custom LoRA Tools for ComfyUI

A lightweight, user-focused collection of **custom nodes for working with LoRAs in ComfyUI** — designed to make LoRA management, previewing, and loading more intuitive and flexible.

---

## 🔧 Included Nodes

| Node Name               | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| 📝 **LoRA Example Prompt** | Displays the recommended prompt and model compatibility for a selected LoRA |
| 🧩 **Multi LoRA Loader**   | Loads up to 5 LoRAs in one node, applies weights, and checks compatibility  |

---

## 📝 LoRA Example Prompt

This node inspects a LoRA file and provides:

- 🔍 **Trigger words** and suggested prompts (based on filename or metadata)
- 🧠 **Inferred model compatibility** (e.g. SD1.5, SDXL, Illustrious)
- 📄 A ready-to-copy prompt snippet to help you get started

### ➕ Inputs

| Input        | Type    | Description                                          |
|--------------|---------|------------------------------------------------------|
| `lora_name`  | STRING  | Dropdown of all LoRAs found in `models/lora/` folder |

### ➡️ Output

| Output         | Type    | Description                                       |
|----------------|---------|---------------------------------------------------|
| `prompt_text`  | STRING  | Suggested prompt including LoRA trigger words     |
| `compatibility`| STRING  | Inferred base model compatibility (e.g. SDXL)     |

---

## 🧩 Multi LoRA Loader

Load and apply multiple LoRA files in a **single node**, with individual weight controls and automatic model compatibility checking.

### 🎯 Features

- 🔢 Load **1 to 5 LoRAs** simultaneously
- 🎚 Set **individual weights**
- ♻️ Optional **reset all weights**
- ⚠️ Warns if a LoRA’s model type mismatches the current model (e.g. SDXL vs SD1.5)

### ➕ Inputs

| Input           | Type    | Description                                          |
|------------------|---------|------------------------------------------------------|
| `model`         | MODEL   | Base model                                           |
| `clip`          | CLIP    | CLIP encoder                                         |
| `num_loras`     | INT     | Number of LoRAs to load (1–5)                        |
| `reset_weights` | BOOL    | If true, resets all weights to 0.5                   |
| `lora_X_name`   | STRING  | Dropdown to select LoRA X from disk                  |
| `lora_X_weight` | FLOAT   | LoRA strength (default = 0.5)                        |

### ➡️ Outputs

| Output              | Type    | Description                                      |
|---------------------|---------|--------------------------------------------------|
| `model`             | MODEL   | Model with all LoRAs applied                     |
| `clip`              | CLIP    | CLIP encoder with LoRAs applied                  |
| `compatibility_info`| STRING  | Summary of detected compatibility/mismatches     |

### 🧠 Model Type Detection

The loader infers LoRA and model types by filename using the following heuristics:

| Model Type   | Detected by keywords like                        |
|--------------|--------------------------------------------------|
| **SDXL**     | `sdxl`, `xl_base`, `xl`                          |
| **SD1.5**    | `1.5`, `v1-5`, `sd15`                            |
| **SD2.1**    | `2.1`, `v2`, `sd21`                              |
| **Illustrious** | `illu`, `illust`, `illustrious`, `illubase`  |
| **Flux**     | `flux`                                           |
| **Unknown**  | None matched                                     |

---

## 📂 Installation

1. Clone this repo into your `ComfyUI/custom_nodes/` folder:

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/ThuckMaBaws/TMB-Nodes.git
```

2. Make sure your `TMB_Nodes/__init__.py` registers both nodes:

```python
from .lora_example_prompt import NODE_CLASS_MAPPINGS as PROMPT_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as PROMPT_DISPLAY
from .multi_lora_loader import NODE_CLASS_MAPPINGS as MULTI_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as MULTI_DISPLAY

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

NODE_CLASS_MAPPINGS.update(PROMPT_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(PROMPT_DISPLAY)

NODE_CLASS_MAPPINGS.update(MULTI_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MULTI_DISPLAY)
```

3. Restart ComfyUI.

---

## 🧪 Example Workflow

```text
[LoRA Example Prompt] --> (View recommendations)
       ↓
[Multi LoRA Loader]  --> (Apply 3–5 LoRAs with weights)
       ↓
[Text to Image / etc.]
```

---

## 📎 Notes

- Works with `.safetensors`, `.pt`, or `.ckpt` LoRAs
- All LoRA files must be in your `models/lora/` folder
- You can increase the max LoRA count in the loader if needed

---

## 👤 Author

**TMB Nodes** by [@ThuckMaBaws](https://github.com/ThuckMaBaws)  
Issues and pull requests are welcome!