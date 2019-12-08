def read(file):
    with open(file, "r") as f:
        return f.readline()


def part_one():
    image = read("input.txt")

    layers = []
    layer = []
    while image:
        layer.append(image[:25])
        image = image[25:]

        if len(layer) == 6:
            layers.append(layer)
            layer = []

    counts = ["".join(layer).count("0") for layer in layers]
    min_index = counts.index(min(counts))
    layer = "".join(layers[min_index])

    return layer.count("1") * layer.count("2")


def part_two():
    image = read("input.txt")

    rows = [[] for _ in range(150)]
    while image:
        for i, row in enumerate(image[:150]):
            rows[i].append(row)

        image = image[150:]

    colours = []
    for row in rows:
        colour = None
        for c in row:
            if c == '0':
                colour = 0
                break
            elif c == '1':
                colour = 1
                break
            else:
                colour = 2

        colours.append(colour)

    image = "".join([str(i) for i in colours])

    while image:
        print("".join([c if c == "1" else " " for c in image[:25]]))
        image = image[25:]
