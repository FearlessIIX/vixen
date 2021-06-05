from lexer import Lexer


class Tokenizer:

    # add: 3, 7
    # 'id-add', 'op-:', 'num-3', 'op-,' 'num-7', '\n'

    contents = []
    items = []

    def __init__(self, src):
        # split by lines
        self.contents = src.split("\n")

        every_line = [self.split(x) for x in self.contents]

        # print(every_line)
        Lexer(every_line)

    def split(self, line):
        temp = ""
        ret = []
        for ch in line:
            if ch == " ":
                continue

            if ch.isalnum():
                temp += ch
            else:
                ret.append(Token(temp))
                ret.append(Token(ch))

                temp = ""

        ret.append(Token(temp))
        return ret


class Token:

    def __init__(self, token):
        self.contents = token
        self.type = None

    def __repr__(self):
        return f'\'{self.contents}\''
