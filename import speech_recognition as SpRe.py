import speech_recognition as SpRe
import nltk
from nltk.corpus import wordnet

def Mysecretary_listen():
    recognizer = SpRe.Recognizer()
    with SpRe.Microphone() as source:
        # source 聲音的來源:電腦麥克風
        audio_data = recognizer.listen(source)

    try:
        # audio_data 儲存聲源, language 指定語系
        content = recognizer.recognize_google(audio_data, language='zh-tw')
        return content

    except:
        return '請再說一遍!!'

def get_adjective(word):
    """獲取指定名詞的形容詞"""
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            for ant in lemma.antonyms():
                synonyms.append(ant.name())
            synonyms.append(lemma.name())
    return synonyms

def modify_text(text):
    """將文本修飾得更順暢"""
    tokens = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    modified_text = []
    for word, pos in pos_tags:
        if pos.startswith('NN') and word == 'Games':  # 如果是名詞且是我們要找的關鍵字
            modified_text.extend(['incredible', 'Games'])  # 添加形容詞修飾
        else:
            modified_text.append(word)  # 其他詞性保留原詞
    return " ".join(modified_text)

def find_keyword(text, keyword):
    """在修飾後的文本中找尋關鍵字"""
    modified_text = modify_text(text)
    tokens = nltk.word_tokenize(modified_text)
    return keyword in tokens

# 測試
question = Mysecretary_listen()
print("修飾前的問題:",question)
modified_question = modify_text(question)
print("修飾後的問題:", modified_question)

keyword = "Games"  # 想要找尋的關鍵字

if find_keyword(modified_question, keyword):
    print(f"在文本中找到了關鍵字 '{keyword}'")
else:
    print(f"在文本中未找到關鍵字 '{keyword}'")