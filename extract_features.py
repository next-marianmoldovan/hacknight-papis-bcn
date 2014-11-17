# -*- coding: utf-8 -*-
from scipy.misc import imsave, imread
from indicoio import image_features
import numpy, os, json

root = 'bcn'
data = []
index = 0

for f in os.listdir('bcn'):
	print f 
	import time
	index += 1
	start = time.time()
	img = imread(root + '/' + f)
	features = image_features(img)
	data.append({'file':f,'features':features})
	end = time.time()
	print str(index)
	print end - start 

json.dump(data, open('features.json' % index, 'wb'))

