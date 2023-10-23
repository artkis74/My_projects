from pathlib import Path

import moviepy.editor

video_path = str(input('Введите имя файла: '))


def extracting_audio(video_path):
    video_file = Path(video_path)
    video = moviepy.editor.VideoFileClip(f'{video_file}')
    audio = video.audio
    audio.write_audiofile(f'{video_file.stem}.mp3')
    return 'Аудиофайл успешно создан'


extracting_audio(video_path)
