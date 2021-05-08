import glob

template_url = "dataset/templates/img/*"
img_files = glob.glob(template_url)
memes_path = "dataset/memes/*"
meme_files = glob.glob(memes_path)
img_names = []
meme_names = []
for i in range (0, len(meme_files)):
    img_names.append(img_files[i].replace(".jpg","").replace("dataset/templates/img/", ""))
    meme_names.append(meme_files[i].replace(".json","").replace("dataset/memes/", ""))

for i in range (0, len(meme_files)):
    if img_names[i] not in meme_names:
        print(img_names[i])
