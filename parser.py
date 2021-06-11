from syntax import meaning


def parse(line, line_number):

    err = False  # if the compiler raised an exception
    all_names = []  # contains the "content" of all tokens
    all_actions = []  # contains the "type" of all tokens
    name = ""
    action = ""

    # fills the above arrays with the specific values for each token
    for thing in line:
        name = thing.content
        action = thing.type

        all_names.append(name)
        all_actions.append(action)

    # TODO delete the example below
    # if type(1 is int): is true

    del(name, action)
    """
    from the start to the end, searches for an instruction
    3; ,; 7; 3; :; add
    """
    # TODO try to add functionality for multiple "instructions" per line IMPOSSIBLE FOR NOW
    # TODO try to add functionality for lines that don't start with "instructions"

    instruct = False  # if the compiler has found an instruction
    separate = False  # if the compiler has found the ":" separator

    count = -1  # token count;; count 0: token 1

    # TODO fix the exceptions in this "for" loop

    '''this block is meant just to find out what the "instruct" is'''
    for snip in all_actions:
        count += 1

        # runs once the compiler has encountered both an instruct and the correct separator op
        '''returns pretty much tell the compiler whether or not to continue parsing the code'''
        if instruct:
            if separate:
                if instruct_name == "add":
                    err = add(line_number, count, all_names, all_actions)
                    return err

        # records the instruct name
        if snip == "instruct":
            if instruct:
                # for now vix ignores multiple instructions
                # focusing on only the first instruction
                continue
            else:
                instruct_name = all_names[count]
                instruct = True
                continue
        elif not instruct:
            # vix will throw an exception here
            '''reached when the first thing encountered is not an instruct'''
            print(f"vix-- err;; in line {line_number + 1}. expected an instruction")
            return True

        # determines if the op is the correct separator
        if snip == "op":
            if instruct:
                if separate:
                    pass
                elif all_names[count] == ":":
                    separate = True
                    continue
                    pass
                else:
                    # vix will throw an exception here
                    '''reached when a ":" is missing after the instruct'''
                    print(f"vix-- err;; in line {line_number + 1}. expected a ':' ")
                    return True
            else:
                # vix will throw an exception here
                '''reached when there is an op encountered before an instruct'''
                print(f"vix-- err;; in line {line_number + 1}. expected an instruction before ':'")
                return True

        else:
            if not separate:
                # vix will throw an exception here
                '''reached when something other then an op is encountered before separation'''
                print(f"vix-- err;; in line {line_number + 1}. unknown content after instruction")
                return True


# TODO fix semi working add method; cannot handle multiple numbers; method exceptions are broken
def add(line_number, pass_count, names, actions):

    found_num = False
    found_op = False
    required = False
    passed_start = False

    total = 0
    num_count = 0

    count = -1
    for snip in actions:
        count += 1

        # skips the lines already read
        if count < pass_count:
            continue
        else:
            if snip == "num" and not passed_start:
                required = True
                passed_start = True
                total += int(names[count])
                num_count += 1
                continue

            else:
                if not passed_start:
                    # vix will throw an exception here
                    '''reached when the first token's type is not "num"'''
                    print(f"vix-- err;; in line {line_number + 1}. expected a num")
                    return True

        if found_op:
            if snip == "num":
                found_op = False
                found_num = True
                total += int(names[count])
                num_count += 1
            else:
                # vix will throw an exception here
                '''reached when a number was expected, but the snip wasn't num'''
                print(f"vix-- err;; in line {line_number + 1}. expected a num after ','")
                return True
            pass

        if required:
            if snip == "op":
                if names[count] == ",":
                    found_op = True
                    found_num = False
                    required = False
                    continue
                else:
                    # vix will throw an exception here
                    '''reached when a "," was expected, but a different op was found'''
                    print(f"vix-- err;; in line {line_number + 1}. expected a ',' but found '{names[count]}'")
                    return True
            else:
                # vix will throw an exception here
                # TODO make this exception more specific;; deviate into multiple exceptions
                '''reached when the code required a "," but there wasn't one'''
                print(f"vix-- err;; in line {line_number + 1}. expected a ','")
                return True

    if found_op:
        # vix will throw an exception here
        '''reached when the parse is finished but the last token was an op'''
        print(f"vix-- err;; in line {line_number + 1}. expected another num")
        return True
    else:
        if num_count < 2:
            # vix will throw an exception here
            '''reached when the parse is finished but only one number was found'''
            print(f"vix-- err;; in line {line_number + 1}. expected 2 nums found {num_count}")
            return True
        else:
            print(total)
            return False
