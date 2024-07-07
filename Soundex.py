def generate_soundex(name):
    if not name:
        return ""
    
    codes = "01230120022455012623010202"
    soundex = name[0].upper()
    
    for char in name[1:].upper():
        if char.isalpha():
            code = codes[ord(char) - ord('A')]
            if code != '0' and code != soundex[-1]:
                soundex += code
                if len(soundex) == 4:
                    break
    
    return soundex.ljust(4, '0')
