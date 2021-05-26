
#use the same function , by changing the directory for test set creating
def create_spectrogram_images(filename,name):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from glob import glob
    from memory_profiler import memory_usage
    from matplotlib import figure
    import gc
    from pathlib import Path
    import librosa
    import librosa.display
    import pylab
    count_ = 0
    plt.interactive(False)
    clip,sample_rate = librosa.load(filename,sr=None)
    fig = plt.figure(figsize=[0.74,0.74])
    
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    
    s = librosa.feature.melspectrogram(y=clip,sr=sample_rate)
    librosa.display.specshow(librosa.power_to_db(s,ref=np.max))
    
    filename =  name + '.jpg'
    count_+=1
    plt.savefig(filename,dpi=400,bbox_inches='tight',pad_inches=0)
    plt.close()
    fig.clf()
    plt.close(fig)
    plt.close('all')
    del filename,name,clip,sample_rate,fig,ax,s
    
def outside_fn():
    
    file = "output.wav"
    filename,name = file,file.split('/')[-1].split('.')[0]
    name = str("output")
    create_spectrogram_images(filename,name)
    print("Succcessfully Created the Spectrogram Copy")
    #deleting the wav file
    import os
    os.remove("output.wav")
    
