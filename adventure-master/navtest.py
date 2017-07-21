""" Kompaktes Test-Dingens fuer das laufen auf einem 2D-Spielbrett """

Spielbrett = [5, 10]  # Masse des Spielbretts
Position = [1, 2]  # Position des Avatars H/B


def generate_map(size):
    z = 0
    zeile = [""] * size[0]  # initialisiere leeres array

    for H in range(size[0]):
        r = list()
        for W in range(size[1]):
            r.append("O")
        zeile[z] = r
        z = z + 1

    return zeile


def print_map(karte, position):
    i = 0
    for H in karte:
        if i == position[0]:
            H[position[1]] = "X"
        i = i + 1

        z = ""
        for W in H:
            z = z + W
        print(z)


def move_avatar(karte, position):
    pass


Karte = generate_map(Spielbrett)
print_map(Karte, Position)

print("Done.")
