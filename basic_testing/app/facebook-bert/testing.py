from transformers import BartForConditionalGeneration, BartTokenizer

# Load the tokenizer and model
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

# Example text data
text_data = "Your text data goes here."

# Tokenize Your Data
inputs = tokenizer(text_data, max_length=1024, return_tensors='pt', truncation=True)

# Generate summary
summary_ids = model.generate(inputs['input_ids'], num_beams=4, min_length=30, max_length=250, length_penalty=2.0)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print(summary)
