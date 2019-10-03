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
import cv2
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser(description="cse 473/573 project 1.")
    parser.add_argument(
        "--img-path",
        type=str,
        default="./data/proj1-task1.jpg",
        help="path to the image"
    )
    parser.add_argument(
        "--filter",
        type=str,
        default="high-pass",
        choices=["low-pass", "high-pass"],
        help="type of filter"
    )
    parser.add_argument(
        "--result-saving-dir",
        dest="rs_dir",
        type=str,
        default="./results/",
        help="directory to which results are saved (do not change this arg)"
    )
    args = parser.parse_args()
    return args


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
    for col in img:
        white_count += col.count(1)
    return white_count/dim


def main():
    args = parse_args()

    img = read_image(args.img_path)

    if not os.path.exists(args.rs_dir):
        os.makedirs(args.rs_dir)

    calculated = findWhite(img)

    print(calculated)


if __name__ == "__main__":
    main()
