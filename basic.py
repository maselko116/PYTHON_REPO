try:
    a = int(input("wprowadz sobie jakies a: "))
    print(f"twoja zmienna to: {a}")
except ValueError:
    print("podaj zmienna typu intiger")