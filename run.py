#!/usr/bin/env python
import sys
import subprocess

# The name of the Python program to run
program_name = "/home/kdarfou1/cs63/project-kdarfou1-ndufiti1/PlayGame.py"



# The command line arguments to pass to the program
args = [
["connect", "mcts", "minmax", "-games",  "10", "-a1", "10", "-d2", "2"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "15", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "20", "-d2", "2"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "25", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "30", "-d2", "2"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "35", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "40", "-d2", "2"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "45", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "50", "-d2", "2" ], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "60", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "65", "-d2", "2"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "70", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "75", "-d2", "2"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "80", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "85", "-d2", "2"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "90", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "95", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "100", "-d2", "2"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "200" , "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "500" , "-d2", "2"],["connect", "mcts", "minmax", "-games",  "10", "-a1", "1000", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "1500", "-d2", "2"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "2000", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "4000", "-d2", "2"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "6000", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "8000", "-d2", "2"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "10000", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "15000", "-d2", "2"],["connect", "mcts", "minmax", "-games",  "10", "-a1", "20000", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "25000", "-d2", "2"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "30000", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "35000", "-d2", "2"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "40000", "-d2", "2"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "45000", "-d2", "2"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "50000", "-d2", "2"],


["connect", "mcts", "minmax", "-games",  "10", "-a1", "10"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "15"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "20"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "25"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "30"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "35"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "40"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "45"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "50"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "60"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "65"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "70"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "75"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "80"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "85"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "90"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "95"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "100"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "200"],["connect", "mcts", "minmax", "-games",  "10", "-a1", "500"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "1000"],["connect", "mcts", "minmax", "-games",  "10", "-a1", "1500"], 
["connect", "mcts", "minmax", "-games",  "10", "-a1", "2000"],["connect", "mcts", "minmax", "-games",  "10", "-a1", "4000"], 
["connect", "mcts", "minmax", "-games",  "10", "-a1", "6000"],["connect", "mcts", "minmax", "-games",  "10", "-a1", "8000"], 
["connect", "mcts", "minmax", "-games",  "10", "-a1", "10000"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "15000"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "20000"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "25000"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "30000"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "35000"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "40000"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "45000"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "50000"],


["connect", "mcts", "minmax", "-games",  "10", "-a1", "10", "-d2", "6"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "15", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "20", "-d2", "6"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "25", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "30", "-d2", "6"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "35", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "40", "-d2", "6"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "45", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "50", "-d2", "6" ], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "60", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "65", "-d2", "6"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "70", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "75", "-d2", "6"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "80", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "85", "-d2", "6"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "90", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "95", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "100", "-d2", "6"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "200" , "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "500" , "-d2", "6"],["connect", "mcts", "minmax", "-games",  "10", "-a1", "1000", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "1500", "-d2", "6"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "2000", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "4000", "-d2", "6"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "6000", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "8000", "-d2", "6"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "10000", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "15000", "-d2", "6"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "20000", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "25000", "-d2", "6"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "30000", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "35000", "-d2", "6"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "40000", "-d2", "6"],
["connect", "mcts", "minmax", "-games",  "10", "-a1", "45000", "-d2", "6"], ["connect", "mcts", "minmax", "-games",  "10", "-a1", "50000", "-d2", "6"],



["connect", "mcts", "pruning", "-games",  "10", "-a1", "10", "-d2", "2"], ["connect", "mcts",  "pruning", "-games",  "10", "-a1", "15", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "20", "-d2", "2"], ["connect", "mcts",  "pruning", "-games",  "10", "-a1", "25", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "30", "-d2", "2"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "35", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "40", "-d2", "2"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "45", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "50", "-d2", "2" ], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "60", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "65", "-d2", "2"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "70", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "75", "-d2", "2"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "80", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "85", "-d2", "2"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "90", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "95", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "100", "-d2", "2"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "200" , "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "500" , "-d2", "2"],["connect", "mcts", "pruning", "-games",  "10", "-a1", "1000", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "1500", "-d2", "2"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "2000", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "4000", "-d2", "2"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "6000", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "8000", "-d2", "2"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "10000", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "15000", "-d2", "2"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "20000", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "25000", "-d2", "2"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "30000", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "35000", "-d2", "2"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "40000", "-d2", "2"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "45000", "-d2", "2"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "50000", "-d2", "2"],


["connect", "mcts", "pruning", "-games",  "10", "-a1", "10"], ["connect", "mcts",  "pruning", "-games",  "10", "-a1", "15"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "20"], ["connect", "mcts",  "pruning", "-games",  "10", "-a1", "25"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "30"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "35"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "40"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "45"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "50"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "60"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "65"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "70"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "75"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "80"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "85"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "90"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "95"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "100"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "200"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "500"],["connect", "mcts", "pruning", "-games",  "10", "-a1", "1000"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "1500"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "2000"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "4000"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "6000"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "8000"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "10000"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "15000"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "20000"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "25000"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "30000"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "35000"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "40000"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "45000"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "50000"],


["connect", "mcts", "pruning", "-games",  "10", "-a1", "10", "-d2", "6"], ["connect", "mcts",  "pruning", "-games",  "10", "-a1", "15", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "20", "-d2", "6"], ["connect", "mcts",  "pruning", "-games",  "10", "-a1", "25", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "30", "-d2", "6"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "35", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "40", "-d2", "6"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "45", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "50", "-d2", "6" ], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "60", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "65", "-d2", "6"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "70", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "75", "-d2", "6"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "80", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "85", "-d2", "6"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "90", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "95", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "100", "-d2", "6"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "200" , "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "500" , "-d2", "6"],["connect", "mcts","pruning", "-games",  "10", "-a1", "1000", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "1500", "-d2", "6"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "2000", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "4000", "-d2", "6"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "6000", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "8000", "-d2", "6"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "10000", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "15000", "-d2", "6"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "20000", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "25000", "-d2", "6"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "30000", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "35000", "-d2", "6"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "40000", "-d2", "6"],
["connect", "mcts", "pruning", "-games",  "10", "-a1", "45000", "-d2", "6"], ["connect", "mcts", "pruning", "-games",  "10", "-a1", "50000", "-d2", "6"]      
]


for arg in args:
        # Run the program and capture the output
        process = subprocess.Popen(["python3", program_name] + arg, stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE)
        
print(f"Program {program_name} has ended running for the specified arguments")

