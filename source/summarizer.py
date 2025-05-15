from transformers import AutoTokenizer, pipeline

model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
summarizer = pipeline("summarization", model=model_name, tokenizer=tokenizer)

def summarize_text(text, max_length=150, min_length=40):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=1024)
    input_ids = inputs["input_ids"]
    truncated_text = tokenizer.decode(input_ids[0], skip_special_tokens=True)
    summary = summarizer(truncated_text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
