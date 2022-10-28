import os
import argparse
import random
from datasets import load_dataset

def multilingual_pairs(writer, dataset_en, datasets):
    """ Input the query and passage with same languages, which random sampled.
    standard monoMT5 settings (but only 3 languages)
    """
    datasets['english'] = dataset_en

    for i in range(len(dataset_en['train'])):

        # queries and passages
        lang = random.sample(datasets.keys(), 1)[0]
        example = datasets[lang]['train'][i]

        query = example['query']
        passage_pos = example['positive']
        passage_neg = example['negative']

        writer.write(f"Query: {query} Document: {passage_pos} Relevant:\tyes\n")
        writer.write(f"Query: {query} Document: {passage_neg} Relevant:\tno\n")

        if i % 100000 == 0:
            print(f"{i} multilingual query-document pairs finished..., {len(datasets.keys())} languages fused.")

def cross_lingual_relevant_pairs(writer, dataset_en, datasets):
    """ Input the query and passage with different languages

    (1) Monolingual (source lang to target lang) if only one language in datasets
    (2) Multilingual (source lang to mulitple kinds of target lang) if multiple languages specified.
    """
    for i, example_en in enumerate(dataset_en['train']):

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
            print(f"{i} Cross-lingual-query-document pair finished..., {len(args.lang)} languages fused.")


def dual_query_ranking_pairs(writer, dataset_en, datasets):
    """ Input the two queries (source langugae and target language) as new query source. 

    (1) Monolingual if only one language in datasets
    (2) Multilingual if multiple languages in datasets
    """
    for i, example_en in enumerate(dataset_en['train']):

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
            print(f"{i} Dual-query-document pair finished..., {len(args.lang)} languages fused.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert MSMARCO tsv passage collection into jsonl files for Anserini.')
    parser.add_argument('--lang', action='append')
    parser.add_argument('--output', required=True, help='Output folder.')
    parser.add_argument('--cross-lingual-relevant', action='store_true', default=False, help='query w/ diff lang of psg.')
    parser.add_argument('--dual-lingual-ranking', action='store_true', default=False, help='query w/ multiple langs')
    parser.add_argument('--multilingual', action='store_true', default=False, help='query-passage multilingual pair')

    args = parser.parse_args()
    f = open(args.output, 'w')

    # multilingual marco
    dataset_en = load_dataset("unicamp-dl/mmarco", 'english', cache_dir='/tmp2/jhju/hf_datasets')
    assert 'english' not in args.lang, 'cannot be english'

    datasets = {}
    for lang in args.lang:
        datasets[lang] = load_dataset("unicamp-dl/mmarco", lang, cache_dir='/tmp2/jhju/hf_datasets')

    if args.cross_lingual_relevant:
        cross_lingual_relevant_pairs(f, dataset_en, datasets)

    if args.dual_lingual_ranking:
        dual_query_ranking_pairs(f, dataset_en, datasets)

    if args.multilingual:
        multilingual_pairs(f, dataset_en, datasets)

    f.close()
    print('Done!')
