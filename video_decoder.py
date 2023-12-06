import subprocess
import os
def convert_and_stream_resolutions(input_video, output_prefix,output_path ):
    resolutions=[(640, 360), (854, 480), (1280, 720)]
    for resolution in resolutions:
        output_file_path = os.path.join(output_path, f'{output_prefix}_{resolution[0]}x{resolution[1]}.mp4')
        cmd = [
            'ffmpeg',
            '-i', input_video,
            '-vf', f'scale={resolution[0]}:{resolution[1]}',
            '-c:a', 'aac',
            '-strict', 'experimental',
            '-bufsize', '2048k',  # Adjust the buffer size as needed
            '-c:v', 'libx264',
            '-b:v', '1024k',  # Adjust the bitrate as needed
            '-r', '30',  # Adjust the output frame rate as needed
            output_file_path
        ]

        subprocess.run(cmd)

