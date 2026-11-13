def normalise(text):
    text = text.replace(" ", "")
    text = text.replace("-", "")
    return text.upper()


def is_valid(reg):
    if len(reg) not in (9, 10):
        return False

    if not reg[:2].isalpha():
        return False

    if not reg[2:4].isdigit():
        return False

    if len(reg[4:-4]) not in (1, 2):
        return False

    if not reg[4:-4].isalpha():
        return False

    if not reg[-4:].isdigit():
        return False

    return True


def format_number(reg):
    if is_valid(reg):
        return reg[:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]
    return "INVALID"


numbers = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "AP 10 CD 5678",
    "KL-07-XY-9876"
]

for raw in numbers:
    reg = normalise(raw)
    print(raw, "->", reg, "->", format_number(reg))
