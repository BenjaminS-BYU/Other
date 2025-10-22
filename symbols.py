def romanToInt(s: str):
    symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    symbol_total = 0

    for i in range(len(s)):
        current_value = symbols[s[i]]

        # if there's a next symbol and it's larger, subtract instead of add
        if i + 1 < len(s) and symbols[s[i + 1]] > current_value:
            symbol_total -= current_value
        else:
            symbol_total += current_value

    return symbol_total


print(romanToInt("III"))      # 3
print(romanToInt("LVIII"))    # 58
print(romanToInt("MCMXCIV"))  # 1994
