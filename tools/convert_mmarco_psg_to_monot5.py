import os
import argparse
import random
from datasets import load_dataset

def cross_lingual_pairs(writer, datasets):
    """ Input the query and passage with different languages
    (1) Monolingual (source lang to target lang) if only one language in datasets
    (2) Multilingual (source lang to mulitple kinds of target lang) if multiple languages specified.
    """
    for i, example_en in enumerate(datasets['english']['train']):

        query_en = example_en['query']

        # queries and passages
        lang = random.sample(args.lang, 1)[0]
        example = datasets[lang]['train'][i]

        query = example['query']
        passage_pos = example['positive']
        passage_neg = example['negative']

        writer.write(f"Query: {query_en} Document: {passage_pos} Relevant:\tyes\n")
        writer.write(f"Query: {query_en} Document: {passage_neg} Relevant:\tno\n")

        if i % 100000 == 0:
            print(f"{i} Cross-lingual qp pair finished...")


def dualingual_query_pairs(writer, datasets):
    """ Input the two queries (source langugae and target language) as new query source. 
    (1) Monolingual if only one language in datasets
    (2) Multilingual if multiple languages in datasets
    """
    for i, example_en in enumerate(datasets['english']['train']):

        query_en = example_en['query']

        # queries and passages
        lang = random.sample(args.lang, 1)[0]
        example = datasets[lang]['train'][i]

        query = example['query']
        passage_pos = example['positive']
        passage_neg = example['negative']

        writer.write(f"Query: {query_en} Query Translation: {query} Document: {passage_pos} Relevant:\tyes\n")
        writer.write(f"Query: {query_en} Query Translation: {query} Document: {passage_neg} Relevant:\tno\n")

        if i % 100000 == 0:
            print(f"{i} Dualingual-query pair finished...")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert MSMARCO tsv passage collection into jsonl files for Anserini.')
    parser.add_argument('--lang', action='append')
    parser.add_argument('--output', required=True, help='Output folder.')
    parser.add_argument('--clf', action='store_true', default=False, help='cross-lingual passage retrieval.')
    parser.add_argument('--dq', action='store_true', default=False, help='query with soruce & target contents.')
    args = parser.parse_args()

    # multilingual marco
    assert 'english' not in args.lang, 'cannot be english'
    datasets = {}
    for lang in args.lang + ['english']:
        datasets[lang] = load_dataset("unicamp-dl/mmarco", lang, data_dir='/tmp2/huggingface/hf_datasets', cache_dir='/tmp2/jhju/cache')

    with open(args.output, 'w') as f:
        if args.clf:
            cross_lingual_pairs(f, datasets)

        if args.dq:
            dualingual_query_pairs(f, datasets)

    print('Done!')
