student_scores = [75, 84, 66, 99, 51, 65]


def get_grade_stats(scores):
    """
    FIGURE THIS OUT. MASTER THIS TYPE OF THINKING
    :param scores:
    :return mean and std_dev tuple:
    """
    # Calculate the arithmetic mean
    mean = sum(student_scores) / len(scores)

    # Calculate the standard deviation
    tmp = 0
    for i in range(len(scores)):
        tmp += (scores[i] - mean) ** 2
    std_dev = (tmp / len(scores)) ** 0.5

    # Package and return average, standard deviation in a tuple
    return mean, std_dev


# Unpack tuple
average, standard_deviation = get_grade_stats(student_scores)

print('Average score:', average)
print('Standard deviation:', standard_deviation)
