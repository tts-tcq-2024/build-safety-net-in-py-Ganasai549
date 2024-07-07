def generate_soundex(name):
    if not name:
        return ""
    
    first_letter = name[0].upper()
    encoded = encode_remaining(name[1:].upper())
    truncated = truncate_to_three(encoded)
    padded = pad_with_zeros(first_letter + truncated)
    
    return padded

def encode_remaining(remaining):
    mapping = {'BFPV': '1', 'CGJKQSXZ': '2', 'DT': '3', 'L': '4', 'MN': '5', 'R': '6'}
    encoded = ""
    prev_code = '0'
    
    for char in remaining:
        code = get_code(char, mapping)
        if code != '0' and code != prev_code:
            encoded += code
            prev_code = code
    
    return encoded

def get_code(char, mapping):
    for key, value in mapping.items():
        if char in key:
            return value
    return '0'

def truncate_to_three(encoded):
    return encoded[:3]

def pad_with_zeros(soundex):
    return soundex.ljust(4, '0')
