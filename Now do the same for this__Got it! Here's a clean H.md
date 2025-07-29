<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Now do the same for this

Got it! Here's a clean HOW_TO_BUILD_LOCALMIND.md file (a GitHub convention-friendly name) that walks through how to create your own version of LocalMind on Hugging Face Spaces.

---

# 🛠️ How to Build LocalMind – Self-Hosted AI Chatbot on Hugging Face

This guide walks you through creating your own **LocalMind**-like chatbot from scratch using Hugging Face Spaces — no server, no backend setup, no cost.

---

## 📦 Requirements

- A free [Hugging Face](https://huggingface.co/) account
- Android or desktop browser
- No coding setup needed locally
- Model must be small enough to run in Hugging Face Spaces (TinyLlama used here)

---

## 🧱 Folder Structure

Your project should look like this:

LocalMind/ ├── app.py              \# Main app logic ├── Dockerfile          \# For custom container setup ├── README.md           \# Project info ├── thumbnail.png       \# (Optional) Display image for README ├── HOW_TO_BUILD_LOCALMIND.md   \# This file

---

## 🪜 Step-by-Step Setup

### 1. **Create a New Space**

- Go to [Hugging Face Spaces](https://huggingface.co/spaces)
- Click **Create new Space**
- Name it (e.g. `LocalMind`)
- Select **"Docker"** as the SDK
- Keep it **Public**
- Click **Create Space**

---

### 2. **Add Your Files**

Upload the following files:

#### `app.py` (Chatbot code)

```python
import os
os.environ["TRANSFORMERS_CACHE"] = "/tmp/hf_cache"

import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()

def chat_fn(message, history):
    prompt = ""
    for user, bot in history:
        prompt += f"User: {user}\nBot: {bot}\n"
    prompt += f"User: {message}\nBot:"
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    with torch.no_grad():
        output_ids = model.generate(
            input_ids,
            max_new_tokens=64,
            temperature=0.7,
            top_p=0.95,
            pad_token_id=tokenizer.eos_token_id
        )
    output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    response = output[len(prompt):].strip().split("\n")[0]
    return response if response else "..."

demo = gr.ChatInterface(fn=chat_fn, title="LocalMind")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")

Dockerfile

FROM python:3.10-slim

RUN pip install --no-cache-dir gradio transformers torch

RUN mkdir -p /tmp/hf_cache && chmod 777 /tmp/hf_cache
ENV TRANSFORMERS_CACHE=/tmp/hf_cache

WORKDIR /code
COPY app.py .

EXPOSE 7860

CMD ["python", "app.py"]


---

3. Wait for It to Build

Once all files are uploaded:

Hugging Face will automatically build your Docker container

Wait for the green "Running" badge

Your chatbot UI will be live


✅ Your Space is now working!


---

🔗 Accessing the API

After deployment, your API will be available at:

https://USERNAME-PROJECTNAME.hf.space/chat

Example Python Client:

import requests

url = "https://harshkumarsaw-localmind.hf.space/chat"
payload = {
    "message": "Hello!",
    "history": []
}

res = requests.post(url, json=payload)
print(res.json()["response"])


---

⚠️ Notes

Hugging Face Spaces may sleep after 48h of inactivity

TinyLlama is selected for its speed– you can swap models as needed

You can fork LocalMind and customize


---

🧩 Optional Additions

Add thumbnail.png to display a banner in README

Link your GitHub repo to Hugging Face

Use HF_HOME instead of TRANSFORMERS_CACHE (for future-proofing)


---

🙌 Done!

You now have a fully self-hosted chatbot API — free, fast, and ready to integrate.

---

Let me know if you want this saved as a downloadable file or added directly to your repo!

Here’s a clean, ready-to-save version of your HOW_TO_BUILD_LOCALMIND.md file. Just copy it into a file named `HOW_TO_BUILD_LOCALMIND.md` and it’s good to go!

```markdown
---

# 🛠️ How to Build LocalMind – Self-Hosted AI Chatbot on Hugging Face

This guide walks you through creating your own **LocalMind**-like chatbot from scratch using Hugging Face Spaces — no server, no backend setup, no cost.

---

## 📦 Requirements

- A free [Hugging Face](https://huggingface.co/) account
- Android or desktop browser
- No coding setup needed locally
- Model must be small enough to run in Hugging Face Spaces (TinyLlama used here)

---

## 🧱 Folder Structure

Your project should look like this:

```

LocalMind/
├── app.py              \# Main app logic
├── Dockerfile          \# For custom container setup
├── README.md           \# Project info
├── thumbnail.png       \# (Optional) Display image for README
├── HOW_TO_BUILD_LOCALMIND.md   \# This file

```

---

## 🪜 Step-by-Step Setup

### 1. **Create a New Space**

- Go to [Hugging Face Spaces](https://huggingface.co/spaces)
- Click **Create new Space**
- Name it (e.g. `LocalMind`)
- Select **"Docker"** as the SDK
- Keep it **Public**
- Click **Create Space**

---

### 2. **Add Your Files**

Upload the following files:

#### `app.py` (Chatbot code)

```

import os
os.environ["TRANSFORMERS_CACHE"] = "/tmp/hf_cache"

import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()

def chat_fn(message, history):
prompt = ""
for user, bot in history:
prompt += f"User: {user}\nBot: {bot}\n"
prompt += f"User: {message}\nBot:"
input_ids = tokenizer.encode(prompt, return_tensors="pt")
with torch.no_grad():
output_ids = model.generate(
input_ids,
max_new_tokens=64,
temperature=0.7,
top_p=0.95,
pad_token_id=tokenizer.eos_token_id
)
output = tokenizer.decode(output_ids, skip_special_tokens=True)
response = output[len(prompt):].strip().split("\n")
return response if response else "..."

demo = gr.ChatInterface(fn=chat_fn, title="LocalMind")

if __name__ == "__main__":
demo.launch(server_name="0.0.0.0")

```

#### `Dockerfile`

```

FROM python:3.10-slim

RUN pip install --no-cache-dir gradio transformers torch

RUN mkdir -p /tmp/hf_cache \&\& chmod 777 /tmp/hf_cache
ENV TRANSFORMERS_CACHE=/tmp/hf_cache

WORKDIR /code
COPY app.py .

EXPOSE 7860

CMD ["python", "app.py"]

```

---

### 3. **Wait for It to Build**

Once all files are uploaded:

- Hugging Face will automatically build your Docker container
- Wait for the green **Running** badge
- Your chatbot UI will be live

✅ Your Space is now working!

---

## 🔗 Accessing the API

After deployment, your API will be available at:

```

https://USERNAME-PROJECTNAME.hf.space/chat

```

Example Python Client:

```

import requests

url = "https://harshkumarsaw-localmind.hf.space/chat"
payload = {
"message": "Hello!",
"history": []
}

res = requests.post(url, json=payload)
print(res.json()["response"])

```

---

## ⚠️ Notes

- Hugging Face Spaces may sleep after 48h of inactivity
- TinyLlama is selected for its speed — you can swap models as needed
- You can fork LocalMind and customize

---

## 🧩 Optional Additions

- Add `thumbnail.png` to display a banner in README
- Link your GitHub repo to Hugging Face
- Use `HF_HOME` instead of `TRANSFORMERS_CACHE` (for future-proofing)

---

🙌 Done!

You now have a fully self-hosted chatbot API — free, fast, and ready to integrate.

---

Let me know if you want this saved as a downloadable `.md` file or if you want me to add anything else!
```

If you want, I can prepare this as a downloadable file for you—just ask!

