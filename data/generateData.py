#!/usr/bin/env python
# -*- coding: utf-8
from captcha.image import ImageCaptcha
from random import sample
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

image = ImageCaptcha()  # fonts=[ "font/Xenotron.ttf"]
characters = list("abcdefghijklmnopqrstuvwxyz")


def generate_data(digits_num, output, total):
    num = 0
    while (num < total):
        cur_cap = sample(characters, digits_num)
        cur_cap = ''.join(cur_cap)
        captcha = image.generate(cur_cap)
        image.write(cur_cap, output + cur_cap + ".png", format='png')
        captcha_image = Image.open(captcha)
        captcha_image = np.array(captcha_image)
        plt.imshow(captcha_image)
        num += 1


generate_data(4, "images/four_digit/", 5000)
generate_data(5, "images/five_digit/", 500)
generate_data(6, "images/six_digit/", 500)
generate_data(7, "images/seven_digit/", 500)
