**Status:** Archive (code is provided as-is, no updates expected)

# CAH-Gen - A Cards Against Humanity response generator

## Description

This python program will generate response cards, it uses ~5k actual response cards from CAH to generate a markov chain based on them, that is then fed into a GPT-Neo model that spits out a few unique respones

## Requirements

Before running the script you need to install **Python v3.7** and run the following from within the folder you cloned the repo to:

> python -m pip install -r requirements.txt

This will install the following required libraries:

- HuggingFace Transformers
- Torch
- Markovify

## Usage

Inside the script you can change several parameters:

> # Parameters
> cardfile = "responses.txt"
> #gptmodel = "EleutherAI/gpt-neo-125M"
> gptmodel = "EleutherAI/gpt-neo-1.3B"
> #gptmodel = "EleutherAI/gpt-neo-2.7B"
> response_length = 500

**cardfile** - the file containing the list of base responses from Cards Against Humanity
**gptmodel** - uncomment the one you want to use, each model consumes more memory and takes longer to run than the last
**response_length** - the number of tokens returns in the response, higher numbers will create more responses per run but also take longer to do so

## Card File

**response.txt** - this file contains ~5k actual response cards, feel free to add your own responses to this file to add some data of your own. You can also replace this file entirely with a response list of your own if you have a source you would prefer to use.

## License

None, feel free to use this as you see fit. You don't have to give me credit or anything. I wrote this in an evening based on a whim.