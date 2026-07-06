def luminance_weights(r, g, b):
    return 0.299 * r + 0.587 * g + 0.114 * b

def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    image_list = []
    for i in range(len(image)):
        pixel_list = []
        for j in range(len(image[i])):
            gry_scl = luminance_weights(
                image[i][j][0],
                image[i][j][1],
                image[i][j][2]
            )
            pixel_list.append(gry_scl)
        image_list.append(pixel_list)

    return image_list