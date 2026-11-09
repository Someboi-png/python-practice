total = 0
count = 0

with open("fuel.txt") as file:
    for line in file:
        line = line.strip()

        if line == "":
          continue

        fuel = int(line)
        total += fuel
        count += 1

average = total / count

print(f"Значений: {count}")
print(f"Сумма: {total}")
print(f"Среднее: {average}")