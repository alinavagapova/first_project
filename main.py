import numpy as np
# test_list = np.random.randint(0, 20, 10)
# print(test_list)
# вопрос - как создать произвольного размера список?
test_list = np.random.choice(20, 10)
print(test_list)
for i in range(len(test_list)):
    if (test_list[i]) % 2 == 0:
        print(i, f'{test_list[i]} is even')
    else:
        print(i, f'{test_list[i]} is odd')
