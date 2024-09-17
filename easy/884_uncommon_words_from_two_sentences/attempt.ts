// Kaden Bilyeu (Bikatr7)
// 2024-09-16
// 884. Uncommon Words from Two Sentences (Easy)
//
// Description:
// A sentence is a string of single-space separated words where each word consists only of lowercase letters.
// A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
// Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
//
// Example 1:
// Input: s1 = "this apple is sweet", s2 = "this apple is sour"
// Output: ["sweet","sour"]
// Explanation: The word "sweet" appears only in s1, while the word "sour" appears only in s2.
//
// Example 2:
// Input: s1 = "apple apple", s2 = "banana"
// Output: ["banana"]
//
// Constraints:
// 1 <= s1.length, s2.length <= 200
// s1 and s2 consist of lowercase English letters and spaces.
// s1 and s2 do not have leading or trailing spaces.
// All the words in s1 and s2 are separated by a single space.
//
// Topics: Hash Table, String, Counting
//
// Hints:
// Hint 1: Use a hash map to count the frequency of each word in both sentences.
// Hint 2: Collect the words that appear exactly once.

function uncommonFromSentences(s1: string, s2: string): string[] 
{
    const wordCount: { [key: string]: number } = {};

    [...s1.split(" "), ...s2.split(" ")].forEach(word => 
    {
        wordCount[word] = (wordCount[word] || 0) + 1;
    });

    return Object.keys(wordCount).filter(word => wordCount[word] === 1);
}
