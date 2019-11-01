"""This function smoothing deep list"""


def smoothing_list(inp_list: list) -> list:
    smooth = []
    for i in inp_list:
        if type(i) == list:
            smooth.extend(smoothing_list(i))
        else:
            smooth.append(i)
    return smooth


if __name__ == '__main__':
    print(smoothing_list([1, [2, 3, [4]], 5]))  # [1, 2, 3, 4, 5]
