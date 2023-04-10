from PIL import Image, ImageDraw, ImageFont
from PIL.ExifTags import TAGS
from datetime import datetime, timedelta, date
import os
import msvcrt #只适用于Windows程序实现按任意键退出，Linux和macOS需要sys,tty,termios和其他的代码

# 获取图像的 EXIF 数据
def get_exif_data(image):
    exif_data = {}
    try:
        exif_info = image._getexif()
        if exif_info:
            for tag, value in exif_info.items():
                decoded = TAGS.get(tag, tag)
                exif_data[decoded] = value
    except AttributeError:
        pass
    return exif_data

# 获取图像的拍摄日期
def get_date_taken(image):
    exif_data = get_exif_data(image)
    date_string = exif_data.get('DateTimeOriginal', None)
    if date_string:
        date_taken = datetime.strptime(date_string, '%Y:%m:%d %H:%M:%S')
        return date_taken.date()
    return None
      
# 处理图像 
def process_image(image_path, output_dir, target_date, font=None):
    with Image.open(image_path) as image:
        date_taken = get_date_taken(image)
        if not date_taken:
            return
        img_width, img_height = image.size
        longside = max(img_height, img_width)
        font_size = int(longside / 40) #控制字体大小，此数值越大，字体显示越小
        target_date = datetime.strptime(target_date, '%Y-%m-%d').date()
        formatted_date = target_date.strftime('%Y-%m-%d')
        # 计算天数、月数和年数
        delta = date_taken - target_date
        days = delta.days
        if days < 0:
            text = f'{formatted_date}之前的照片'
        elif days <= 100:
            text = f'{days}天'
        elif days < 365:
            months = days // 30
            days = days % 30
            if days == 0:
                text = f'{months}个月'
            else:
                text = f'{months}个月{days}天'
        else:
            years = days // 365
            months = (days % 365) // 30
            days = (days % 365) % 30
            if months == 0 and days == 0:
                text = f'{years}岁'
            elif months == 0:
                text = f'{years}岁零{days}天'
            elif days == 0:
                text = f'{years}岁{months}个月'
            else:
                text = f'{years}岁{months}个月{days}天'
        # 在图像上添加文本
        draw = ImageDraw.Draw(image)
        if font is None:
            font = ImageFont.truetype('msyh.ttc', size=font_size) # 此处指定字体为雅黑
        text_bbox = font.getbbox(text)
        text_width, text_height = text_bbox[2], text_bbox[3]
        x = img_width - text_width - 80 #右侧预留80像素
        y = img_height - text_height * 2 - 50 #下侧预留50像素
        draw.text((x + text_width//2, y + text_height//2), str(date_taken), fill='magenta', anchor='mm', font=font)
        draw.text((x + text_width//2, y + text_height*3//2), text, fill='magenta', anchor='mm', font=font)
        # 将处理后的图像保存到指定的输出目录
        output_path = os.path.join(output_dir, os.path.relpath(image_path, input_dir))
        output_dir = os.path.dirname(output_path)
        os.makedirs(output_dir, exist_ok=True)
        image.save(output_path, quality=95)

if __name__ == '__main__':
    while True:
        date_str = input("请输入一个日期（比如小孩的生日），格式为:20200321:")
        try:
            target_date = datetime.strptime(date_str, '%Y%m%d').date().strftime('%Y-%m-%d')
            break
        except ValueError:
            print("输入日期格式不正确，请重新输入")

    input_dir = os.getcwd()
    output_dir = 'D:\\已处理\\'

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg')):
                image_path = os.path.join(root, file)
                print(f"正在处理图片: {file}")
                process_image(image_path, output_dir, target_date)

    print("处理完毕，按任意键退出本程序并打开 D:\\已处理")
    msvcrt.getch()

os.system('start "" "D:\\已处理"')
