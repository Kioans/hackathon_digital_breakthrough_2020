import pandas
import nltk
import re
import string
import pymorphy2


def tokenize(text):
    text = text.lower()
    text = re.sub('r^[^a-zA-Z ^0-9]', '', str(text))
    return text.split()


def split_by(text, char):
    while text.find(char) >= 0:
        text = text.replace(char, ' ')
    return text


def remove_punctuation(text):
    chars = string.punctuation + '\n\xa0«»\t—…'
    return "".join([ch for ch in text if ch not in chars])


def remove_numbers(text):
    chars = string.digits
    return "".join([ch for ch in text if ch not in chars])


def remove_stopwords(text):
    stop_words = set(nltk.corpus.stopwords.words("russian"))
    return [word for word in text if word not in stop_words]


def to_normal_form(text):
    morph = pymorphy2.MorphAnalyzer()
    morphed_words = []
    for word in text:
        temp = morph.parse(word)[0]
        morphed_words.append(temp.normal_form)
    return morphed_words


def filter_text(text):
    text = text.lower()
    text = split_by(text, '-')
    text = remove_punctuation(text)
    text = remove_numbers(text)
    text = nltk.word_tokenize(text)
    text = remove_stopwords(text)
    text = to_normal_form(text)
    result = ""
    for elem in text:
        result += elem + " "
    return result


def make_labels(y_data, unique):
    labels = dict([(unique[i], i) for i in range(0, len(unique))])
    new_data = []
    for elem in y_data:
        new_data.append(labels[elem])
    return new_data, labels


def get_normalized_words():
    data_frame = pandas.read_excel(io='dataset.xlsx',
                                   engine='openpyxl',
                                   usecols='A:B',
                                   sheet_name="WithoutAdds")

    y_data = list(data_frame.loc[:, 'answers'])
    x_data_unfiltered = list(data_frame.loc[:, 'question'])

    print(y_data)

    y_unique_values = set(y_data)
    y_unique_values = list(y_unique_values)

    y_data, y_labels = make_labels(y_data, y_unique_values)

    nltk.download('wordnet')
    nltk.download('stopwords')
    x_data = []
    unique_words = set()
    for line in x_data_unfiltered:
        ans = filter_text(line)
        for elem in ans:
            unique_words.add(elem)
        x_data.append(ans)

    data = [(x_data[i], y_data[i]) for i in range(0, len(x_data))]
    x_data_df = pandas.DataFrame(data)
    x_data_df.to_excel('input.xlsx')
    y_labels_df = pandas.DataFrame(list(y_labels.keys()))
    y_labels_df.to_excel('labels.xlsx')

    return x_data, y_data, y_labels


get_normalized_words()