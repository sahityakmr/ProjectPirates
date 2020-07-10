cobol = []
pole_vault = []
doughnut_eating = []
pole_vault_and_doughnut_eating = []
dry_run = False
if dry_run:
    # n = 4
    # cobol = [1, 1, 1, 1]
    # pole_vault = [10, 10, 10, 10]
    # doughnut_eating = [0, 0, 0, 0]

    n = 3
    cobol = [18, 23, 20]
    pole_vault = [7, 10, 9]
    doughnut_eating = [6, 27, 14]
else:
    n = int(input())
    for i in range(n):
        c, pv, de = map(int, input().split())
        cobol.append(c)
        pole_vault.append(pv)
        doughnut_eating.append(de)

for i in range(n):
    pole_vault_and_doughnut_eating.append(pole_vault[i] + doughnut_eating[i])

total_cobol = sum(cobol)
max_de_index = 0
max_de = pole_vault_and_doughnut_eating[0]
min_de_index = 0
min_de = pole_vault_and_doughnut_eating[0]
for i in range(1, n):
    if pole_vault_and_doughnut_eating[i] > max_de \
            or (pole_vault_and_doughnut_eating[i] == max_de
                and cobol[i] < cobol[max_de_index]):
        max_de = pole_vault_and_doughnut_eating[i]
        max_de_index = i
    if pole_vault_and_doughnut_eating[i] <= min_de:
        min_de = pole_vault_and_doughnut_eating[i]
        min_de_index = i
time = total_cobol
remaining_cobol = total_cobol - cobol[max_de_index]
if max_de > remaining_cobol and max_de - remaining_cobol > min_de:
    time += max_de - remaining_cobol
else:
    time += min_de
if dry_run:
    print('total_cobol  :', total_cobol)
    print('max_de       :', max_de)
    print('min_de       :', min_de)
    print('max_de_index :', max_de_index)
    print('min_de_index :', min_de_index)
print(time)
