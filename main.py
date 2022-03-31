from sys import exit

def anagram(word1, word2):
    while True:
        if len(word1) == len(word2):
            for x in range(len(word1)):
                if word1[x] == word2[x]:
                    if word1[-1] == word1[x]:
                        print("The words are anagrams.")
                        exit()
                    continue
                else:
                    break        
        print("The words are't anagrams.")
        exit()

text1 = list(input("Type your first word: ").upper().strip())
text2 = list(input("Type your second word: ").upper().strip())

anagram(text1, text2)