given_list = [1, 2, 3, 4, 5]

def compute(a_list):
    new_list = []

    for index, value in enumerate(a_list):
        original_list = a_list
        original_int = original_list[index]
        original_list[index] = 1

        result = 1
        for x in original_list:
            result = result * x

        new_list.append(result)

        original_list[index] = original_int

    return new_list, value

r = compute(given_list)
print(r)
