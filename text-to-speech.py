# by rakuzan2weak
import nltk
from newspaper import Article
from gtts import gTTS


def text_to_speech(url):
 article = Article(url)
 article.download()
 article.parse()
 nltk.download('punkt')
 article.nlp()
 article_text = article.text
 language = 'ru' # выбирайте язык
 my_obj = gTTS(text=article_text, lang=language, slow=False)
 my_obj.save("text-to-speech-by-rakuzan2weak.mp3")


if __name__ == '__main__':
 text_to_speech(
 url='https://habr.com/ru/articles/675492/' # ваша ссылка на сайт, который хотите озвучить
 )