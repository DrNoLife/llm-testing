from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """  i go almost daily to buy kebab fromthe same place (close both to myhouse and my work place)
  There is this underpaid andoverworked arab guy that makes thekebab145 KB JPG
  I always tip 50%
  He always packs my kebab with moremeat than usual
  He also knows how i like it, big and spicy with all thesauces and a diet pepsi
  He gets verry happy when he sees me and he calls me,boss,, and ,brother,
  Today i was sad af but the ,hello boss, the usual?"Made me feel better
  Kebab heals people
"""
summary = summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False)

print(summary[0]["summary_text"])
