messages = ['Enter an equation',
            'Do you even know what numbers are? Stay focused!',
            'Yes ... an interesting math operation. You\'ve slept through '
            'all classes, haven\'t you?',
            'Yeah... division by zero. Smart move...',
            'Do you want to store the result? (y / n):',
            'Do you want to continue calculations? (y / n):',
            ' ... lazy',
            ' ... very lazy',
            ' ... very, very lazy',
            'You are',
            'Are you sure? It is only one digit! (y / n)',
            'Don\'t be silly! It\'s just one number! Add to the memory? (y / '
            'n)',
            'Last chance! Do you really want to embarrass yourself? (y / n)']
v_oper = ["+", "-", "*", "/"]

memory = 0.0

again = False


def is_one_digit(v):
    return 10 > v > -10 and v.is_integer()


def save_to_memory(v):
    if not is_one_digit(v):
        return True

    else:
        msg_index = 10

        while True:
            print(messages[msg_index])
            answer = input()

            if answer == 'n':
                return False

            elif answer == 'y' and msg_index < 12:
                msg_index += 1
                continue

            else:
                return True


def check(v1, v2, v3):
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + messages[6]

    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + messages[7]

    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "-" or v3 == "+"):
        msg = msg + messages[8]

    if msg != "":
        msg = messages[9] + msg

    print(msg)


while True:
    print(messages[0])
    calc = input()
    x, oper, y = calc.split()

    if x == "M":
        x = memory

    if y == "M":
        y = memory

    try:
        x = float(x)
        y = float(y)

    except ValueError:
        print(messages[1])
        continue

    check(x, y, oper)

    if oper not in v_oper:
        print(messages[2])
        continue

    else:
        if oper == "+":
            result = x + y

        elif oper == "-":
            result = x - y

        elif oper == "*":
            result = x * y

        else:
            try:
                result = x / y

            except ZeroDivisionError:
                print(messages[3])
                continue

        print(result)

        while True:
            print(messages[4])
            answer_1 = input()

            if answer_1 == "y":
                if save_to_memory(result):
                    memory = result
                break

            elif answer_1 == "n":
                break

            else:
                continue

        while True:
            print(messages[5])
            answer_2 = input()

            if answer_2 == "y":
                again = True
                break

            if answer_2 == "n":
                again = False
                break

            else:
                continue

    if not again:
        break

    else:
        continue

# burnoz :o
