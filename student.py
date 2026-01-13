def calculate_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def main():
    name = "Veeresh"
    dept = "BCA"
    sem = 3
    m1, m2, m3 = 85, 90, 80

    avg = (m1 + m2 + m3) / 3
    grade = calculate_grade(avg)

    print("=== Student Grade Management System ===")
    print("Name       :", name)
    print("Department :", dept)
    print("Semester   :", sem)
    print("Marks      :", m1, m2, m3)
    print("Average    : {:.2f}".format(avg))
    print("Grade      :", grade)


if __name__ == "__main__":
    main()
