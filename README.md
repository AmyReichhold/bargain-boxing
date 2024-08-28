# bargain-boxing
### By Amy Reichhold

The purpose of the program is to minimize space by stacking as many boxes 
inside each other as possible. Given the number of boxes, the program will 
use the Ford-Fulkerson algorithm for Max-Flow to determine the minimum number 
of visible boxes remaining. 

There are several implementation in various languages. Each implementation
is contained in a self identifying directory (e.g. `java` for the Java version,
`python` for the Python version).

## How to run Python bargain-boxing
On the command line, run the following command from the `python` directory:
```
cat input_file | python3 bargain-boxing.py
```
where `input_file` is the desired input file name.
The program will read the input file from standard input. Below is an example 
input file:
> 4\
> 2 1 3\
> 4 3 5\
> 2 3 4\
> 4 5 6

The first line in the file is the number of boxes and the following lines 
represent boxes and their dimensions. Once the minimum number of visible 
boxes is found, that number will be printed to standard output.

Below is a sample run of the program using an input from the `inputs` 
directory in this repository: 
```
$ cd python
$ cat ../inputs/sampleInput.txt | python3 bargain_boxing.py
1
```
The output of `1` shows that all boxes listed in `sampleInput.txt` can fit 
inside one another, such that only one box remains visible.

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
