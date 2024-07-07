def generate_soundex(name):
    if not name:
        return ""
    
    soundex = name[0].upper()
    mapping = {'BFPV': '1', 'CGJKQSXZ': '2', 'DT': '3', 'L': '4', 'MN': '5', 'R': '6'}
    prev_code = '0'
    
    for char in name[1:].upper():
        code = next((v for k, v in mapping.items() if char in k), '0')
        if code != '0' and code != prev_code:
            soundex += code
            prev_code = code
        if len(soundex) == 4:
            break
    
    return soundex.ljust(4, '0')
