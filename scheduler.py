#!/usr/bin/env python3 

import json, sys
from collections import defaultdict

#  scheduler combines helper functions to get the correct order
def scheduler(path: str):
    classes = parse_json(path) # parses JSON (result is a dict)
    names, prereqs = [x['name'] for x in classes], [x['prerequisites'] for x in classes]
    uniqueClasses = names + [x for sublist in prereqs for x in sublist if x not in names]
    indexes = [] 
    for c in classes: 
        for prereq in c['prerequisites']:
            indexes.append([uniqueClasses.index(c['name']), uniqueClasses.index(prereq)])
        if not c['prerequisites']:
            indexes.append([uniqueClasses.index(c['name']), -1])
    return get_order(uniqueClasses, indexes)

# parse_json takes in a path and outputs the contents of the corresponding JSON file 
def parse_json(path: str): 
    try: 
        with open(path) as contents:
            f = json.load(contents)
    except IOError: 
        print("Error: Invalid path to JSON")
        sys.exit()
    if (type(f) != list):
        print("Error: Bad input")
        sys.exit()
    return f 

# get_order returns the sorted order using a dfs algorithm. 
def get_order(classes, numbered_classes):
    adj_list = defaultdict(list)
    [adj_list[src].append(dest) for dest, src in numbered_classes]

    result = []
    no_cycles = True
    marker = {i: 1 for i in range(len(classes))}

    def dfs(node):
        nonlocal no_cycles
        if not no_cycles:
            return

        marker[node] = 2
        if node in adj_list:
            for neighbor in adj_list[node]:
                if marker[neighbor] == 1:
                    dfs(neighbor)
                elif marker[neighbor] == 2:
                    no_cycles = False
        marker[node] = 3
        result.append(classes[node])
    
    [dfs(vertex) for vertex in range(len(classes)) if marker[vertex] == 1]
    if no_cycles:
        [print(x) for x in result[::-1]]

scheduler(sys.argv[1])