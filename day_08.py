WIDTH = 25
HEIGHT = 6


def read(file):
    with open(file, "r") as f:
        return [c for c in chunks(f.readline(), WIDTH * HEIGHT)]


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i: i + n]


def get_colour(pixels):
    return "".join(pixels).lstrip("2")[:1] or "2"


def part_one():
    layers = read("inputs/day_08.txt")
    zero_counts = {layer: layer.count("0") for layer in layers}
    min_layer = min(zero_counts, key=zero_counts.get)
    return min_layer.count("1") * min_layer.count("2")


def part_two():
    layers = read("inputs/day_08.txt")
    colours = [get_colour(pixels) for pixels in zip(*layers)]
    return [
        "".join("#" if p == "1" else " " for p in row)
        for row in chunks(colours, WIDTH)
    ]
