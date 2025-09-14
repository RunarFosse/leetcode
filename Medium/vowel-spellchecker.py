# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Create a translation table for making vowels a wildcard "*"
        wildcard_translation = {ord(c): ord("*") for c in "aeiou"}

        # Then, store the words in three different dictionaries
        dictionary, case_dictionary, wildcard_dictionary = {}, {}, {}
        for word in wordlist:
            # Add the word to the normal dictionary
            dictionary[word] = word
        
            # If it doesn't exist, add the lowercase into the case dictionary
            key = word.lower()
            if key not in case_dictionary:
                case_dictionary[key] = word
            
            # If it doesn't exist, add the wildcard word into the wildcard dictionary
            key = key.translate(wildcard_translation)
            if key not in wildcard_dictionary:
                wildcard_dictionary[key] = word
        
        # At last, iterate the queries, returning first occuring word
        words = []
        for query in queries:
            word = ""
            if query in dictionary:
                word = dictionary[query]
            
            query = query.lower()
            if word == "" and query in case_dictionary:
                word = case_dictionary[query]
            
            query = query.translate(wildcard_translation)
            if word == "" and query in wildcard_dictionary:
                word = wildcard_dictionary[query]
            
            words.append(word)
    
        # Finally, return the resulting words
        return words


# We store them in a dictionary, with the key as the search string, value a the word.
# To ensure case-insensitivity, we store the key in lower case.
# To work with vowel-errors, we encode the vowels as a special "*" character.