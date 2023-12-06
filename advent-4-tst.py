matches = [4,2,2,1,0,1]
base_cy = [1,1,1,1,1,1]
cycle_0 = [0,1,1,1,1,0]
cycle_1 = [0,0,1,1,0,0]
cycle_2 = [0,0,0,1,1,0]
cycle_3 = [0,0,0,0,1,0]
cycle_4 = [0,0,0,0,0,0]
cycle_5 = [0,0,0,0,0,0]

final_c = [1,2,4,8,14,1]

cycle_reproduce = []
for i in range(len(matches)):
    zeros = [0] * len(matches)
    if (i+1+matches[i]) > len(matches):
        end_range = len(matches)
    else:
        end_range = i+1+matches[i]
    for j in range(i+1, end_range):
        zeros[j] += 1
    cycle_reproduce.append(zeros)
    
# print(cycle_reproduce[1][:])

total = base_cy
print(len(cycle_reproduce))

game = 0
while game < len(cycle_reproduce):
    # print("Matches this game : ", cycle_reproduce[game])
    # print("Current total : ", total)
    total_before = total.copy()
    for index in range(1, len(total)):
        print("Index : ", index)
        # print("Current value : ", total_before[index])
        # print("Added value : ", total_before[index-1] * cycle_reproduce[game][index])
        total[index] = total_before[index-1] * cycle_reproduce[game][index] + total_before[index]
        # print("New value : ", total[index])
    
    game += 1

print(total)
    


