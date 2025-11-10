def count_mortal_rabbits(n, m):
    if n == 1:
        return 0, 1
    elif n == 2:
        return 1, 0
    else:
        mature_prev, offspring_prev = count_mortal_rabbits(n - 1, m)
        if n > m:
            mature_m_ago, offspring_m_ago = count_mortal_rabbits(n - m, m)
            deaths_this_month = offspring_m_ago
        else:
            deaths_this_month = 0

        mature_this_month = offspring_prev + mature_prev - deaths_this_month
        offspring_this_month = mature_prev

        return mature_this_month, offspring_this_month


if __name__ == "__main__":
    mature_rabbit, offspring_rabbit = count_mortal_rabbits(100, 18)
    total_rabbits = mature_rabbit + offspring_rabbit
    print(total_rabbits)
