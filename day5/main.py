class SupplyStack:
    def __init__(self, string_input):
        data = string_input.split('\n\n')
        self.stack = self.parse_stack(data[0])
        self.instructions = data[1]

    def set_stack(self, stack):
        self.stack = stack

    def get_stack(self):
        return self.stack

    def parse_stack(self, stack_string):
        rows = stack_string.split('\n')
        num_keys = rows.pop(-1)
        base_length = int(num_keys[-1])
        return_arr = []
        for i in range(base_length):
            return_arr.append([])
        rows.reverse()
        for row in rows:
            j = 0
            for col in return_arr:
                ndx = 1 + (j * 4)
                if ndx < len(row):
                    chr = row[ndx]
                    if chr != ' ':
                        col.append(chr)
                j += 1
        return return_arr

    def move_boxes(self, instruction):
        #assumes uniformity with instructions
        instruction_array = instruction.split()
        for i in range(3):
            j = 2 * i + 1
            instruction_array[j] = int(instruction_array[j])
        for i in range(instruction_array[1]):
            box = self.stack[instruction_array[3] - 1].pop()
            self.stack[instruction_array[5] - 1].append(box)

    def get_top_crates(self):
        top = []
        for col in self.stack:
            if len(col) > 0:
                top.append(col[-1])
            else:
                top.append('')
        return top