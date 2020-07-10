prime = {2,3,5,7,11,13,17}
goal = (1,2,3,4,5,6,7,8,9)

all_states = {}
dist = 0
current_state = {goal:dist}

while current_state:
    next_state = {}
    dist += 1
    for state in current_state:
        lstate = list(state)
        for i in range(2):
            for j in range(3):
                d=1
