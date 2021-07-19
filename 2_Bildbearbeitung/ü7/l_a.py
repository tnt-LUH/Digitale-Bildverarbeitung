i_00 = 1
i_10 = 2
i_01 = 3
i_11 = 4


# 1)
i_new_bilinear = 0.2 * (0.7 * 1 + 0.3 * 2) + 0.8 * (0.7 * 3 + 0.3 * 4)
i_new_nn = 3
print(i_new_bilinear, i_new_nn)

# 2)
i_new_bilinear = 0 * (1 * 1 + 0 * 2) + 1 * (1 * 3 + 0 * 4)
i_new_nn = 3
print(i_new_bilinear, i_new_nn)

# 3)
i_new_bilinear = 0.5 * (0.5 * 1 + 0.5 * 2) + 0.5 * (0.5 * 3 + 0.5 * 4)
i_new_nn = 4  # Multiple solutions! Here: Ceil
print(i_new_bilinear, i_new_nn)
