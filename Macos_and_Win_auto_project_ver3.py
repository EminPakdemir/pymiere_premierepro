#!/usr/bin/env python3
# coding: utf-8

import os
import platform
import time
import subprocess

print("""
    +++++++++++++++++++++++++++++++++++++++++++++++++++
    +                                                 +
    +                                                 +
    +            AUTOMATIC PROJECT BUILDER            +
    +          Adobe Premiere Pro 2020-2022           +
    +                                                 +
    +                    ver 3.0                      +
    +                                                 +
    +           Developed by Emin Pakdemir            +
    +             eminpakdemir@gmail.com              +
    +                                                 +
    +++++++++++++++++++++++++++++++++++++++++++++++++++
""")

# TODO: CHECK OPEN ADOBE PREMIERE PRO 2020-2022

plt = platform.system()

if plt == "Windows":

    tasklistesi = subprocess.Popen('TASKLIST', stdout=subprocess.PIPE).stdout.readlines()
    type(tasklistesi)
    c = str(list(tasklistesi)).find("b'Adobe Premiere Pro.exe")

    if c == -1:
        print("""\n\n<=== ADOBE PREMIERE PRO IS NOT RUNNING! ===>\n""")
        subprocess.Popen("C:\Program Files\Adobe\Adobe Premiere Pro 2020\Adobe Premiere Pro.exe")
        i = 0
        while i < 25:
            x = (i - 25) * -1
            print("=>",x, "After seconds, the program and project builder will start automatically.")
            time.sleep(1)
            i += 1

        print("""\n\n<=== ADOBE PREMIERE PRO 2020-2022 HAS ALREADY STARTED PROGRAM ===>\n""")
    

    else:
        print("""\n\n<=== ADOBE PREMIERE PRO 2020-2022 HAS ALREADY STARTED PROGRAM ===>\n""")
   
        time.sleep(4)


elif plt == "Darwin":

    tasklistesi = subprocess.Popen(["ps", "-axc"], stdout=subprocess.PIPE).stdout.readlines()
    type(tasklistesi)
    c = str(list(tasklistesi)).find("Adobe Premiere Pro 2020") # ÖNEMLİ!!! MACOSX'TE VERSİYON NUMARASI VAR. Eğer güncellenirse buradaki değer değişritilmesi gerekir.

    if c == -1:
        print("""\n\n<=== ADOBE PREMIERE PRO IS NOT RUNNING! ===>\n""")
        subprocess.Popen(['open', '/Applications/Adobe Premiere Pro 2020/Adobe Premiere Pro 2020.app'])
        i = 0
        while i < 25:
            x = (i - 25) * -1
            print("=>",x, "After seconds, the program and project builder will start automatically.")
            time.sleep(1)
            i += 1

        print("""\n\n<=== ADOBE PREMIERE PRO 2020-2022 HAS ALREADY STARTED PROGRAM ===>\n""")
       

    else:
        print("""\n\n<=== ADOBE PREMIERE PRO 2020-2022 HAS ALREADY STARTED PROGRAM ===>\n""")
       
        time.sleep(4)



# In[3]:


import pymiere

# In[4]:


if plt == "Windows": #FOR WINDOWS SYSTEMS

    ROOT_FOLDER = os.getcwd()
    for_project_name = ROOT_FOLDER.split("\\")
    reverse_list = for_project_name[::-1]
    PROJECT_NAME = reverse_list[0]
    project_path = f"{ROOT_FOLDER}\\01_PR_PROJECT\\{PROJECT_NAME}.prproj"  ### Eğer 01_PR_PROJECT adında klasör yoksa aşağıdaki komut çalışmaz.

    print("=>",project_path)

elif plt == "Darwin": #FOR MACOSX SYSTEMS

    ROOT_FOLDER = os.getcwd()
    for_project_name = ROOT_FOLDER.split("/")
    reverse_list = for_project_name[::-1]
    PROJECT_NAME = reverse_list[0]
    project_path = f"{ROOT_FOLDER}/01_PR_PROJECT/{PROJECT_NAME}.prproj"  ### Eğer 01_PR_PROJECT adında klasör yoksa aşağıdaki komut çalışmaz.

    print("=>",project_path)

