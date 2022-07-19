# # 5 Написать функцию которая будет считать дискриминант (через lambda и def)
# def discriminant(a: int, b: int, c: int) -> int:
#     d = b**2 - 4*a*c
#     return d
#
# print(discriminant(5,6,7))
# # result = discriminant(6, 3, 5)
# # print(result)

discriminant = lambda a, b, c: b**2 - 4*a*c
print(discriminant(5, 6, 7))