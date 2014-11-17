# -*- coding: utf-8 -*-
from scipy.misc import imsave, imread
from indicoio import image_features
import numpy, os, json

root = 'bcn'
data = []

for f in os.listdir('bcn'):
	import time
	start = time.time()
	img = imread(root + '/' + f)
	features = image_features(img)
	data.append({'file':f,'features':features})
	end = time.time()
	print end - start 

json.dump(data, open('features.json', 'wb'))