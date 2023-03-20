#  Python Coding - Files Example

total = 0.0
count = 0
in_file = open("scores.txt", 'r')
for line in in_file:
    score = float(line)
    total += score
    count += 1
    print(f"Score = {score:4.1f}  Total so far = {total:6.1f}")
in_file.close()
average = total / count
print(f"Average = {average:.1f}")