# In[5]:


pymiere.objects.qe.newProject(project_path)

# In[6]:


pymiere.objects.app.project.name

# In[7]:


pymiere.objects.app.project.rootItem.name

# In[8]:


pymiere.objects.app.project.rootItem.createBin("00_FINAL_SEQUENCES")
pymiere.objects.app.project.rootItem.createBin("03_VIDEOS")
pymiere.objects.app.project.rootItem.createBin("05_MUSICS")
pymiere.objects.app.project.rootItem.createBin("08_AUDIOS")

# In[9]:


if plt == "Windows":

    sequence_preset_path = f"{ROOT_FOLDER}\\SequencePresets\\DSLR 1080p50_V3_A3.sqpreset"

elif plt == "Darwin":

    sequence_preset_path = f"{ROOT_FOLDER}/SequencePresets/DSLR 1080p50_V3_A3.sqpreset"

# In[10]:


sequence_name = PROJECT_NAME

# In[11]:


pymiere.objects.qe.project.newSequence(sequence_name, sequence_preset_path)

# In[12]:


try:

    for i in range(5):
        name = pymiere.objects.app.project.rootItem.children[i].name
        print("=>",name, "Children", [i])




except ValueError:
    pass

# In[13]:


app = pymiere.objects.app

# In[14]:


sequence = [s for s in app.project.sequences if s.name == sequence_name][0]
print("=>",sequence)

# In[15]:


app.project.openSequence(sequenceID=sequence.sequenceID)

# In[16]:


print("=>",app.project.activeSequence.name, "created.")

# In[17]:


time.sleep(1)

# TODO: FOLDERS AND FILES PATHS
# In[18]:


if plt == "Windows":

    media_path_03_VIDEOS = f"{ROOT_FOLDER}\\03_VIDEOS"
    media_path_05_MUSICS = f"{ROOT_FOLDER}\\05_MUSICS"
    media_path_08_AUDIOS = f"{ROOT_FOLDER}\\08_AUDIOS"
    

elif plt == "Darwin":

    media_path_03_VIDEOS = f"{ROOT_FOLDER}/03_VIDEOS"
    media_path_05_MUSICS = f"{ROOT_FOLDER}/05_MUSICS"
    media_path_08_AUDIOS = f"{ROOT_FOLDER}/08_AUDIOS"
    

# TODO: IMPORT FOLDERS AND FILES, LIST AND len()


# In[19]:


if plt == "Windows":

    list_dir_03_ham_video = os.listdir(media_path_03_VIDEOS)

    print("=>",list_dir_03_ham_video)

    len(list_dir_03_ham_video)

    try:
        for i in range(len(list_dir_03_ham_video)):
            success_03_ham_video = app.project.importFiles(
                [media_path_03_VIDEOS + "\\" + list_dir_03_ham_video[i]],  # can import a list of media
                suppressUI=True,
                targetBin=app.project.rootItem.children[1],
                importAsNumberedStills=False
            )
        print("=>",success_03_ham_video, ": IMPORT VIDEO FILES")

    except:
        pass

elif plt == "Darwin":

    list_dir_03_ham_video = os.listdir(media_path_03_VIDEOS)

    print("=>",list_dir_03_ham_video)

    len(list_dir_03_ham_video)

    try:
        for i in range(len(list_dir_03_ham_video)):
            success_03_ham_video = app.project.importFiles(
                [media_path_03_VIDEOS + "/" + list_dir_03_ham_video[i]],  # can import a list of media
                suppressUI=True,
                targetBin=app.project.rootItem.children[1],
                importAsNumberedStills=False
            )
        print("=>",success_03_ham_video, ": IMPORT VIDEO FILES")

    except:
        pass

# In[20]:


