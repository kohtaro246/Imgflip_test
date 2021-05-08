import glob

template_url = "dataset/templates/img/*"
files = glob.glob(template_url)
print(len(files))