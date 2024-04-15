# Tic Tac Toe with AI

This repo contains my implementation of project Tic Tac Toe with AI from JetBrains Academy (https://hyperskill.org/projects/82)

### Usage

To run the game type ```python tictactoe.py```.

After being prompted user can type either ```exit``` to exit the program or ```start {player} {player}```, where ```{player}``` is one of the 4 possibilities:

* ```user``` - human player
* ```easy``` - easy difficulty AI that makes only random moves
* ```medium``` - medium difficulty AI that 1) checks if it can win with a move 2) checks if it can prevent opponent from winning 3) otherwise makes a random move
* ```hard``` - hard difficulty AI that uses minimax algorithm (https://en.wikipedia.org/wiki/Minimax) to play optimal moves

In case ```user``` player is selected user will have to type cooridnates of the cell where they want to place their symbol.  
Coordinates of the game grid are as follows:  
(1, 1) (1, 2) (1, 3)  
(2, 1) (2, 2) (2, 3)  
(3, 1) (3, 2) (3, 3)

The game always starts with the ```X```.
