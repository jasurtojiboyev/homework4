def foizlar_va_onlik(foizlar):
    onliklar = []
    for foiz in foizlar:
        son = float(foiz.replace('%', '')) / 100
        onliklar.append(son)
    return onliklar

# Misol uchun:
foizlar_royxati = ["45%", "32%", "97%", "33%"]
print(foizlar_va_onlik(foizlar_royxati))
