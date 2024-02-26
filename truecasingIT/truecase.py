import re
import os

class Truecaser:

    def __init__(self):
        wordforms_path = os.path.join(os.path.dirname(__file__), "wordforms.txt")
        punct_path = os.path.join(os.path.dirname(__file__), "punct.txt")

        with open(wordforms_path) as f:
            self.surface_forms = f.read().splitlines()
        with open(punct_path) as f:
            self.sent_pos = f.read().splitlines()


    def truecase(self, text):
        """
        Process a string by truecasing the words based on the provided surface forms and punctuation marks.

        Args:
            text (str): The input text to be processed.

        Returns:
            str: The processed text with truecased words.
        """
        
        for exc in [("Â", "'"), ("Ã", "à")]:
            text = text.replace(exc[0], exc[1])
        sentences = re.split(r'(?<=[.!?])\s*', text)
        truecased_sentences = []
        for sentence in sentences:
            words = sentence.split()
            truecased_words = []
            for i, word_with_punctuation in enumerate(words):
                
                # Separate word from punctuation
                word, punctuation = "", ""
                indices = []
                for idx, char in enumerate(word_with_punctuation):
                    if char in self.sent_pos:
                        punctuation += char
                    else:
                        word += char
                
                # Check if the word without punctuation is in the Italian words list
                if i == 0 or word.lower() not in self.surface_forms:
                    # Capitalize the first word of the sentence or words not in the Italian word list
                    truecased_word = word.capitalize()
                else:
                    # Lowercase words that don't need to be capitalized
                    truecased_word = word.lower()
                
                # Add back the punctuation mark, if any
                # one exception if the word is in single quotes
                if punctuation == "''":
                    truecased_word = f"'{truecased_word}'"
                else: 
                    truecased_word += punctuation


                truecased_words.append(truecased_word)
            truecased_sentence = ' '.join(truecased_words)
            truecased_sentences.append(truecased_sentence)
        
        final = ' '.join(truecased_sentences).replace("l' ", "l'")
        return final