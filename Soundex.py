def generate_soundex(name):
    if not name:
        return ""
    
    first_letter = name[0].upper()
    encoded = encode_remaining(name[1:].upper())
    return pad_with_zeros(first_letter + encoded)

def encode_remaining(remaining):
    codes = [get_code(char) for char in remaining]
    return ''.join(filter_codes(codes))

def get_code(char):
    mapping = {'BFPV': '1', 'CGJKQSXZ': '2', 'DT': '3', 'L': '4', 'MN': '5', 'R': '6'}
    return next((code for key, code in mapping.items() if char in key), '0')

def filter_codes(codes):
    result = []
    prev_code = '0'
    for code in codes:
        if code != '0' and code != prev_code:
            result.append(code)
            prev_code = code
        if len(result) == 3:
            break
    return result

def pad_with_zeros(soundex):
    return soundex.ljust(4, '0')
