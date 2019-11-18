
import imageio
import os
import moviepy.editor as mp
clip1 = mp.VideoFileClip("cn.mp4").subclip(0,2)
clips=clip1.write_videofile("cnshort.mp4")
clip=os.path.abspath('cnshort.mp4')
#print(clip)
def gifmaker(inputPath,targetFormat):
    outputPath=os.path.splitext(inputPath)[0] + targetFormat
    print(f'converting {inputPath} \n to {outputPath}')
    reader=imageio.get_reader(inputPath)
    fps=reader.get_meta_data()['fps']
    writer=imageio.get_writer(outputPath,fps=fps)

    for frames in reader:
        writer.append_data(frames)
        print(f'Frame{frames}')
    print('Done!')
    writer.close()

gifmaker(clip,'.gif')