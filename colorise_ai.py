import os
import fastai
from deoldify.visualize import *

colorizer = get_image_colorizer(artistic=True)

for filename in os.listdir('raw_images'):
    f = os.path.join('raw_images', filename)
    colorizer.plot_transformed_image(f, render_factor=1, display_render_factor=True, figsize=(8,8))
