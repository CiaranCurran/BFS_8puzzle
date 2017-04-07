import timeit
start_time = timeit.default_timer()
class problem(object):
    def __init__(self, start_state, goal_state):
        problem.start_state = start_state
        problem.goal_state = goal_state
    
    def result(self, state, action):
        #conditionals that perform appropriate action on state
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
        
        
    def actions(self, state):
        for i in range(len(state)):
            if state[i] == 0:
                if i == 0:
                    return ['right', 'down']
                elif i == 1:
                    return ['left', 'right', 'down']
                elif i == 2:
                    return ['left', 'down']
                elif i == 3:
                    return ['right', 'up', 'down']
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


    def goalTest(self, state):
        if state == problem.goal_state:
            return True
        else:
            return False 
        
class Node(object):
	def __init__(self, state, parent, action, path_cost):
		self.state = state
		self.parent = parent
		self.action = action
		self.path_cost = path_cost
		
#generates a child node
def childNode(problem, parent, action):
    return Node(problem.result(list(parent.state), action), parent, action, 0)

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
            
    
#initialise the problem
start_state = [0,1,4,5,2,3,6,7,8]
goal_state = [1,4,2,6,8,3,7,0,5]

#initialise frontier
problem = problem(start_state, goal_state)
node = Node(list(problem.start_state),None,None,0)
frontier = [node]
explored = []
goal_found = False

#BFS ALGORITHM
while goal_found==False:
    if frontier == []:
        print("Failure")
        break
    
    node = frontier.pop()
    explored.append(list(node.state))
    
    for action in problem.actions(node.state):
        child = childNode(problem, node, action)
        print("From:",node.state, action, "move->", child.state)
        if list(child.state) not in explored and all(node.state != child.state for node in frontier):
            if problem.goalTest(list(child.state)):
                print("SOLUTION FOUND")
                solution(child)
                goal_found = True
                break
            frontier.append(child)

#benchmarking
elapsed = timeit.default_timer() - start_time
print("Execution Time", elapsed)                             
