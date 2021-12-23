from paraphrase1 import get_response
from sentence_splitter import SentenceSplitter, split_text_into_sentences
#processing
def paraphrase(contexts_list):
    contexts = contexts_list
    paraphrased_list = []
    for z in contexts:
        splitter = SentenceSplitter(language='en')

        sentence_list = splitter.split(z)
        sentence_list
        paraphrase = []

        for i in sentence_list:
            a = get_response(i,1)
            paraphrase.append(a)

        paraphrase2 = [' '.join(x) for x in paraphrase]

        paraphrase3 = [' '.join(x for x in paraphrase2) ]
        paraphrased_text = str(paraphrase3).strip('[]').strip("'")
        paraphrased_list.append(paraphrased_text)
    return paraphrased_list


list1 = ['hi i am sneh','where do you live','who are you?']
x = paraphrase(list1)
print(x)