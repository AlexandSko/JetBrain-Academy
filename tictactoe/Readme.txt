This is a TicTacToe game on Python3!


Nowadays, this game is known all over the world. Each country may have its own version of the name,

sometimes the rules are different, but the meaning of the game remains the same.

Below are the main rules that may be familiar to you since childhood.

Tic-tac-toe is a game played by two players on a 3x3 field where the duel takes place.

One of the players plays as 'X', and the other player is 'O'. 'X' plays first, then the 'O' side plays, and so on.

The first player that writes 3 'X' or 3 'O' in a straight line (including diagonals) wins.


_____________________________________________________________________________________________________________________________

Description of game field:

Suppose the bottom left cell has the coordinates (1, 1) and the top right cell has the coordinates (3, 3) like in this table:

(1, 3) (2, 3) (3, 3)
(1, 2) (2, 2) (3, 2)
(1, 1) (2, 1) (3, 1)

Keep in mind that the first coordinate goes from left to right and the second coordinate goes from bottom to top.

Also, notice that coordinates start with 1 and can be 1, 2 or 3.





The program is working in the following way:


1) Prints an empty 3x3 field with cells at the beginning of the game (before the user's move).

2) Creates a game loop where the program asks the user to enter the cell coordinates of his next move.

3) Then the user should input 2 numbers that represent the cell on which user wants to make his X or O.

4) The program analyzes the move for correctness and shows a field with the changes if everything is ok.

   But what if the user enters incorrect coordinates?

   The user could enter symbols instead of numbers or enter coordinates representing occupied cells.

   The program prevent all of that by checking a user's input and catching possible exceptions.

	Possible exceptions:

	-"This cell is occupied! Choose another one!" - if the cell is not empty;

	-"You should enter numbers!" - if the user enters other symbols;

	-"You should enter two numbers!" - if the user enters other amount of symbols;

	-"Coordinates should be from 1 to 3!" - if the user goes beyond the field.
	

5) Then the program outputs the table including the user's most recent move.

6) Ends the game when someone wins or there is a draw.

7) Outputs the final result after the end of the game.


Good luck gaming!





_____________________________________________________________________________________________________________________________

References:

    1) https://hyperskill.org/projects/73?track=2

    2) https://hyperskill.org/projects/73/stages/399/implement

    3) https://hyperskill.org/projects/73/stages/400/implement

    4) https://hyperskill.org/projects/73/stages/401/implement

    5) https://hyperskill.org/projects/73/stages/402/implement

    6) https://hyperskill.org/projects/73/stages/403/implement
