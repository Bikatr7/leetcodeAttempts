## Bikatr7
## 2024-07-31
## 1105. Filling Bookcase Shelves (Medium)

## Description:

## You are given an array books where books[i] = [thickness_i, height_i] indicates the thickness and height of the ith book. You are also given an integer shelf_width.
## We want to place these books in order onto bookcase shelves that have a total width of shelf_width.
## We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth.
## Build another level of the shelf of the bookcase so that the total height of the bookcase increases by the maximum height of the books we jut put on the shelf.
## We repeat this process until there are no more books to place.
## Note that at each step of the above process, the order of the books we place is the same order as the given books array. 
## For example, if we have an ordered list of 5 books, we might place the first and second book on the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
## Return the minimum possible height that the total bookcase can be after placing shelves in this manner.

## Constraints:

## 1 <= books.length <= 1000
## 1 <= thickness_i <= shelf_width <= 1000
## 1 <= height_i <= 1000

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

## built-in libraries
import typing

class Solution:
    def minHeightShelves(self, books:typing.List[typing.List[int]], shelf_width:int) -> int:
        num_books = len(books)
        min_heights = [float('inf')] * (num_books + 1)
        min_heights[0] = 0
        
        for i in range(1, num_books + 1):
            current_width = 0
            current_height = 0
            
            for j in range(i - 1, -1, -1):
                book_width, book_height = books[j]
                current_width += book_width
                
                if(current_width > shelf_width):
                    break
                
                current_height = max(current_height, book_height)
                min_heights[i] = min(min_heights[i], min_heights[j] + current_height)
        
        return min_heights[num_books]

## Submission Code:
class Solution:
    def minHeightShelves(self, b, w):
        n = len(b)
        d = [float('inf')] * (n + 1)
        d[0] = 0
        for i in range(1, n + 1):
            h = wd = 0
            for j in range(i - 1, -1, -1):
                if (wd := wd + b[j][0]) > w:
                    break
                h = max(h, b[j][1])
                d[i] = min(d[i], d[j] + h)
        return d[n]