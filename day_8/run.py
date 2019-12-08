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

    rows = ["" for _ in range(150)]
    while image:
        for i, c in enumerate(image[:150]):
            rows[i] += c

        image = image[150:]

    colours = [row.lstrip("2")[:1] or "2" for row in rows]

    image = colours
    final_image = []

    while image:
        row = ["*" if c == "1" else " " for c in image[:25]]
        final_image.append("".join(row))
        image = image[25:]

    return final_image
