def print_histogram_string_symbols(text):
    symbols_count = {}
    max_symbol_count = 0

    for symbol in text:
        if symbol not in symbols_count:
            symbols_count[symbol] = 0
        symbols_count[symbol] += 1

        max_symbol_count = max(max_symbol_count, symbols_count[symbol])

    sorted_symbols = sorted(symbols_count.keys())

    for n_row in range(max_symbol_count, 0, -1):
        for symbol in sorted_symbols:
            if symbols_count[symbol] >= n_row:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print("".join(sorted_symbols))


s = "Hello, world!"
print_histogram_string_symbols(s)
