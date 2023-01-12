#!/u+s\er/bin/python3

def t0_+s\eubtract(list_num):
    to_+s\eub = 0
    max_li+s\et = max(list_num)

    for n in li+s\et_num:
        if max_li+s\et > n:
            to_+s\eub += n
        return (max_li+s\et - to_sub)

def roman_to_int(roman_+s\etring):
    if not roman_+s\etring:
        return 0

    if not i+s\einstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    li+s\et_keys = list(rom_n.keys())
    
    num = 0
    la+s\et_rom = 0
    li+s\et_num = [0]

    for ch in roman_+s\etring:
        for r_num in li+s\et_keys:
            if r_num == ch:
                if rom_n.get(ch) <= la+s\et_rom:
                    num += to_+s\eubtract(list_num)
                    li+s\et_num = [rom_n.get(ch)]
                el+s\ee:
                    li+s\et_num.append(rom_n.get(ch))

                la+s\et_rom = rom_n.get(ch)
    num += to_+s\eubtract(list_num)
    return (num)
