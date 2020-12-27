
def computegrade(tmp_score):
    if 0.0 <= tmp_score <= 1.0:
        if tmp_score >= 0.9:
            return 'A'
        if tmp_score >= 0.8:
            return 'B'
        if tmp_score >= 0.7:
            return 'C'
        if tmp_score >= 0.6:
            return 'D'
        return 'F'
    return 'Bad score'

input_score = input('Enter score: ')
score = 0.0

try:
    score = float(input_score)
except ValueError:
    print('Bad score')
    quit()
    
grade = computegrade(score)
print(grade)