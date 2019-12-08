WIDTH = 25
HEIGHT = 6


def read(file):
    with open(file, "r") as f:
        return f.readline()


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i: i + n]


def get_colour(pixels):
    return "".join(pixels).lstrip("2")[:1] or "2"


def part_one():
    layers = [c for c in chunks(read("input.txt"), WIDTH * HEIGHT)]
    min_layer = None
    min_zeros = WIDTH * HEIGHT
    for layer in layers:
        zeroes = layer.count("0")
        if zeroes < min_zeros:
            min_layer = layer
            min_zeros = zeroes

    return min_layer.count("1") * min_layer.count("2")


def part_two():
    layers = [c for c in chunks(read("input.txt"), WIDTH * HEIGHT)]
    colours = [get_colour(pixels) for pixels in zip(*layers)]
    return [
        "".join("#" if p == "1" else " " for p in row)
        for row in chunks(colours, WIDTH)
    ]
