import random

# Lists of determiners, nouns, verbs, and prepositions
determiners = ["A", "The", "One", "Some", "Many"]
nouns = ["girl", "bird", "child", "dogs", "rabbits", "cats"]
verbs = ["talked", "drinks", "run", "laugh", "will talk"]
prepositions = ["for", "off", "on", "above", "at", "about"]

# Function to get a random element from a list
def get_random_element(word_list):
    return random.choice(word_list)

# Function to generate a prepositional phrase
def get_prepositional_phrase():
    preposition = get_random_element(prepositions)
    determiner = get_determiner()
    noun = get_noun()
    return f"{determiner} {noun} {preposition}"

# Functions to get determiner, noun, and verb
def get_determiner():
    return get_random_element(determiners)

def get_noun():
    return get_random_element(nouns)

def get_verb():
    return get_random_element(verbs)

# Function to make a sentence
def make_sentence():
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    prep_phrase = get_prepositional_phrase()
    return f"{determiner} {noun} {verb} {prep_phrase}."

# Main function
def main():
    num_sentences = int(input("Enter the number of sentences to generate: "))
    for _ in range(num_sentences):
        sentence = make_sentence()
        print(sentence)

if __name__ == "__main__":
    main()
