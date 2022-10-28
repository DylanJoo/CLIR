import os
import collections
import re
import argparse
import json
from utils import load_runs, load_queries, load_collections, post_process_clir_queries

parser = argparse.ArgumentParser()
parser.add_argument("--run", type=str, required=False,)
parser.add_argument("--queries", type=str, required=True,)
parser.add_argument("--queries_source", type=str, required=True,)
parser.add_argument("--corpus", type=str, required=True,)
parser.add_argument("--output_text_pair", type=str, required=True)
parser.add_argument("--output_id_pair", type=str, required=True)
parser.add_argument("--queries_original", type=str, required=False, help='Only use for dual-query ranking')
parser.add_argument('--dq', action='store_true', default=False, help='query w/ multiple langs')
parser.add_argument('--clr', action='store_true', default=False, help='query w/ diff lang of psg.')
args = parser.parse_args()
# parser.add_argument('--lang', action='append')

runs = load_runs(path=args.run)
queries = load_queries(path=args.queries)
queries = post_process_clir_queries(queries=queries, source=args.queries_source)

if args.dq:
    queries_original = load_queries(path=args.queries_original)
    queries_original = post_process_clir_queries(queries_original, 'original')

if os.path.isdir(args.corpus):
    # directory
    collections = load_collections(dir=args.corpus)
else: 
    #path
    collections = load_collections(path=args.corpus)

with open(args.output_text_pair, 'w') as text_pair, \
     open(args.output_id_pair, 'w') as id_pair:

    for i, (qid, docid_ranklist) in enumerate(runs.items()):
        for k, docid in enumerate(docid_ranklist):

            if args.dq:
                text_pair.write(
                        f"Query: {queries_original[qid]} Query Translation: {queries[qid]} Document: {collections[docid]} Relevant:\n"
                ) 
                id_pair.write(f"{qid}\t{docid}\t{k+1}\n")

            if args.cross_lingual_relevant:
                text_pair.write(
                        f"Query: {queries[qid]} Document: {collections[docid]} Relevant:\n"
                ) 

            id_pair.write(f"{qid}\t{docid}\t{k+1}\n")

        if i % 1000 == 0:
            print(f'Creating monot5 re-ranking input ...{i}')

print("DONE!")
