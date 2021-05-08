import glob

template_url = "dataset/templates/img/*"
img_files = glob.glob(template_url)
img_files_up = []
for i in range (0, len(img_files)):
    img_files_up.append(img_files[i].replace())
#print(len(img_files))

