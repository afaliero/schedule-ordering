# Algorithm 
* I chose a graph-based approach using depth first search to solve this problem. Each class is a vertex, and the relationship between classes and prerequisites are edges. The program considers all possible paths originating from the first visited node before moving on to other nodes. This way, all nodes stemming from this first node have the first node as a prerequisite. 

# scheduler and parse_json
* To implement this algorithm, I first created the functions parse_json and scheduler. Parse_json takes in a file path provided by the user and loads the contents of the corresponding JSON file. 
* The scheduler function takes the loaded file contents and converts it to a list (called indexes) of [a, b] pairs where a = an integer corresponding to a class and b = an integer corresponding to a prerequisite for that class. I did this because it is easier to deal with class-prerequisite integer pairs in the get_order function than it is to deal with a dictionary that has a variable number of prerequisites for each class.
    * I assign integer values to classes by creating a list of unique classes (called uniqueClasses), which is also used to determine the total number of unique classes (useful in get_order)

# get_order
* Next, I created a function get_order that takes in the "indexes" and "uniqueClass" lists described above. 
* I initialize an adjacency list using the edge pairs (b -> a) given by the indexes input list. I also initialize a stack (result) that contains the topologically sorted order of classes in the graph. 
* I then run a DFS to check if nodes have been visited using the no_cycle boolean variable and integers 1-3 as markers. If a node has not been processed, I recurse. 
* Once a node's neighbors are processed, I add the node to the result stack. The stack is useful for ordering, as adding a node to the stack can be done with the knowledge that all classes that require the node as prerequisites have already been pushed to the stack. 
* I then return the stack from the top down. 

# Time Complexity 
* Time complexity = O(2V + E), where V represents the number of vertices (classes) and E represents the number of edges (class-prerequisite pairs). Because we keep track of visited nodes, we only need to process them all once. The extra V comes from creating a new list in the scheduler function. 

* Note: I included test outputs in ./test_output.txt. Ran tests on math.json, physics.json, and falseorder.json (an edge case).
