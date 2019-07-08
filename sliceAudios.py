import os, re


# Get the start and end time for each SRT file

for files in os.listdir('.'):
    if files.endswith('.srt'):
        f = open(files, mode="r")
        start_time = re.findall(r'(\d\d:\d\d:\d\d,\d\d\d)\s-->', f.read())
        f.close()
        f = open(files, mode="r")
        end_time = re.findall(r"-->\s(\d\d:\d\d:\d\d,\d\d\d)", f.read())

        #change the timestamp format
        startTimeALL = []
        endTimeALL = []

        for i in start_time:
            startTime = re.sub(r",", r'.', i)
            startTimeALL.append(startTime)
        for j in end_time:
            endTime = re.sub(r',', r'.', j)
            endTimeALL.append(endTime)

        timeALL = dict(zip(startTimeALL, endTimeALL))
        mp3 = os.path.splitext(files)[0] + ".wav"

        r = 1
        for key, value in timeALL.items():
            os.system("ffmpeg -i {} -ss  {} -to {} -c copy {}.wav".format(mp3, key, value, r))
            r += 1

        base = os.path.splitext(files)[0]
        # os.makedirs(base)
        os.makedirs(base+"_AUDIO")


        for audios in os.listdir('.'):
            if re.match(r"\d\d{0,}\.wav", audios):
                print(audios)
                os.rename(audios, str(base+"_AUDIO/")+audios)


