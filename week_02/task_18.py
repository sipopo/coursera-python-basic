a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

isEqual_1 = (a1 == a2) and (b1 == b2) and (c1 == c2)
isEqual_2 = (a1 == a2) and (b1 == c2) and (c1 == b2)
isEqual_3 = (a1 == b2) and (b1 == c2) and (c1 == a2)
isEqual_4 = (a1 == b2) and (b1 == a2) and (c1 == b2)
isEqual_5 = (a1 == c2) and (b1 == a2) and (c1 == b2)
isEqual_6 = (a1 == c2) and (b1 == b2) and (c1 == a2)

isLarger_1 = (a1 > a2) and (b1 > b2) and (c1 > c2)
isLarger_2 = (a1 > a2) and (b1 > c2) and (c1 > b2)
isLarger_3 = (a1 > b2) and (b1 > c2) and (c1 > a2)
isLarger_4 = (a1 > b2) and (b1 > a2) and (c1 > b2)
isLarger_5 = (a1 > c2) and (b1 > a2) and (c1 > b2)
isLarger_6 = (a1 > c2) and (b1 > b2) and (c1 > a2)

isSmaller_1 = (a1 < a2) and (b1 < b2) and (c1 < c2)
isSmaller_2 = (a1 < a2) and (b1 < c2) and (c1 < b2)
isSmaller_3 = (a1 < b2) and (b1 < c2) and (c1 < a2)
isSmaller_4 = (a1 < b2) and (b1 < a2) and (c1 < b2)
isSmaller_5 = (a1 < c2) and (b1 < a2) and (c1 < b2)
isSmaller_6 = (a1 < c2) and (b1 < b2) and (c1 < a2)

isEqual = isEqual_1 or isEqual_2 or isEqual_3
isEqual = isEqual or isEqual_4 or isEqual_5 or isEqual_6

isSmaller = isSmaller_1 or isSmaller_2 or isSmaller_3
isSmaller = isSmaller or isSmaller_4 or isSmaller_5 or isSmaller_6

isLarger = isLarger_1 or isLarger_2 or isLarger_3
isLarger = isLarger or isLarger_4 or isLarger_5 or isLarger_6

if isEqual:
    print("Boxes are equal")
elif isSmaller:
    print("The first box is smaller than the second one")
elif isLarger:
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
