def count_rabbits(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        offspring = count_rabbits(n - 2, k) * k
        mature_rabbit = count_rabbits(n - 1, k)
        return offspring + mature_rabbit


print(count_rabbits(29, 4))
