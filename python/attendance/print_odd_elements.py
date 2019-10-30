numbers = [ 2,7,14,19,31,146]
odd_elements = []
count = 0
for Z in numbers:
    if count % 2 == 1:
        odd_elements.append(Z)
    count += 1
print(odd_elements)