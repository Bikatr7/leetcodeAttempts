// Start of Selection
// Kaden Bilyeu (Bikatr7)
// 2024-09-16
// 884. Uncommon Words from Two Sentences (Easy)

// Description:
// A sentence is a string of single-space separated words where each word consists only of lowercase letters.
// A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
// Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

// Example 1:
// Input: s1 = "this apple is sweet", s2 = "this apple is sour"
// Output: ["sweet","sour"]
// Explanation: The word "sweet" appears only in s1, while the word "sour" appears only in s2.

// Example 2:
// Input: s1 = "apple apple", s2 = "banana"
// Output: ["banana"]

// Constraints:
// 1 <= s1.length, s2.length <= 200
// s1 and s2 consist of lowercase English letters and spaces.
// s1 and s2 do not have leading or trailing spaces.
// All the words in s1 and s2 are separated by a single space.

// Topics: Hash Table, String, Counting

import java.util.*;

class Solution
{
    public String[] uncommonFromSentences(String s1, String s2)
    {
        Map<String, Integer> wordCount = new HashMap<>();
        for (String word : s1.split(" "))
        {
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }
        for (String word : s2.split(" "))
        {
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }

        List<String> result = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : wordCount.entrySet())
        {
            if (entry.getValue() == 1)
            {
                result.add(entry.getKey());
            }
        }

        return result.toArray(new String[result.size()]);
    }
}
