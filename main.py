SYMBOL_DICT = {
    '(': ')',
    '[': ']',
    '{': '}'
}

class Stack:

    def __init__(self):
        self.steck_list = []
        
    def isEmpty(self):
        return len(self.steck_list) == 0

    def push(self, _item):
        self.steck_list.append(_item)

    def pop(self):
        if not self.isEmpty():
            _item = self.steck_list.pop()
        return _item

    def peek(self):
        if not self.isEmpty():
            return self.steck_list[-1]

    def size(self):
        return len(self.steck_list)


def check_ballance(seq_):
    stack = Stack()
    for item_ in seq_:
        if item_ in SYMBOL_DICT:
            stack.push(item_)
        elif item_ == SYMBOL_DICT.get(stack.peek()):
            stack.pop()
        else:
            return 'Несбалансированно'
    return 'Сбалансированно'


if __name__ == '__main__':

    # сбалансированные
    string_1 = '(((([{}]))))'
    string_2 = '[([])((([[[]]])))]{()}'
    string_3 = '{{[()]}}'

    # несбалансированные
    string_4 = '}{}'
    string_5 = '{{[(])]}}'
    string_6 = '[[{())}]'

    print(f'{string_1:<50}{check_ballance(string_1)}')
    print(f'{string_2:<50}{check_ballance(string_2)}')
    print(f'{string_3:<50}{check_ballance(string_3)}')
    print(f'{string_4:<50}{check_ballance(string_4)}')
    print(f'{string_5:<50}{check_ballance(string_5)}')
    print(f'{string_6:<50}{check_ballance(string_6)}')
