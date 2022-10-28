import os
import collections
import re
import argparse
import json
from utils import load_runs, load_queries, load_collections

def dual_lingual_query_passage_pair(qtext_orig, qtext, dtext):
    """
    qtext: English query 
    qtext_trans: Translated query from English
    """
    return f"Query: {qtext_orig} Query Translation: {qtext} Document: {dtext} Relevant:\n"

def solo_relevant_pair(qtext, dtext):
    return f"Query: {qtext} Document: {dtext} Relevant:\n"

def convert_to_monot5(args):

    # laod requirments
    runs, _ = load_runs(args.run, 1000)
    queries = load_queries(args.queries, args.lang, args.source)

    if args.dual_lingual_ranking:
        queries_orig = load_queries(args.queries, 'eng', 'original')

    if os.path.isdir(args.corpus):
        collections = load_collections(dir=args.corpus)
    else:
        collections = load_collections(path=args.corpus)


    with open(args.output_text_pair, 'w') as text_pair, \
         open(args.output_id_pair, 'w') as id_pair:

        for i, (qid, docid_ranklist) in enumerate(runs.items()):
            for k, docid in enumerate(docid_ranklist):

                if args.dual_lingual_ranking:
                    query_passage_pair = dual_lingual_query_passage_pair(
                            queries_orig[qid], queries[qid], collections[docid]
                    )
                else:
                    query_passage_pair = solo_relevant_pair(queries[qid], collections[docid])

                text_pair.write(query_passage_pair)
                id_pair.write(f"{qid}\t{docid}\t{k+1}\n")

            if i % 1000 == 0:
                print(f'Creating re-ranking input ...{i}')

    print("DONE!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-run", "--run", type=str, required=False,)
    parser.add_argument("-q", "--queries", type=str, required=True,)
    parser.add_argument("-corpus", "--corpus", type=str, required=True,)
    parser.add_argument("--output_text_pair", type=str, required=True,)
    parser.add_argument("--output_id_pair", type=str, required=True,)
    #
    parser.add_argument('--lang', type=str, required=True, default='eng')
    parser.add_argument('--source', type=str, required=True, default='original')
    parser.add_argument('--dual-lingual-ranking', action='store_true', default=False)

    args = parser.parse_args()
    convert_to_monot5(args)
