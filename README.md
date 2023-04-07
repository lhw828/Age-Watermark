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
程序将自动处理当前文件夹及其子目录中所有图片，并按原目录结构将处理后的图片同意保存至D:\已处理\文件夹。

Add watermarks to photos in batches. The watermark content is the date 
the photo was taken and the interval between the date the photo was 
taken and a specified time. For example, if the specified time is the 
child’s date of birth, the program will automatically calculate the 
child’s age on the day the photo was taken. If it is less than or 
equal to 100 days, it will be displayed directly as days; if it is 
more than 100 days and less than 1 year old, it will be displayed as 
several months and several days (if the number of days is zero, only 
several months will be displayed); if it is more than 1 year old, it 
will be displayed as several years old, several months and several days. 
If the number of months is zero, only a few years old and a few days will 
be displayed; if the number of days is zero, only a few years old and a 
few months will be displayed.
