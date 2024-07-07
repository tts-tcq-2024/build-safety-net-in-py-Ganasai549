def generate_soundex(name):
    if not name:
        return ""
    
    soundex = name[0].upper()
    mapping = {'BFPV': '1', 'CGJKQSXZ': '2', 'DT': '3', 'L': '4', 'MN': '5', 'R': '6'}
    
    for char in name[1:].upper():
        for key, value in mapping.items():
            if char in key and value != soundex[-1]:
                soundex += value
                if len(soundex) == 4:
                    return soundex
                break
    
    return soundex.ljust(4, '0')
