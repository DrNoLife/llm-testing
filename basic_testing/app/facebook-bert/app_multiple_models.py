from transformers import pipeline

# Array of model names
models = ["facebook/bart-large-cnn", "allenai/led-base-16384", "t5-small", "sshleifer/distilbart-cnn-12-6"]

# Your text data
ARTICLE = """
be me
sad depressed
suicidal thoughts
dad notices
thinks it's because of my siblings
takes me to the planetarium every other
falls asleep every time because he's working 12h a day
he always takes me
still alive
thanks dad
"""

# Calculate input length
input_length = len(ARTICLE.split())

# Loop through each model
for model_name in models:
    print(f"Model: {model_name}")
    
    # Initialize the summarizer with the current model
    summarizer = pipeline("summarization", model=model_name)
    
    # Set max_length to half of input_length or to some other fraction
    max_length = int(input_length / 2)

    if input_length > 250:
        max_length = 100
    elif input_length > 150:
        max_length = 75
    else:
        max_length = 50

    # Generate the summary
    try:
        summary = summarizer(ARTICLE, max_length=max_length, min_length=40, do_sample=False)
        print(summary[0]["summary_text"])
    except Exception as e:
        print(f"Error: {e}")
    
    print("-" * 80)  # Print a separator line

