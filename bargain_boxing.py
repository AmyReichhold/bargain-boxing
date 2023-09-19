import sys

print_box_information = False

def Graph(boxes, g_prime_edges):
    vertices = []
    edges = []

    vertices.append(f's')
    vertices.append(f't')
    for i in range(len(boxes)):
        vertices.append(f'u_{i}')
        vertices.append(f'v_{i}')
        edges.append(('s', f'u_{i}'))
        edges.append((f'v_{i}', 't'))

    for i in g_prime_edges:
        edges.append((f'u_{i[0]}', f'v_{i[1]}'))

    capacity = [1 for i in range(len(edges))]
    flow = [0 for i in range(len(edges))]

    return vertices, edges

def get_neighbors_in_queue(queue, u, edges, capacity):
    neighbors = []
    for edge in edges:
        if u == edge[0] and capacity[edge] > 0:
            neighbors.append(edge[1])
        else:
            continue

    queue_neighbors = []
    for v in queue:
        if v in neighbors:
            queue_neighbors.append(v)
        else:
            continue

    return queue_neighbors

def dequeue_vertex_with_min_dist(queue, dist):
    min_dist = sys.maxsize
    vertex = None
    for u in queue:
        if dist[u] < min_dist:
            min_dist = dist[u]
            vertex = u
    if vertex is not None:
        queue.remove(vertex)
    return vertex

def shortest_path(network):
    Graph = network[0]
    capacity = network[1]
    source = network[2]
    terminus = network[3]

    vertices = Graph[0]
    edges = Graph[1]
    dist = {}
    prev = {}
    queue = []

    for v in vertices:
        dist[v] = len(edges)+1
        prev[v] = None
        queue.append(v)
    dist[source] = 0

    while queue:
        u = dequeue_vertex_with_min_dist(queue, dist)
        
        for v in get_neighbors_in_queue(queue, u, edges, capacity):
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    path = reconstruct_path_edges(prev, source, terminus)
    return path

def reconstruct_path_edges(prev, source, terminus):
    path_from_t = []

    current = terminus
    while prev[current] != None:
        path_from_t.append((prev[current], current))
        current = prev[current]

    return path_from_t

def get_residual_edges(edges):
    residual_edges = []

    for edge in edges:
        residual_edges.append(edge)
        residual_edges.append((edge[1], edge[0]))
    
    return residual_edges

def path_exists(network):
    path = shortest_path(network)

    return len(path) > 0

def Ford_Fulkerson(Graph, capacity, source, terminus):
    vertices = Graph[0].copy()
    edges = Graph[1].copy()
    flow = {}
    residual_capacity = {}

    # initialize flow for flow graph to be zero
    for edge in edges:
        flow[edge] = 0
    
    # sets up residual graph edges
    residual_edges = get_residual_edges(edges)

    # initialize all the edges in the residual graph to be zero
    for edge in residual_edges:
        residual_capacity[edge] = 0

    # set the edges from the flow graph in the residual graph to have the 
    # same capacity as in the flow graph
    for edge in edges:
        residual_capacity[edge] = capacity[edge]

    residual_graph = (vertices, residual_edges)
    residual_network = (residual_graph, residual_capacity, source, terminus)

    while path_exists(residual_network):
        path = shortest_path(residual_network)
        path_residual_capacity = min([residual_capacity[edge] for edge in path])

        for edge in path:
            if edge in edges:
                flow[edge] = flow[edge] + path_residual_capacity
            
            # this differs from the wikipedia pseudo code 
            # and instead follows what we learned in class
            residual_capacity[edge] = \
                    residual_capacity[edge] - path_residual_capacity

            residual_capacity[(edge[1], edge[0])] = \
                    residual_capacity[(edge[1], edge[0])] + \
                    path_residual_capacity

    flow_from_source = 0
    flow_into_terminus = 0
    for edge in edges:
        if edge[0] == source:
            flow_from_source += flow[edge]
        elif edge[1] == terminus:
            flow_into_terminus += flow[edge]

    return flow_into_terminus

def fits(box1, box2):
    # Checks if each dimension for box1 is less than the corresponding 
    # dimensions for box2. If so, box1 fits inside box2.
    for (fst, snd) in zip(box1, box2):
        if fst >= snd:
            return False
    return True

def main():
    # get the file from standard input
    input_file = sys.stdin.readlines()

    # get the number of boxes
    n = int(input_file[0])

    box_dims = []
    for line in input_file[1:]:
        # get the individual boxes and sort them
        dim = tuple(sorted([int(x) for x in line.strip().split(' ')]))
        box_dims.append(dim)
        
    # checks to see if one box will fit in another box.
    # if so, add the boxes as a tuple to the g_prime_edges list
    g_prime_edges = []
    for one in range(len(box_dims)):
        dim_one = box_dims[one]
        for two in range(len(box_dims)):
            dim_two = box_dims[two]
            if fits(dim_one, dim_two):
                g_prime_edges.append((one, two))
            else:
                continue

    # set up the graph
    G = Graph(box_dims, g_prime_edges)
    edges = G[1]

    # sets up flow and capacity for flow graph
    capacity = {}
    for edge in edges:
        capacity[edge] = 1

    # find the max flow on the graph with Ford-Fulkerson algorithm
    max_flow = Ford_Fulkerson(G, capacity, 's', 't')

    # the number of visible boxes is: the number of boxes (n) minus the 
    # max-flow returned by the Ford-Fulkerson algorithm
    visible_boxes = n - max_flow

    # prints the number of boxes and lists the boxes (dimensions sorted)
    if print_box_information:
        print(f'Number of Boxes - {n}')
        print('Boxes - Sorted Dimensions')
        for i in range(len(box_dims)):
            print(f'{i} - {str(box_dims[i])}')
        print(f'Visible Boxes - {visible_boxes}')
    else:
        # just prints the number of boxes visible
        print(visible_boxes)

    return None

if __name__ == '__main__':
    main()
