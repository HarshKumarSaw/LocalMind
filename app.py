import os
from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import uvicorn

os.environ["HF_HOME"] = "/tmp/hf_cache"
app = FastAPI()

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()

class ChatInput(BaseModel):
    message: str
    history: list = []

@app.post("/chat")
async def chat(req: ChatInput):
    prompt = ""
    for user, bot in req.history:
        prompt += f"User: {user}\nBot: {bot}\n"
    prompt += f"User: {req.message}\nBot:"

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

    req.history.append((req.message, response))
    return {"response": response, "history": req.history}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)