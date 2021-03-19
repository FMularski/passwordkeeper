def encode_password(password, pin):
    pin_sum = 0
    for char in pin:
        pin_sum += ord(char)

    encoded = ''

    for char in password:
        encoded += chr(ord(char) + pin_sum)

    return encoded


def decode_password(encoded, pin):
    pin_sum = 0
    for char in pin:
        pin_sum += ord(char)

    decoded = ''

    for char in encoded:
        decoded += chr(ord(char) - pin_sum)

    return decoded
