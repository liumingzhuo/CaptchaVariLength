#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

image_shape = (3, 60, 250)
max_caption_len =8
images_dir = "../data/images/pic"
labels_dir = "../data/images/labels"
ch_index_dir = "../data/images/ch_index"
model_output = "../checkpoints/"
ch_index = json.loads(open(ch_index_dir, encoding='utf-8').read())
vocab_size = len(ch_index)
