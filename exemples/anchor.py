from tmtk.topic_models import anchor

from tmtk.metrics.metrics import preplexity
from tmtk.collection.collection import BagOfWordsCollections

collection_train = BagOfWordsCollections(
    path='/home/oem/Dropbox/projests/Python/tmtk/tmtk/corpa/bag_of_words/wiki_ru_article',
    name='wiki_ru_article_train'
).fill()

collection_test = BagOfWordsCollections(
    path='/home/oem/Dropbox/projests/Python/tmtk/tmtk/corpa/bag_of_words/wiki_ru_article',
    name='wiki_ru_article_test'
).fill()

F, anchors_wrd = anchor.anchor_model(
    collection_train.documents, collection_test.documents,
    wrd_count=len(collection_train.id_to_words), metric=preplexity
)

anchor.print_topics(F, collection_train.id_to_words, anchors_wrd)