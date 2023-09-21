# bargain-boxing
### By Amy Reichhold

The purpose of the program is to minimize space by stacking as many boxes 
inside each other as possible. Given the number of boxes, the program will 
use the Ford-Fulkerson algorithm for Max-Flow to determine the minimum number 
of visible boxes remaining. 

## How to run bargain-boxing.py
On the command line, run the following command:
```
cat input_file | python3 bargain-boxing.py
```
The program will read the input file from standard input. Below is an example 
input file:
> 4
> 2 1 3
> 4 3 5
> 2 3 4
> 4 5 6

The first line in the file is the number of boxes and the following lines 
represent boxes and their dimensions. Once the minimum number of visible 
boxes is found, that number will be printed to standard output.


## Implementation
The program reads the input file specifying a bargain-boxing problem, and 
creates a directed graph representing the problem. The nodes of the graph 
represent boxes and a directed edge from box x to box y means that box x 
fits inside box y according to their respective dimensions. Ford-Fulkerson 
is run on the directed graph and will return the max flow, see the Max Flow 
section for more details. To find the minimum number of visible boxes, the 
max flow is subtracted from the number of boxes.


## Max Flow
The Maximum flow problem is an optimization problem that finds the maximum 
amount of flow that can be sent through a flow network. The flow network is 
a directed graph with a source node s, sink node t, and capacities on each 
edge that represents how much flow can be sent through it. The purpose is to 
find the maximum amount of flow that can be sent from the source to the sink, 
while adhering to the capacity constraints.
