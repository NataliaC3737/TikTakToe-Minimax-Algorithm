# TikTakToe-Minimax-Algorithm
# In this project you will see the code for a TikTakToe game with 3 types of game modes 
# 1. Player1 vs Player2 
# 2. Player vs RandomAI 
# 3. Player vs MinimaxAI

"""
To beging with I will explain how I've made the algorithm. The program is about the game of Tic-Tac-Toe with 3 game modes. The first one is Player vs Player, where the user can play on the same computer with a friend; the second one is Player vs Random AI, in which the user plays against an AI that makes random moves; and lastly, Player vs Impossible AI, in this mode, the user plays against an AI that blocks their moves and, if it sees a possibility to win, it wins. This last game mode was programmed with a minimax algorithm, which operates with a decision tree that evaluates the possible moves to determine the best move.

Additionally, I used the pygame interface to make everything look better, like in the original game. For the game board, I used a 3x3 matrix of zeroes that collects the players' values (1 or 2) in a list of immutable tuples (the tuples are indices in this program).
"""