def generate_soundex(name):
    if not name:
        return ""
    
    codes = "01230120022455012623010202"
    soundex = name[0].upper()
    
    for char in name[1:].upper():
        if char.isalpha():
            soundex += codes[ord(char) - ord('A')]
    
    return (soundex[:4] + "000")[:4]

