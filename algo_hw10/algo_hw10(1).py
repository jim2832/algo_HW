def do_backtrack(a, inputs):
    c = []
    if (is_a_solution(a, inputs)):
        process_solution(a, inputs)
    else:
        construct_candidate(a, inputs, c)
        for i in c:
            a.append(i)
            do_backtrack(a, inputs)
            a.pop()

def process_solution(a:list, inputs:list):
    solution.append(a.copy())

def is_a_solution(a, inputs):
    return len(a) == len(inputs)

def construct_candidate(a, inputs, c):
    distinct = set()
    s = inputs.copy()
    for i in a:
        a.remove(i)
    for j in s:
        distinct.add(j)
    for d in distinct:
        c.append(d)

solution = []    
do_backtrack([],[1, 2, 2, 1])
print(sorted(solution))