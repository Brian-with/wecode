def get_even_numbers():
    even_list = []
    for i in range(50+1):
        if i % 2 == 0:
            even_list.append(i)
        else:
            continue
    return even_list

print(get_even_numbers())