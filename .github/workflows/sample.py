import random

def get_random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "I'm reading a book on the history of glue. I just can’t seem to put it down!",
    ]
    return random.choice(jokes)

random_joke = get_random_joke()
print(random_joke)
