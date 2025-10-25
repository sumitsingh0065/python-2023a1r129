'''Write a Python function called group_anagrams(words) 
that takes a list of strings and returns a list of groups, 
where each group contains words that are anagrams of each other.'''

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
def group_anagrams(words):
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
            return list(anagram_dict.values())
        print(group_anagrams(words))
