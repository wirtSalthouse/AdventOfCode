# This is a sample Python script.

class Elf:
    def __init__(self, place=1):
        self.place = place
        self.calories = 0

    def add_calories(self, calories):
        self.calories += int(calories)

    def to_tuple(self):
        return (self.place, self.calories)

    def has_more_calories(self, elf):
        return self.calories > elf.calories

def count_calories(elf_line):
    if not elf_line:
        return False
    most_calories_elf = Elf()
    cur_elf = Elf()
    arr = elf_line.split('\n')
    counter = 1
    for x in arr:
        if x:
            try:
                cur_elf.add_calories(x)
            except:
                return False
        else:
            if cur_elf.has_more_calories(most_calories_elf):
                most_calories_elf = cur_elf
            counter += 1
            cur_elf = Elf(counter)

    if cur_elf.has_more_calories(most_calories_elf):
        return cur_elf.to_tuple()
    return most_calories_elf.to_tuple()




