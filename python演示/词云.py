from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import random
import jieba
def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h, s, l = random.choice([(188, 72, 53), (253, 63, 56), (12, 78, 69)])
    return "hsl({}, {}%, {}%)".format(h, s, l)
df = pd.read_csv('juanwang_comments.csv', encoding='utf-8-sig')
df = df.drop_duplicates('user_id')
df = df.dropna()
words = pd.read_csv('fergiemcdowall_stopwords_zh.txt',encoding='utf-8' ,sep='\t', names=['stopword'])
print(words)
text = ''
for line in df['user_name']:
    text += ' '.join(jieba.cut(str(line), cut_all=False))
stopwords = set('')
stopwords.update(words['stopword'])
wc = WordCloud(
    background_color='white',
    font_path=r'~/Songti.ttc',
    max_words=2000,
    max_font_size=250,
    min_font_size=15,
    color_func=random_color_func,
    prefer_horizontal=1,
    random_state=50,
    stopwords=stopwords
)

wc.generate_from_text(text)
process_word = WordCloud.process_text(wc, text)
sort = sorted(process_word.items(), key=lambda e: e[1], reverse=True)
print(sort[:50])
plt.imshow(wc)
plt.axis('off')
wc.to_file("juanwang_user词云.jpg")
print('生成词云成功!')