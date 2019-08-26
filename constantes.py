width = 800
height = 800
blocks = (30,30)
tscale = 0.1
block_size_x = width / blocks[0]
block_size_y = height / blocks[1]


def block_to_pixel(coord):
    return [coord[0] * block_size_x , coord[1] * block_size_y]
