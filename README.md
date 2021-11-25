# Point Cloud Augmentation Tool

## Motivation
Recently, I have been doing research and working with **Point Cloud Registration** using **Deep Learning**. However, one main limitation of deep learning is the need for large data sets. My work is related to `medical data`, and it is always difficult to get more data due to various issues related to the healthcare sector.

To overcome this difficulty, I decided to make a simple **point cloud augmentation** tool that can help to increase the data set size. Then I might be able to have sufficient data to train deep learning models.

## Avalable functions
For now, I have decided to include some `basic` augmentations like:

* Rotation
* Translation
* Sampling
* Interpolation
* Jitter

If I come up with more ideas, I will try to include them in the `tool`.

## App Interface
The app is built using the **Tkinter module** in python. In the simplest form, we can create some `frame` and `canvas`, attach some `buttons` to it, and then assign some `commands` or `actions` to those buttons via `functions`.

This [tutorial](https://www.youtube.com/watch?v=jE-SpRI3K5g) from **Dev Ed** really helped me to get started with it.