i_00 = 1  # New position: (x=0.5, y=0.5)
i_10 = 2  # New position: (x=1.5, y=0.5)
i_01 = 3  # New position: (x=0.5, y=1.5)
i_11 = 4  # New position: (x=1.5, y=1.5)


# 1)
i_new_bilinear = 0.5 * (0.5 * 1 + 0.5 * 2) + 0.5 * (0.5 * 3 + 0.5 * 4)
i_new_nn = 4  # Multiple solutions! Here: Ceil
print(i_new_bilinear, i_new_nn)

# 2)
# This solution is depending on the border behaviour! If no border behaviour is defined, there is not bilinear solution!
i_new_bilinear = ...
i_new_nn = 1
print(i_new_nn)
