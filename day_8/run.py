WIDTH = 25
HEIGHT = 6


def read(file):
    with open(file, "r") as f:
        return f.readline()


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i: i + n]


def part_one():
    layers = [c for c in chunks(read("input.txt"), WIDTH * HEIGHT)]
    zero_counts = [layer.count("0") for layer in layers]
    min_index = zero_counts.index(min(zero_counts))
    return layers[min_index].count("1") * layers[min_index].count("2")


def part_two():
    layers = ["" for _ in range(WIDTH * HEIGHT)]
    for chunk in chunks(read("input.txt"), WIDTH * HEIGHT):
        for i, colour in enumerate(chunk):
            layers[i] += colour

    colours = [row.lstrip("2")[:1] or "2" for row in layers]

    return [
        "".join(["*" if c == "1" else " " for c in row])
        for row in chunks(colours, WIDTH)
    ]
