from typing import List
"""
Approach
----------------

1. Create a dictionary mapping the letters referring to morse code
2. Create a list to store the converted words 
3. Use string array
    3.1 Iterate each word in the list
    3.2 Iterate each character of the word and add the corresponding morse code
4. Add all converted codes into the list of converted words
5. Returns the count of unique morse code representations
"""

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_dict = {
        'a': ".-",
        'b': "-...",
        'c': "-.-.",
        'd': "-..",
        'e': ".",
        'f': "..-.",
        'g': "--.",
        'h': "....",
        'i': "..",
        'j': ".---",
        'k': "-.-",
        'l': ".-..",
        'm': "--",
        'n': "-.",
        'o': "---",
        'p': ".--.",
        'q': "--.-",
        'r': ".-.",
        's': "...",
        't': "-",
        'u': "..-",
        'v': "...-",
        'w': ".--",
        'x': "-..-",
        'y': "-.--",
        'z': "--.."
        }
        
        morse_code = [] 
        
        for word in words: 
            code = ""
            for char in word: 
                code += morse_dict[char]
            morse_code.append(code)
            
        return(len(set(morse_code)))