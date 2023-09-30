from transformers import T5Tokenizer, T5ForConditionalGeneration

max_length = 512

# Load the tokenizer and model
tokenizer = T5Tokenizer.from_pretrained('t5-large', model_max_length=max_length, legacy=False) 
model = T5ForConditionalGeneration.from_pretrained('t5-large')

# Example text data
text_data = """> i go almost daily to buy kebab fromthe same place (close both to myhouse and my work place)
> There is this underpaid andoverworked arab guy that makes thekebab145 KB JPG
> I always tip 50%
> He always packs my kebab with moremeat than usual
> He also knows how i like it, big and spicy with all thesauces and a diet pepsi
> He gets verry happy when he sees me and he calls me,boss,, and ,brother,
> Today i was sad af but the ,hello boss, the usual?"Made me feel better
> Kebab heals people"""

text_data = text_data.replace("> ", "").replace(",,", '"')

inputs = tokenizer("Create a brief and short description about the following text. You are under no circumstances to just tell the story in other words. You are to give a summary, but a very brief one: " + text_data, return_tensors="pt", max_length=max_length, truncation=True)

title_ids = model.generate(inputs['input_ids'], num_beams=4, min_length=10, max_length=80, length_penalty=2.0)
title = tokenizer.decode(title_ids[0], skip_special_tokens=True)

print(title)
