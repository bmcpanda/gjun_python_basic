def calculate_third_edge(first_edge, second_edge, include_long_edge=False):
    possible_answer = list()
    if include_long_edge == False:
        answer = (first_edge * first_edge + second_edge * second_edge) ** 0.5
        possible_answer.append(answer)
    elif first_edge != second_edge:
        longer_one = max(first_edge, second_edge)
        shorter_one = min(first_edge, second_edge)
        answer_2 = (longer_one * longer_one - shorter_one * shorter_one) ** 0.5
        possible_answer.append(answer_2)
    return possible_answer 

if __name__ == '__main__' :
    print(calculate_third_edge(3, 4))
    print(calculate_third_edge(5, 12))
    print(calculate_third_edge(13, 12, True))