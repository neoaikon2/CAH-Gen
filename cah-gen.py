from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import markovify
import time

# Parameters
cardfile = "responses.txt"
#gptmodel = "EleutherAI/gpt-neo-125M"
gptmodel = "EleutherAI/gpt-neo-1.3B"
#gptmodel = "EleutherAI/gpt-neo-2.7B"
response_length = 150

print("Loading " + cardfile + " and generating Markov Chain...")
# Import ~5k response cards
with open(cardfile) as f:
	text = f.read()
# Generate the Markov Chain model
markov = markovify.Text(text)
time.sleep(1)
print("Done!\r\n")

print("Loading "+gptmodel+" into RAM...")
# Setup the GPT model
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained(gptmodel, torch_dtype=torch.float16, pad_token_id=tokenizer.eos_token_id, low_cpu_mem_usage=True)
print("Done!\r\n")

def CreatePrompt():
	tmpPrompt = ""
	# Use the markov chain to generate a bunch of unique response cards
	for i in range(75):
		while(True):
			text = markov.make_short_sentence(50)
			# Make sure it isn't None, which is a no-no
			if(type(text) == type("")):
				break
		# Build the prompt
		tmpPrompt = tmpPrompt + text + "\r\n"
	# Return the completed set of responses
	return tmpPrompt
	
def CreateResponses(prompt):
	# Generate the input IDs for the prompt
	input_ids = tokenizer(prompt, return_tensors="pt").input_ids	
	bad_ids = tokenizer(["cock","faggot"]).input_ids
	print("Generating response cards...\r\n")
	# Use GPT to generate some responses
	gen_tokens = model.generate(input_ids, bad_words_ids=bad_ids, do_sample=True, temperature=1.23, repetition_penalty=2.0, top_k=100, max_length=(len(prompt)/4)+response_length)
	# Decode the result
	return tokenizer.batch_decode(gen_tokens)[0]

def PrintResponses(gen_text):	
	text = gen_text[len(prompt):len(gen_text)-13].split("\n")
	for i in range(len(text)-1):
		print(text[i])
	input("\r\nPress any key to generate a next set...")

while(True):
	# Create a unique response set
	#print("Creating Prompt...")
	prompt = CreatePrompt()
	#print("Creating unique response cards...")
	# Use GPT to generate some responses using ML
	gen_text = CreateResponses(prompt)
	# Print the result
	PrintResponses(gen_text)
