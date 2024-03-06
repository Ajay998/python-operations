"""
Given an expression string exp, write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in the given expression.

Example:

Input: exp = “[()]{}{[()()]()}”
Output: Balanced
Explanation: all the brackets are well-formed

Input: exp = “[(])”
Output: Not Balanced
Explanation: 1 and 4 brackets are not balanced because
there is a closing ‘]’ before the closing ‘(‘

Follow the steps mentioned below to implement the idea:

Declare a character stack (say temp).
Now traverse the string exp.
If the current character is a starting bracket ( ‘(‘ or ‘{‘  or ‘[‘ ) then push it to stack.
If the current character is a closing bracket ( ‘)’ or ‘}’ or ‘]’ ) then pop from the stack and if the popped character is the matching starting bracket then fine.
Else brackets are Not Balanced.
After complete traversal, if some starting brackets are left in the stack then the expression is Not balanced, else Balanced.
"""