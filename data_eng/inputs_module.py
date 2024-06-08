

def ask_for_int(message='please enter number'):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print("==== please enter valid number =====")


