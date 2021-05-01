"""
# 1-1.별 찍기(1)
for i in range(5):
    for a in range(i + 1):
        print("*",end="")
    print()

# *            줄 = 1    별 = 1
# **           줄 = 2    별 = 1 2
# ***          줄 = 3    별 = 1 2 3
# ****         줄 = 4    별 = 1 2 3 4
# *****        줄 = 5    별 = 1 2 3 4 5
"""

"""
# 1-2.별 찍기(2)
for i in range(5):
    for n in range(4 - i):
        print(" ", end="")
    for a in range(i + 1):
        print("*", end="")
    print()
    
#     *          줄 = 1    공백 = 1 2 3 4    별 = 1
#    **          줄 = 2    공백 = 1 2 3      별 = 1 2
#   ***          줄 = 3    공백 = 1 2        별 = 1 2 3
#  ****          줄 = 4    공백 = 1          별 = 1 2 3 4
# *****          줄 = 5    공백 =            별 = 1 2 3 4 5
"""

"""
# 1-3.별 찍기(3)
for i in range(1,6):
    for n in range(5 - i):
        print(" ", end="")
    for a in range(i * 2 - 1):
        print("*",end="")
    print()
    
#     *            줄 = 1    공백 = 1 2 3 4    별 = 1
#    ***           줄 = 2    공백 = 1 2 3      별 = 1 2 3
#   *****          줄 = 3    공백 = 1 2        별 = 1 2 3 4 5
#  *******         줄 = 4    공백 = 1          별 = 1 2 3 4 5 6 7
# *********        줄 = 5    공백 =            별 = 1 2 3 4 5 6 7 8 9 
"""

"""
# 1-3.별 찍기(3)
for i in range(1,6):
    for n in range(5 - i):
        print(" ", end="")
    for a in range(i * 2 - 1):
        print("*",end="")
    print()
for i in range(1,6):
    for n in range(0 + i):
        print(" ", end="")
    for a in range(9 - i * 2):
        print("*",end="")
    print()
#     *            줄 = 1    공백 = 1 2 3 4    별 = 1
#    ***           줄 = 2    공백 = 1 2 3      별 = 1 2 3
#   *****          줄 = 3    공백 = 1 2        별 = 1 2 3 4 5
#  *******         줄 = 4    공백 = 1          별 = 1 2 3 4 5 6 7
# *********        줄 = 5    공백 =            별 = 1 2 3 4 5 6 7 8 9
#  *******         줄 = 6    공백 = 1          별 = 1 2 3 4 5 6 7
#   *****          줄 = 7    공백 = 1 2        별 = 1 2 3 4 5
#    ***           줄 = 8    공백 = 1 2 3      별 = 1 2 3
#     *            줄 = 9    공백 = 1 2 3 4    별 = 1
"""

"""
# 1-4. 별 찍기(4)
for i in range(4):
    for a in range(i + 1):
        print("*", end="")
    for n in range(5 - i * 2):
        print(" ", end="")
    for b in range(i + 1):
        if i + 1 >= 4:
            print("***", end="")
            break
        print("*", end="")
    print()
for i in range(3):
    for a in range(3 - i):
        print("*", end="")
    for b in range(1 + i * 2):
        print(" ", end="")
    for n in range(3 - i):
        print("*", end="")
    print()

# *     *             줄 = 1    별 = 1        공백 = 1 2 3 4 5   별 = 1
# **   **             줄 = 2    별 = 1 2      공백 = 1 2 3       별 = 1 2 
# *** ***             줄 = 3    별 = 1 2 3    공백 = 1           별 = 1 2 3
# *******             줄 = 4    별 = 1 2 3 4  공백 =             별 = 1 2 3
# *** ***             줄 = 5    별 = 1 2 3    공백 = 1           별 = 1 2 3
# **   **             줄 = 6    별 = 1 2      공백 = 1 2 3       별 = 1 2
# *     *             줄 = 7    별 = 1        공백 = 1 2 3 4 5   별 = 1
"""