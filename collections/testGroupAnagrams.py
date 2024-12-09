import unittest

from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for istr in strs:
        sorted_str = ''.join(sorted(istr))
        anagrams[sorted_str].append(istr) if sorted_str in anagrams else anagrams.update({sorted_str: [istr]})

    output = list(anagrams.values())
    print(output)
    return output


class TestGroupAnagrams(unittest.TestCase):
    def test_group_anagrams(self):
        input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertEqual(group_anagrams(input_strings), expected_output)

    def test_empty_input(self):
        input_strings = []
        expected_output = []
        self.assertEqual(group_anagrams(input_strings), expected_output)

    def test_single_string(self):
        input_strings = ["hello"]
        expected_output = [["hello"]]
        self.assertEqual(group_anagrams(input_strings), expected_output)

    def test_no_anagrams(self):
        input_strings = ["abc", "def", "ghi"]
        expected_output = [["abc"], ["def"], ["ghi"]]
        self.assertEqual(group_anagrams(input_strings), expected_output)

    def test_mixed_anagrams(self):
        input_strings = ["abcd", "dcba", "efgh", "hgef", "ijk", "kji"]
        expected_output = [["abcd", "dcba"], ["efgh", "hgef"], ["ijk", "kji"]]
        self.assertEqual(group_anagrams(input_strings), expected_output)


if __name__ == "__main__":
    unittest.main()


""" testGroupAnagrams (unittest.loader._FailedTest) ... ERROR

======================================================================
ERROR: testGroupAnagrams (unittest.loader._FailedTest)
----------------------------------------------------------------------
ImportError: Failed to import test module: testGroupAnagrams
Traceback (most recent call last):
  File "/usr/lib/python3.8/unittest/loader.py", line 436, in _find_test_path
    module = self._get_module_from_name(name)
  File "/usr/lib/python3.8/unittest/loader.py", line 377, in _get_module_from_name
    __import__(name)
  File "/config/workspace/tests/testGroupAnagrams.py", line 3, in <module>
    from config.groupAnagrams import group_anagrams
  File "/config/workspace/config/groupAnagrams.py", line 14, in <module>
    print(group_anagrams(input_strings))
  File "/config/workspace/config/groupAnagrams.py", line 7, in group_anagrams
    anagrams[hash(sorted_str)].append(istr) if sorted_str in anagrams else anagrams.update({sorted_str: [str]})
TypeError: unhashable type: 'list'


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1) """
