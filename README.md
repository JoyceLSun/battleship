<h2> Python Battleship Game </h2>
  
<p>This file contains a player vs. computer battleship game on a 5x5 gameboard, my final project for my Intro Programming class I took fall semester 
of freshman year(2020).</p>
  
<p><strong>User Guide: </strong></p>
<p>Users are prompted to enter the direction they would like to place their ship, then to pick a origin coordinate from which the ship will generate 
downwards or rightwards of. Based on the origin point selected, users can choose the length of the ship prompted by the program. The program will 
randomly generate a ship for the computer, and tell the player the length and direction of the ship. Each guess by the player will be signified with
an X in the computer board, and the computer guess (randomly generated) will be marked with an O. If the computer hits a part of the ship you have placed,
it will be signified with a capital delta (∆). If you hit a part of the computer's ship, it will also be signaled by a capital delta (∆). Whoever hits
the entire ship will be the winner, and the program will return number of turns. </p>

<p><strong>Debugging: </strong></p>
<p>Functions have been written to check user inputs. When prompted to determine ship placement direction, if inputs are not exactly "horizontal" or 
"vertical", the user will be prompted that this is not a valid option and that they must enter these exact terms. Use of .lower() could have been 
beneficial for marking out capitals. When picking coordinates, if the inputted value is not a number or not in range of the suggested numbers, the user 
will be prompted to enter a valid value. </p>

<p><strong>Future Fixes: </strong></p>
<p>Possible future fixes could be uploading the game to a better interface than the current IDLE shell. The game also does not prompt users if they would 
like to play again, which would be a nice feature to have. </p>
