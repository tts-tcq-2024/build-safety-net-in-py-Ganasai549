def generate_soundex(name):
    if not name:
        return ""
    
    soundex = name[0].upper()
    mapping = {
        'BFPV': '1', 'CGJKQSXZ': '2', 'DT': '3',
        'L': '4', 'MN': '5', 'R': '6'
    }
    
    for char in name[1:].upper():
        for key in mapping:
            if char in key:
                code = mapping[key]
                if code != soundex[-1]:
                    soundex += code
                break
        if len(soundex) == 4:
            break
    
    return soundex.ljust(4, '0')
