from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Your text data
text_data = """  i go almost daily to buy kebab fromthe same place (close both to myhouse and my work place)
  There is this underpaid andoverworked arab guy that makes thekebab145 KB JPG
  I always tip 50%
  He always packs my kebab with moremeat than usual
  He also knows how i like it, big and spicy with all thesauces and a diet pepsi
  He gets verry happy when he sees me and he calls me,boss,, and ,brother,
  Today i was sad af but the ,hello boss, the usual?"Made me feel better
  Kebab heals people"""


# Instruction for summary generation
instruction = "Generate a description/summary for the following story: "

# Combine the instruction and text data
input_text = instruction + " " + text_data

# Tokenize the input text
inputs = tokenizer(input_text, return_tensors='pt', max_length=512, truncation=True)

# Generate the summary
# Increase max_length to avoid the max_length warning and runtime error
# Pass the attention_mask to avoid the attention mask warning
summary_ids = model.generate(
    inputs['input_ids'], 
    attention_mask=inputs['attention_mask'],
    num_beams=4, 
    min_length=10, 
    max_length=250,  # Increased max_length
    length_penalty=2.0
)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print(summary)

