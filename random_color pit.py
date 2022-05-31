from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import string

#混合字符串，可自定义
basic_string = '0123456789'+string.ascii_letters+'9876543210'
def randColor():  #产生随机颜色
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))#颜色可以通过对数字的随机性来得出颜色所以是三位randit()函数是对(a,b)之间进行随机数的选择

def randChar():  #产生随机数字字母组合列表
    return random.sample(basic_string,4)#chr(random.randint(65,90))#sample()是对随机数组进行切割

def pictureDraw():

    height=100
    width=300
    image=Image.new('RGB',(width,height),(255,255,255))  #白色画布用RGB的方式
    font=ImageFont.truetype("/Users/kein/Library/Fonts/FuraMono-Medium Powerline.otf",80)        #画笔字体
    draw=ImageDraw.Draw(image)   #绘画对象
    for i in range(width):
        for j in range(height):
            draw.point((i,j),fill=randColor())     #随机逐像素填充颜色

    for i in range(4):
        draw.text((60*i+10,19),randChar()[i],font=font,fill=(random.randint(30,120),random.randint(30,120),random.randint(30,120)))  #文本绘画

    image=image.filter(ImageFilter.BLUR)  #产生模糊感
    image.save('CAPTCHA.jpg','jpeg')
    image.show()

if __name__=='__main__':
    pictureDraw()
