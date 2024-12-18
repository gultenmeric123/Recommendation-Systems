import os
from PIL import Image, ImageOps
import pandas as pd

def get_item_image(item_id, resize=True, width=100, height=150):
    path = 'results/images/'+item_id+'.jpeg'
    image = Image.open(path)

    if resize:
        basewidth = width
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((width, height), Image.Resampling.LANCZOS)
        image = ImageOps.expand(image, 2)

    return image

def get_rcmnds(customer_data):
    # Sadece feature_rcmnds kullanılıyor.
    feature_rcmnds = customer_data.feature_rcmnds.values
    return feature_rcmnds

def get_rcmnds_scores(customer_data):
    # Sadece feature_scores kullanılıyor.
    feature_scores = customer_data.feature_scores.values
    return feature_scores

def get_rcmnds_images(feature_rcmnds):
    # Sadece feature_rcmnds kullanılıyor.
    feature_rcmnds_images = [get_item_image(str(i)) for i in feature_rcmnds]
    return feature_rcmnds_images

def get_rcmnds_features(df, feature_rcmnds):
    # Sadece feature_rcmnds kullanılıyor.
    feature_rcmnds_features = df[df.article_id.isin(feature_rcmnds)][['product_type_name', 'colour_group_name', 'department_name']]
    return feature_rcmnds_features

