from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk import sent_tokenize

# From https://becominghuman.ai/text-summarization-in-5-steps-using-nltk-65b21e352b65

def get_frequency_table(text):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
    ps = PorterStemmer()

    frequency_table = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in frequency_table:
            frequency_table[word] += 1
        else:
            frequency_table[word] = 1

    return frequency_table

def score_sentences(sentences, frequency_table):
    sentence_scores = dict()
    for sentence in sentences:
        word_count_in_sentence = len(word_tokenize(sentence))
        for word in frequency_table:
            if word in sentence.lower():
                if sentence[:10] in sentence_scores:
                    sentence_scores[sentence[:10]] += frequency_table[word]
                else:
                    sentence_scores[sentence[:10]] = frequency_table[word]
        sentence_scores[sentence[:10]] //= word_count_in_sentence
    return sentence_scores

def find_threshold(scores):
    '''
    Return the score threshold (average score of sentences)
    '''
    return sum(scores.values()) // len(scores)

def generate_summary(sentences, scores, threshold):
    summary = ''
    for sentence in sentences:
        if scores[sentence[:10]] >= threshold:
            summary += ' ' + sentence
    return summary

def summarize(text):
    frequency_table = get_frequency_table(text)
    sentences = sent_tokenize(text)
    scores = score_sentences(sentences, frequency_table)
    threshold = find_threshold(scores)
    return generate_summary(sentences, scores, threshold)


if __name__ == "__main__":
    with open("./quantum_physics_wikipedia.txt", "r") as f:
        text = f.read()
        print(summarize(text))
    
