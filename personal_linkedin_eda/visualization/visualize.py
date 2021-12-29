import matplotlib.pyplot as plt
from wordcloud import WordCloud
from typing import List


def show_word_cloud(
    text: str,
    max_words: int = 15,
    height: int = 380,
    stopwords: List[str] = [],
    collocations: bool = False,
):
    wrd = WordCloud(
        background_color="white",
        width=700,
        height=height,
        margin=0,
        collocations=collocations,
        max_words=max_words,
        colormap="winter",
        stopwords=stopwords,
    )
    wordcloud = wrd.generate(text)

    plt.figure(figsize=(30, 15))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
