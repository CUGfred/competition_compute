import itertools
import copy


# in board, index 0 means win count, index 1 means lose count

def run_competiton(competition, board):
    win_case  = copy.deepcopy(board)    
    lose_case = copy.deepcopy(board)  

    win_case[competition[0]][0] += 1
    win_case[competition[1]][1] += 1

    lose_case[competition[0]][1] += 1
    lose_case[competition[1]][0]  += 1

    return win_case, lose_case

def compute_competitons(competitions, results):
    for competition in competitions:
        stage_result = []
        for result in results:
            win_case, lose_case = run_competiton(competition=competition, board=result)
            stage_result.append(win_case)
            stage_result.append(lose_case)
        
        results = stage_result
    return results



board = {'gam':[0, 3], 'tes':[1, 2], 'drx':[2, 1], 'rge':[3,0]}
teams = list(board.keys())
competitions = list(itertools.combinations(teams, 2))
win, lose = run_competiton(competition=competitions[0], board=board)
results = [board]
ret = compute_competitons(competitions=competitions, results=results)
ret = sorted(ret, key=lambda x:x['tes'][0], reverse=True)
for i, element in enumerate(ret):
    print("{} result is {}".format(i+1, element.items()))

print("all result in {} situations.".format(len(ret)))



