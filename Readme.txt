
This is a TicTacToe game on Python3!

First one of you moves as X, and then the other one moves as O.


Description

I divided the field into cells.

Suppose the bottom left cell has the coordinates (1, 1) and the top right cell has the coordinates (3, 3) like in this table:

(1, 3) (2, 3) (3, 3)
(1, 2) (2, 2) (3, 2)
(1, 1) (2, 1) (3, 1)



Objectives

The program should ask to enter the coordinates where the user wants to make a move.

Keep in mind that the first coordinate goes from left to right and the second coordinate goes from bottom to top. Also, notice that coordinates start with 1 and can be 1, 2 or 3.

But what if the user enters incorrect coordinates? The user could enter symbols instead of numbers or enter coordinates representing occupied cells. You need to prevent all of that by checking a user's input and catching possible exceptions.




Then the user should input 2 numbers that represent the cell on which user wants to make his X or O. (9 symbols representing the field would be on the first line and these 2 numbers would be on the second line of the user input)

The program should also check user input. If the user input is unsuitable, the program should ask him to enter coordinates again.

So, you need to output a field from the first line of the input and then ask the user to enter a move. Keep asking until the user enters coordinate that represents an empty cell on the field and after that output the field with that move. You should output the field only 2 times - before the move and after a legal move.



The program is working in the following way:

Prints an empty 3x3 field with cells at the beginning of the game (before the user's move).

Creates a game loop where the program asks the user to enter the cell coordinates of his next move, 
analyzes the move for correctness and shows a field with the changes if everything is ok.
Analyze user input and show messages in the following situations:
-"This cell is occupied! Choose another one!" - if the cell is not empty;
-"You should enter numbers!" - if the user enters other symbols;
-"Coordinates should be from 1 to 3!" - if the user goes beyond the field.
Then output the table including the user's most recent move.
Ends the game when someone wins or there is a draw.
Outputs the final result after the end of the game.

Good luck gaming!

