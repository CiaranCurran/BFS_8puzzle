import timeit

class problem(object):
    def __init__(self, start_state, goal_state):
        problem.start_state = start_state
        problem.goal_state = goal_state
    
    #performs action on state and returns new state
    def result(self, state, action):
        for i in range(len(state)):
            if state[i] == 0:
                if action == 'up':
                    tmp = state[i-3]
                    state[i-3] = state[i]
                    state[i] = tmp
                    return state
                elif action == 'down':
                    tmp = state[i+3]
                    state[i+3] = state[i]
                    state[i] = tmp
                    return state
                elif action == 'right':
                    tmp = state[i+1]
                    state[i+1] = state[i]
                    state[i] = tmp
                    return state
                elif action == 'left':
                    tmp = state[i-1]
                    state[i-1] = state[i]
                    state[i] = tmp
                    return state
        
    #returns list of possible actions that can be made from current state    
    def actions(self, state):
        for i in range(len(state)):
            if state[i] == 0:
                if i == 0:
                    return ['down', 'right']
                elif i == 1:
                    return ['down', 'left', 'right']
                elif i == 2:
                    return ['down', 'left']
                elif i == 3:
                    return ['up', 'down', 'right']
                elif i == 4:
                    return ['up', 'down', 'left', 'right']
                elif i == 5:
                    return ['up', 'down', 'left']
                elif i == 6:
                    return ['up', 'right']
                elif i == 7:
                    return ['up', 'left', 'right']
                elif i == 8:
                    return ['up', 'left']

    #returns true if the current state is a goal state
    def goalTest(self, state):
        if state == problem.goal_state:
            return True
        else:
            return False 
        
class node(object):
    def __init__(self, state, parent, action, path_cost, layer):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.layer = layer
      
#generates a child node
def childNode(problem, parent, action):
    return node(problem.result(list(parent.state), action), parent, action, 0, (parent.layer+1))

#prints solution to console
def solution(child):
    actions = []
    states = []
    actions.append(child.action)
    states.append(child.state)
    while True:
        parent = child.parent
        if parent.state == start_state:
            print(list(reversed(actions)))
            print(list(reversed(states)))
            return
        states.append(parent.state)
        actions.append(parent.action)
        child = parent
            

start_state = input("Enter start configuration [x1,...,x8]: ")#initialise the problem 
start_state = [int(s) for s in start_state.split(',')]
#TEST start_state = [0,5,2,1,4,3,7,8,6]
goal_state = [1,2,3,4,5,6,7,8,0] #default goal state


problem = problem(start_state, goal_state)
start_node = node(list(problem.start_state),None,None,0,0)
frontier = [start_node]
explored = []
goal_found = False
layer = 0;

start_time = timeit.default_timer()#begin timer

#BFS ALGORITHM
while goal_found==False:
   
 
    if frontier == []:
        print("Failure")
        break

    current_node = frontier.pop(0)    #initialise frontier
    explored.append(list(current_node.state))   #add the new node's state to the explored set
    
    for action in problem.actions(current_node.state):
        child = childNode(problem, current_node, action)
      
        if list(child.state) not in explored and all(node.state != child.state for node in frontier):
            if problem.goalTest(list(child.state)):
                print("SOLUTION FOUND")
                solution(child)
                goal_found = True
                break
            
            frontier.append(child)
    
    if child.layer > layer:
        print("Graph has reached layer:", layer)
        layer = child.layer

#End timer || benchmarking
elapsed = timeit.default_timer() - start_time
print("Execution Time:", elapsed)                           
