

class Lexer:
    def __init__(self, code):
        syn = [
            'add', 'sub', 'print', ';', ":", ','
        ]

        meaning = {
            'add': {
                'type': 'syn',
                'action': '+'
            },
            'sub': {
                'type': 'syn',
                'action': '-'
            },
            'print': {
                'type': 'syn',
                'action': 'print'
            },
            ':': {
                'type': 'op',
                'action': 'perform'
            },
            ',': {
                'type': 'op',
                'action': 'perform'
            },
            ';': {
                'type': 'syn',
                'action': 'end'
            }
        }
        item = 'add'
        if item in syn:
            print("E")
        print(meaning[item]['type'])
        lexxed = []
        for ind in range(0, len(code)):
            for item in code[ind]:
                temp_str = ""
                temp_str += str(item)
                temp_str += ": "

                if item in syn:
                    temp_str += meaning[item]['type']
                    print(meaning[item]['type'])
                #print(temp_str)

            #temp_ret.append(temp)
            #lexxed.append(temp_ret)

        print(lexxed)

        # You want to lexer line by line
        # code = the whole code in an array
        # meaning['add']['type']

        """
            1. Create a new class for syntaxes (but just make a list for now)
            2. Go through each line then for each line, go through each token
            3. Identify if the token is a syntax then add the type
            4. If it's not a syntax then check what is that type (is it number or a string)
            
            [
                Token Object = {
                    'content': 'add',
                    'type': 'syntax
                },
                {
                    'content': ':',
                    'type': 'syntax'
                },
                {
                    'content: '1',
                    'type': 'number'
                },
                {
                    'content': ',',
                    'type': 'operator'
                }
            ]
                
        """