if plt == "Windows":

    list_dir_05_music = os.listdir(media_path_05_MUSICS)

    print("=>",list_dir_05_music)

    len(list_dir_05_music)

    try:
        for i in range(len(list_dir_05_music)):
            success_05_music = app.project.importFiles(
                [media_path_05_MUSICS + "\\" + list_dir_05_music[i]],  # can import a list of media
                suppressUI=True,
                targetBin=app.project.rootItem.children[2],
                importAsNumberedStills=False
            )
        print("=>",success_05_music, ": IMPORT MUSIC FILES")

    except:
        pass

elif plt == "Darwin":

    list_dir_05_music = os.listdir(media_path_05_MUSICS)

    print("=>",list_dir_05_music)

    len(list_dir_05_music)

    try:
        for i in range(len(list_dir_05_music)):
            success_05_music = app.project.importFiles(
                [media_path_05_MUSICS + "/" + list_dir_05_music[i]],  # can import a list of media
                suppressUI=True,
                targetBin=app.project.rootItem.children[2],
                importAsNumberedStills=False
            )
        print("=>",success_05_music, ": IMPORT MUSIC FILES")

    except:
        pass

# In[21]:


if plt == "Windows":

    list_dir_08_audio = os.listdir(media_path_08_AUDIOS)

    print("=>",list_dir_08_audio)

    len(list_dir_08_audio)

    try:
        for i in range(len(list_dir_08_audio)):
            success_08_audio = app.project.importFiles(
                [media_path_08_AUDIOS + "\\" + list_dir_08_audio[i]],  # can import a list of media
                suppressUI=True,
                targetBin=app.project.rootItem.children[3],
                importAsNumberedStills=False
            )
        print("=>",success_08_audio, ": IMPORT AUDIO FILES")

    except:
        pass

elif plt == "Darwin":

    list_dir_08_audio = os.listdir(media_path_08_AUDIOS)

    print("=>",list_dir_08_audio)

    len(list_dir_08_audio)

    try:
        for i in range(len(list_dir_08_audio)):
            success_08_audio = app.project.importFiles(
                [media_path_08_AUDIOS + "/" + list_dir_08_audio[i]],  # can import a list of media
                suppressUI=True,
                targetBin=app.project.rootItem.children[3],
                importAsNumberedStills=False
            )
        print("=>",success_08_audio, ": IMPORT AUDIO FILES")

    except:
        pass





# In[22]:


# TODO: VIDEO FILES IN TO CREATED SEQUENCE
from pymiere.wrappers import time_from_seconds

items_03_VIDEOS = app.project.rootItem.findItemsMatchingMediaPath(media_path_03_VIDEOS, ignoreSubclips=False)

i = len(items_03_VIDEOS)
print("\n","=>", i, f"Video Clips will import in {sequence_name} Sequence")

for i in range(i - 1, -1, -1):
    # add clip to active sequence
    app.project.activeSequence.videoTracks[0].insertClip(items_03_VIDEOS[i], time_from_seconds(0))
    print("=>",i)

# In[23 ]:


# TODO: AUDIO RECORDED FILES IN TO CREATED SEQUENCE

items_08_AUDIOS = app.project.rootItem.findItemsMatchingMediaPath(media_path_08_AUDIOS, ignoreSubclips=False)

i = len(items_08_AUDIOS)
print("\n","=>",i, f"Audio Record Clips will import in {sequence_name} Sequence")

for i in range(i - 1, -1, -1):
    # add clip to active sequence
    app.project.activeSequence.videoTracks[1].insertClip(items_08_AUDIOS[i], time_from_seconds(0))
    print("=>",i)

# # Project Save

# In[24]:
print("""
    +++++++++++++++++++++++++++++++++++++++++++++++++++
    +                                                 +     
    +                                                 +
    +          Thank you for choosing me.             +  
    +      15 seconds after saving the project,       +   
    +      this window will close automatically!      +
    +                                                 +
    +                   Good work!                    +
    +          Don't forget to Clean Export           +
    +                                                 +
    +           Developed by Emin Pakdemir            +
    +             eminpakdemir@gmail.com              +
    +                                                 +
    +++++++++++++++++++++++++++++++++++++++++++++++++++
""")


pymiere.objects.app.project.save()

time.sleep(15)
