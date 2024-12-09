from collections import defaultdict

def group_anagrams_1(strs):
    anagrams = defaultdict(list)
    for istr in strs:
        sorted_str = sorted(istr)
        anagrams[sorted_str].append(istr) if sorted_str in anagrams else anagrams.update({sorted_str: [str]})
    return list(anagrams.values())

def group_anagrams_working(strs):
    anagrams = defaultdict(list)
    for istr in strs:
        anagrams[str(sorted(istr))].append(istr)
    return list(anagrams.values())

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for istr in strs:
        anagrams[''.join(sorted(istr))].append(istr)
    return list(anagrams.values())



# Example usage
input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(input_strings))