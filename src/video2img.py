import os
import cv2
import datetime

videos_src_path = r'../videos'
videos_save_path = r'../video_to_imgs'

videos = os.listdir(videos_src_path)
i = 0
for each_video in videos:
    print('Video Name :', each_video)
    each_video_name, _ = each_video.split('.')
    os.mkdir(videos_save_path + '/' + each_video_name)
    os.mkdir(videos_save_path + '/' + each_video_name + '/rgb')
    output_txt_path = '../video_to_imgs/' + each_video_name + '/rgb.txt'
    output_txt = open(output_txt_path, 'w')

    each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '/'

    each_video_full_path = os.path.join(videos_src_path, each_video)

    cap = cv2.VideoCapture(each_video_full_path)
    frame_count = 1
    success = True
    while (success):
        success, frame = cap.read()
        cv2.waitKey(10)
        i = i + 1
        if success == True:
            uuid_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            uuid_str = str(uuid_str)
            uuid_str = uuid_str.replace(":", "-")
            uuid_str = uuid_str.replace(" ", "")
            uuid_str = uuid_str.replace("-", "")
            uuid_str = uuid_str.replace("_", "")
            if i % 1 == 0:
                cv2.imwrite(each_video_save_full_path + uuid_str + '.png', frame)
                output_txt.write(uuid_str +' '+ 'rgb/'+ uuid_str + '.png' + '\n')

        frame_count = frame_count + 1
    print('Final frame:', frame_count)