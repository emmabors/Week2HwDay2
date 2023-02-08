# Exercise 1
l_1 = [1,11,14,5,8,9]

def less_than_10(l_1):
    for num in l_1:
        if num < 10:
            print(num)

less_than_10(l_1)

# Exercise 2
l_11 = [1,2,3,4,5,6]
l_22 = [3,4,5,6,7,8,10]
# this works in vscode:
for num in l_22:
    l_11.append(num)
    l_11.sort()
print(l_11)
# this works in jupyter notebook, but not getting an output for this one in vscode
def merged_list():
    merged_list = l_22 + l_11
    merged_list.sort()
    return f'Merged list: {merged_list}'
merged_list()



