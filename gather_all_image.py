import os
#paths=['coco2014','Stanford','vehicleplate']
paths=['all_fire_21211']
f=open('train_all_21211.txt', 'w')
for path in paths:
    p=os.path.abspath(path)+'/JPEGImages'
    filenames=os.listdir(p)
    for filename in filenames:
        im_path=p+'/'+filename
        print(im_path)
        f.write(im_path+'\n')
f.close()
