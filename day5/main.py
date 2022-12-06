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

    def move_boxes_unorderd(self):
        return self.move_all_boxes( False)

    def move_boxes_ordered(self):
        return self.move_all_boxes(True)

    def move_all_boxes(self, ordered=True):
        for instruction in self.instructions.split('\n'):
            self.move_boxes(instruction, ordered)

    def move_boxes(self, instruction, preserve_order=False):
        #assumes uniformity with instructions
        instruction_array = instruction.split()
        for i in range(3):
            j = 2 * i + 1
            instruction_array[j] = int(instruction_array[j])

        move_cluster = []
        for i in range(instruction_array[1]):
            box = self.stack[instruction_array[3] - 1].pop()
            if preserve_order:
                move_cluster.insert(0, box)
            else:
                move_cluster.append(box)

        self.stack[instruction_array[5] - 1] += move_cluster

    def get_top_crates(self):
        top = []
        for col in self.stack:
            if len(col) > 0:
                top.append(col[-1])
            else:
                top.append('')
        return top