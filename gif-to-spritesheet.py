import sys
from PIL import Image

def get_frame_count(gif_path):
    try:
        with Image.open(gif_path) as img:
            frame_count = 1
            while True:
                try:
                    img.seek(frame_count)
                    frame_count += 1
                except EOFError:
                    break
            return frame_count - 1
    except Exception as e:
        print("Error:", e)
        return 0

def extract(gif, out):
    with Image.open(gif) as im:
        width, height = im.width, im.height
        frame_nums = get_frame_count(gif)
        new_height = height*frame_nums
        new_image = Image.new('RGBA',(width, new_height), (0, 0, 0, 0))
        for index, i in enumerate(range(frame_nums)):
            im.seek(im.n_frames // frame_nums * i)
            new_image.paste(im,(0,height*index))
        new_image.save('{}'.format(out))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: gif-to-spritesheet.py <gif> <png output>")
        exit()
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    extract(in_file, out_file)
