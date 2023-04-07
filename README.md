# Age-Watermark

特别说明：本程序代码部分来自New Bing，我提出需求，New Bing给出代码，循环往复
不断优化直至变得基本可用，请各位大神斧正，增加更多功能。

程序功能：

批量给图片增加水印，水印内容为照片拍摄日期，以及拍摄日期到指定时间的间隔时间。
例如指定时间为小孩的出生日期，程序会自动计算照片拍摄当天小孩的年纪。
如果小于等于100天，直接显示为天数；
100天以上，1岁以下显示几个月几天（如果天数为零，则只显示几个月）；
一岁以后显示几岁几个月几天，其中月数为零，则不显示月数，只显示几
岁，零几天；
天数如果为零，则显示几岁几个月。
默认字体：微软雅黑，字号：45，颜色：magenta

程序已添加注释，请按实际需要自行更改。

用法：

将Age-Watermark-1.3.exe文件放到需要处理的图片文件夹，双击运行，手动输入小孩生日后，
程序将自动为当前文件夹及其子目录中所有图片添加水印，水印内容包含：1、照片拍摄时间；
2、照片拍摄时小孩的年龄（根据程序启动时手动指定的生日计算得来），按原目录结构将处
理后的图片同意保存至 D:\已处理\ 文件夹。

Note: The code for this program was partially provided by New Bing. I requested the functionality and New Bing provided the code, with iterative improvements until it became functional. Please feel free to refine and add more features.

Program Functionality:
Batch adding watermarks to images with the watermark content being the date the photo was taken and the time interval between the date of the photo and a specified time. For example, if the specified time is the child's birthdate, the program will automatically calculate the age of the child on the day the photo was taken. If the age is less than or equal to 100 days, it will be displayed as the number of days. If the age is over 100 days but still under 1 year old, it will display as the number of months and days (if the number of days is zero, only the number of months will be displayed). If the child is over 1 year old, it will display as the number of years, months, and days (if the number of months is zero, only the number of years and days will be displayed). If the number of days is zero, it will display as the number of years and months.

Default font: Microsoft YaHei, font size: 45, color: magenta.

The program has been commented in the code, so please modify it according to your actual needs.

Usage:
Place the Age-Watermark-1.3.exe file in the folder containing the images to be processed, double-click to run, manually enter the child's birthdate, and the program will automatically add watermarks to all images in the current folder and its subdirectories. The watermark content includes: 1. the date the photo was taken; 2. the age of the child at the time the photo was taken (calculated based on the manually specified birthdate when the program started). The processed images will be saved in the D:\Processed\ folder while maintaining the original directory structure.
