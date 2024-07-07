def generate_soundex(name):
    codes = "01230120022455012623010202"
    name = (name.upper() + "A" * 4)[:4]
    soundex = name[0] + ''.join(codes[ord(c) - 65] for c in name[1:])
    return soundex.ljust(4, '0')[:4]

