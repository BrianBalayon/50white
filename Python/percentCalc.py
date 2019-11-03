"""
50white.py
By: Brian Anthony M. Balayon

This was created for use by the Undergraduate Student Association of the University at Buffalo, SUNY. At the time
this was created, recognized clubs and organizations must have their flyers consist of at least 50% whitespace if
they would like to use their printing credits.
"""

import argparse
import copy
import os
import sys
import cv2
import numpy as np
import gui


def parse_args():
    parser = argparse.ArgumentParser(description="50% whitespace detector")
    parser.add_argument(
        "--img-path",
        type=str,
        dest="img_path",
        default=".TestImgs/50h.png",
        help="path to the image"
    )
    args = parser.parse_args()
    return args

def calc(img_path):
    read_img = read_image(img_path)
    percent = findWhite(read_img)
    return percent


def read_image(img_path, show=False):
    """Reads an image into memory as a grayscale array."""
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if not img.dtype == np.uint8:
        pass
    if show:
        show_image(img)
    img = [list(row) for row in img]
    return img


def show_image(img, delay=1000):
    """Shows an image."""
    cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image', img)
    cv2.waitKey(delay)
    cv2.destroyAllWindows()


def write_image(img, img_saving_path):
    """Writes an image to a given path."""
    if isinstance(img, list):
        img = np.asarray(img, dtype=np.uint8)
    elif isinstance(img, np.ndarray):
        if not img.dtype == np.uint8:
            assert np.max(img) <= 1, "Maximum pixel value {:.3f} is greater than 1".format(np.max(img))
            img = (255 * img).astype(np.uint8)
    else:
        raise TypeError("img is neither a list nor a ndarray.")

    cv2.imwrite(img_saving_path, img)


def findWhite(img):
    width = len(img)
    height = len(img[0])
    dim = width*height
    white_count = 0
    for i in range(len(img)):
        white_count += (img[i]).count(255)
        gui.update_text("Progress:" + str((i/width) * 100) + "\n")
    gui.update_text(str((white_count/dim) * 100) + "% white \n")


def main():
    args = parse_args()
    if not os.path.exists(args.img_path):
        print("Invalid image path:", args.img_path)
        sys.exit()
    img = read_image(args.img_path)
    calculated = findWhite(img)
    print(calculated)


if __name__ == "__main__":
    main()
