# bargain-boxing
### By Amy Reichhold

## How to run bargain-boxing.py
On the command line, run the following command:
```
cat input_file | python3 bargain-boxing.py
```
The program will read the input file from standard input. The purpose of the
program is to minimize space by stacking as many boxes inside each other as
possible. Given the number of visible boxes, the program will use the
Ford-Fulkerson algorithm for Max-Flow to determine the minimum number of
visible boxes remaining. The input file denotes the number of boxes and the
dimensions of each box. Once the minimum number of boxes is found, the number
will be printed to standard output.


## Overview
The program creates a graph and runs the Ford-Fulkerson algorithm on the graph.
To create the graph, the program finds the vertices by reading and sorting
the box dimensions. To find the edges, the program connects two boxes with an
edge when a box fits inside another box. Next, create the graph and run
Ford-Fulkerson on the graph. The algorithm will return the max flow. To find
the minimum number of visible boxes, you subtract the max-flow from the
number of boxes.
