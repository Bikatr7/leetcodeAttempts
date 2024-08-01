## Bikatr7
## 2024-08-01
## 2678. Number of Senior Citizens (Easy)

## Description:

## Your are given a 0-indexed array of strings details.
## Each element of details provides information about a given passenger compressed into a string of length 15.
## The system is such that:
## The first ten characters consist of the phone number of passengers
## The next character denotes the gender of the person.
## The following two characters are used to indicate the age of the person
## The last two characters determine the seat allocated to the person
## Return the number of passengers who are strictly more than 60 years old.

## Constraints:

## 1 <= details.length <= 100
## details[i].length == 15
## details[i] consists of digits from '0' to '9'
## details[i][10] is either 'M' or 'F' or 'O'
## The phone number an seat numbers of each passenger is unique

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

## built-in libraries
import typing

class Solution:
    def countSeniors(self, details:typing.List[str]) -> int:
        return len([detail for detail in details if int(detail[11:13]) > 60])
    
## Submission Code:
class Solution:
    def countSeniors(self, d):
        return len([d for d in d if int(d[11:13]) > 60])