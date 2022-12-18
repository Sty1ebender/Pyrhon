def encode_string(strings):
    list_bytes = []
    for i in strings:
        a = i.encode('utf-8')
        list_bytes.append(a)
    return list_bytes


def decode_string(byte):
    list_strings = []
    for i in byte:
        my_string = bytes.decode(i, 'utf-8')
        list_strings.append(my_string)
    return list_strings


byte_codes = encode_string(["Один", "Два", 'Три'])
print(byte_codes)
print(decode_string(byte_codes))
