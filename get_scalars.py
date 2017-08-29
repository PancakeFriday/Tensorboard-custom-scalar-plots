#!/usr/bin/python

import csv
import tensorflow as tf
from tensorflow.tensorboard.backend.event_processing import event_accumulator

tf.app.flags.DEFINE_string('logdir', None,
		'The logdir to get the scalars from')

ea = event_accumulator.EventAccumulator(tf.app.flags.FLAGS.logdir,
    size_guidance={ # see below regarding this argument
        event_accumulator.COMPRESSED_HISTOGRAMS: 500,
        event_accumulator.IMAGES: 4,
        event_accumulator.AUDIO: 4,
        event_accumulator.SCALARS: 0,
        event_accumulator.HISTOGRAMS: 1,
})

ea.Reload()

tags = ea.Tags()['scalars']

# fields are:
#   - wall_time
#   - step
#   - value

# create a file for each tag
for t in tags:
    tag_data = []
    for d in ea.Scalars(t):
        tag_data.append([d.step, d.value])

    with open("data_%s.csv"%t, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(tag_data)

    print(t)
