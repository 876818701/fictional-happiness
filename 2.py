from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import  jieba
def GetWordCloud():
   path_txt = './Peaky Blinders.txt'
   path_img = "D:/DOWNLOAD/162054507.jpg"
   f = open(path_txt, 'r', encoding='UTF-8').read()
   background_image = np.array(Image.open(path_img))

   cut_text = " ".join(jieba.cut(f))
 
   wordcloud = WordCloud(
      
       font_path="C:/Windows/Fonts/GLECB.TTF",
       background_color="white",
       
       mask=background_image,
       max_words=5000).generate(cut_text)
       
   # 生成颜色值
   image_colors = ImageColorGenerator(background_image)
   # 下面代码表示显示图片
   plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
   plt.axis("off")
   plt.show()
 
if __name__ == '__main__':
   GetWordCloud()
