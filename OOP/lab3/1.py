def add_score(
    subject_score: dict[str, int], 
    subject: str, 
    score: int
):
    subject_score[subject] = score
    return subject_score
    
def calc_average_score(subject_score: dict[str, int]):
    return f'{sum(subject_score.values()) / len(subject_score):.2f}'