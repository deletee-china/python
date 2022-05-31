from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

with open('juanwang_comments.csv', encoding='utf-8') as f:
    data = pd.read_csv(f)
text = str(data['comment'])

wordcloud=WordCloud(background_color='white',scale=1.5,font_path=r'~/Songti.ttc').generate(text)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
wordcloud.to_file('网易云音乐评价词云可视化2.png')