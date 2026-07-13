def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here

    hist_list = [0 for i in range(256)]

    for idx, value in enumerate(image):
        for jdx, value_2 in enumerate(image[idx]):
            hist_list[value_2] += 1

    return hist_list