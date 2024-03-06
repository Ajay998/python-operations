"""
The RPS world championship is here. Here two players A and B play the game. You need to determine who wins.
Both players can choose moves from the set {R,P,S}.
The game is a draw if both players choose the same item.
The winning rules of RPS are given below:

Rock crushes scissor
Scissor cuts paper
Paper envelops rock
Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains single line of input that contains two characters sidebyside. These characters denote the moves of players A and B respectively.

Output:
For each testcase, in a newline, print the winner. If match is draw, print 'DRAW'.

Constraints:
1<= T <= 50

Example:
Input:
7
RR
RS
SR
SP
PP
PS
RP

Output:
DRAW
A
B
A
DRAW
B
B
"""

choices = {'R','P','S'}
a_input = int(input("Enter input: "))
for i in range(a_input):
    player_one_move = str(input("Enter the player1 choice: "))
    player_two_move = str(input("Enter the player2 choice: "))
    if player_one_move == player_two_move:
        print("DRAW")
    elif (player_one_move == 'R' and player_two_move == 'S') or (player_one_move == 'P' and player_two_move == 'R') or (player_one_move == 'S' and player_two_move == 'P'):
        print("A")
    else:
        print("B")