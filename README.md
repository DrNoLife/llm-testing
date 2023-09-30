# Summarization and Title Generation API
This repository contains a Flask API that provides endpoints for text summarization and title generation using Hugging Face's Transformers library.

## Features
* Summarization of provided text using different models.
* Title generation for a given story or text snippet.
* Dockerized for easy setup and deployment.
* Supports live code reloading for easier development.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
* Docker
* Docker Compose
### Setup
1. Clone this repository:
```bash
git clone https://github.com/DrNoLife/llm-testing.git
cd llm-testing
```
2. Build the Docker image:
```bash
docker compose up --build
```

Note: I decided to omit the ```-d``` flag, to make logging easier.

3. Start the Docker container:
```bash
docker-compose up
```

Now the API should be running at http://localhost:5002.

## Usage
The API provides two main endpoints: ```/summarize``` and ```/generate-title```.

### Summarization
Send a POST request to ```/summarize``` with a JSON payload containing the Text and Model properties:

```json
{
    "Text": "Your text here...",
    "Model": "facebook/bart-large-cnn"
}
```

Note: The default model for summarization is ```sshleifer/distilbart-cnn-12-6```.

### Title Generation
Send a POST request to ```/generate-title``` with a JSON payload containing the Text and Model properties:

```json
{
    "Text": "Your text here...",
    "Model": "gpt2"
}
```

Note: The default model for title generation is ```gpt2```.

### Available Models

Users can specify different models for summarization and title generation tasks by providing the `Model` property in the JSON payload. Below are some of the models that can be specified:

1. `facebook/bart-large-cnn`
2. `sshleifer/distilbart-cnn-12-6`
3. `philschmid/bart-large-cnn-samsum`
4. `google/pegasus-xsum`
5. `google/pegasus-cnn_dailymail`
6. `facebook/bart-large-xsum`
7. `google/pegasus-large`
8. `tuner007/pegasus_summarizer`
9. `google/bigbird-pegasus-large-arxiv`
10. `google/bigbird-pegasus-large-bigpatent`
11. `gpt2` - Generative Pre-trained Transformer 2

Provide the model name exactly as shown (case-sensitive) in the `Model` property of the JSON payload when making a request to the API.

## Development
The Flask application is set up to reload automatically on code changes. Just save your files and the application will reload.

## Deployment
Remember to switch Flask to production mode by setting the ```FLASK_ENV``` environment variable to production in the Dockerfile before deploying:

```Dockerfile
ENV FLASK_ENV=production
```

---

TL;DR: Testing repo for a bunch of text generation and whatnot. It's useful for code samples, and leaning how this stuff works.
