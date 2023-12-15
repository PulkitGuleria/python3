list1 = input("data1: ").split(",")
list2 = input("data2: ").split(",")
if len(list1) != len(list2):
    print("lists are different length")
else:
    outstr="{"
    for i in range(len(list1)):
        outstr += f"' {list1[i]}"