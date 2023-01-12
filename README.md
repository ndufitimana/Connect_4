
## TL;DR
This repository contains the implementation of the Connect-4 Game using both the Monte Carlo Tree Search and Minimax Algorithms. It was a capstone project in Artificial Intelligence at Swarthmore College completed in partnership with my colleague Kelvin Darfour. We ran experiments comparing the performance of these algorithms using different parameters and the findings can be found in the project.pdf file in the Paper folder. The repository contains various player options for the game including human, random, minimax, pruning, and MCTS players, each with their own keywords. Users can run the game on the terminal by using the python command `python3 PlayGame.py connect [player1 keyword] [Player2 keyword] [Player1 arguments] [Player2 Arguments] [Other game arguments]` with various arguments available depending on the players chosen. The run.py file provided also allows users to run all the experiments we did on MCTS and Minmax, however it may take over 24 hours to run all the experiments.
### Demo: MCTS vs Minmax
MCTS is the yellow player and is given 1500 rollouts while minmax limited at a depth of 4.
<img src="https://recordit.co/rvnWq2vmyy" width=200><br>

## Full Details


This repository contains the implementation of both Monte Carlo Tree Search and 
Minimax Algorithms that play the Connect-4 Game on the terminal. 
This project was a partnerned project with friend, Kelvin Darfour from Swarthmore College. 
It was presented as a a Capstone Project  in CS063, Artificial Intelligence, at Swarthmore College

We ran several experiments on these algorithms to compare their performance 
using different parameters, namely rollouts for MCTS and search depth for Minimax.       

If interested in the  findings, read the paper under the folder Paper and filename project.pdf or compile the project.tex file.        

We have several players that can play Connect-4 with their keywords in ():       
* Random Player(random): Plays random moves in Connect-4.           
* Human Player(human): Allows a human player to play Connect-4 from the terminal.        
* Minimax Player(minmax): A Player that uses Minimax algorithm to play Connect-4.         
* Pruning Player(pruning): A Player that uses the Alpha-Beta Pruning version of MCTS to Play Connect-4.      
* MCTS Player(mcts): A Player that uses Monte Carlo Tree Search Algorithm to Play Connect-4.         

If you are running the game on another computer that is not Swarthmore College CS Machines,
make sure that you have all the requirements outlined in the requirements.txt file.        

To get started, follow run a command to the terminal following this pattern:        

`python3 PlayGame.py connect [player1 keyword] [Player2 keyword] [Player1 arguments] [Player2 Arguments] [Other game arguments]`

Several arguments are available depending on the players you choose. Here are the main arguments for each player listed above:        

* Human Player: No other arguments.        
* Random Player: No other arguments.          
* Minimax and Pruning: depth(-d1 if player1 and -d2 if player2). The default depth is 4.       
* MCTS: number of rollouts(-a1 if player 1 and -a2 if player two). The default number of rollouts is 1000.         
* if you add the -games argument, you specify how many games to play.        

Check the file PlayGame.py for a list of all the available arguments. Here are a few examples of applying the commands to play the Connect-4 using different Players 
make sure you are under the correct directory:            

The following command plays one game between the random player and a human player        

`python3 PlayGame.py connect random human`

The next command plays 5 games between minmax and mcts where minmax is using a depth of 4 
and mcts is using 5000 rollouts.          

`python3 PlayGame.py connect minmax mcts -d1 4 -a2 5000 -games 5`      

This last command plays 1 game between mcts and human where mcts is using 1500 rollouts       

`python3 PlayGame.py connect mcts human  -a1 1500`        


We also provided a file called run.py  which contains a script that allows you to run all the experiments we
ran on MCTS and Minmax.       

Before you run, make it an executable by running the following command        

`chmod u+x run.py` if you are on the cs machines or `chmod +x run.py` if you are on your own computer and have all the requirements installed.       

After making it an executable, simply run the following command: `./run.py`          
it will output the results of the game alongside the arguments used in the game in a file called result.txt.
Be patient as it might take over 24 hours to run all our experiments.  




