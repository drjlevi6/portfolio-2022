Solves this puzzle: Given a string of asterisks and pipes, count the asterisks contained within pipes.

usage: python3 ContainerPuzzle.py

The Story ("ethically hacked", edited without permission from www.hackerrank.com):

A certain company would like to know how much inventory exists in their closed inventory compartments. Given a string s consisting of items as "*" and closed compartments as an open and close "|", an array of starting indices startindices, and an array of ending indices endlndices (all 1-based), determine the number of items in closed compartments within the substring between the two indices, inclusive.

•	An item is represented as an asterisk ('*' =
	ascii decimal 42)

•	A compartment is represented as a pair of
	pipes that may or may not have items
	between them ('|' = ascii decimal 124).

Example
s='|**|*|*'
startlndices = [1, 1]
endlпdices = [5, б]

The string has a total of 2 closed compartments, one with 2 items and one with 1 item. For the first pair of indices, (1, 5), the substring is '|**|*'. There are 2 items in a compartment. For the second pair of indices, (1, 6), the substring is ' |**|*|' and there are 2 + 1 = 3 items in compartments. Both of the answers are returned in an array, [2, 3]. 

My partial solution handles entire strings only (no indices).
