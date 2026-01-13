from student import calculate_grade

def test_grade_S():
    assert calculate_grade(95) == "S"

def test_grade_A():
    assert calculate_grade(85) == "A"

def test_grade_B():
    assert calculate_grade(70) == "B"

def test_grade_F():
    assert calculate_grade(30) == "F"
