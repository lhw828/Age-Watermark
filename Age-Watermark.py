from PIL import Image, ImageDraw, ImageFont
from PIL.ExifTags import TAGS
from datetime import datetime, timedelta
import os

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
def process_image(image_path, output_dir):
    image = Image.open(image_path)
    date_taken = get_date_taken(image)
    if not date_taken:
        return
    # 指定目标日期（例如小孩的生日）
    target_date = datetime.strptime('2010-05-11', '%Y-%m-%d').date()
    # 计算天数、月数和年数    
    delta = date_taken - target_date
    days = delta.days
    if days <= 100:
        text = f'{days} 天'
    elif days < 365:
        months = days // 30
        days = days % 30
        if days == 0:
            text = f'{months} 个月'
        else:
            text = f'{months} 个月 {days} 天'
    else:
        years = days // 365
        months = (days % 365) // 30
        days = (days % 365) % 30
        if months == 0 and days == 0:
            text = f'{years} 岁'
        elif months == 0:
            text = f'{years} 岁零 {days} 天'
        elif days == 0:
            text = f'{years} 岁 {months} 个月'
        else:
            text = f'{years} 岁 {months} 个月 {days} 天'
    # 在图像上添加文本
    width, height = image.size
    draw = ImageDraw.Draw(image)
    #此处指定字体和字号，默认微软雅黑，45号 
    font = ImageFont.truetype('msyh.ttc', 45)
    text_bbox = font.getbbox(text)
    text_width, text_height = text_bbox[2], text_bbox[3]
    x = width - text_width - 10
    y1 = height - text_height * 2 - 10
    y2 = height - text_height - 10
    draw.text((x, y1), str(date_taken), fill='magenta', font=font)
    draw.text((x, y2), text, fill='magenta', font=font)
    # 将处理后的图像保存到指定的输出目录
    output_path = os.path.join(output_dir, os.path.basename(image_path))
    image.save(output_path,quality=95)

# 处理指定目录中的所有图像
def process_images(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(('.jpg', '.jpeg')):
                image_path = os.path.join(root, file)
                process_image(image_path, output_dir)

#指定要处理的图片所在目录
input_dir = 'D:\\tset\\'
#指定处理完的图片存储目录
output_dir = 'D:\\tset\\1\\'
process_images(input_dir, output_dir)
