from transformers import AutoTokenizer, AutoModelForCausalLM

# Load LLaMA model and tokenizer
MODEL_NAME = "TroyDoesAI/RAG-Qwen2.5-7B"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, trust_remote_code=True)

def generate_response_with_context(query, retrieved_data):
    """
    Generate a response using LLaMA, augmented with retrieved data.
    """
    # Build the prompt with retrieved context
    context = "\n".join([f"- {item['content']}" for item in retrieved_data])
    prompt = f"""
    User Query: "{query}"

    Relevant Data:
    {context}

    Provide a helpful response based on the user's query and the data provided above.
    """

    # Generate response
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=500, temperature=0.7)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
