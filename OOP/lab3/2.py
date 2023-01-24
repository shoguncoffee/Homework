def add_score(
    subject_score: dict[str, dict[str, int]], 
    student: str, 
    subject: str, 
    score: int
):
    subject_score.setdefault(student, {})[subject] = score
    return subject_score
    
def calc_average_score(subject_score: dict[str, dict[str, int]]):
    return {
        student: f'{sum(subjects.values()) / len(subjects):.2f}'
        for student, subjects in subject_score.items()
    }