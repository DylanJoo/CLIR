import json
import argparse
from pyserini.search.lucene import LuceneSearcher

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--retrieve_k_docs", default=1000, type=int)
parser.add_argument("-k1", "--k1", default=float(0.9), type=float)
parser.add_argument("-b", "--b", default=float(0.4), type=float)
parser.add_argument("-index", "--dir_index", default=None, type=str)
parser.add_argument("-query", "--path_qtext", default='sample_queries.tsv', type=str)
parser.add_argument("-qval", "--qvalue", type=str)
parser.add_argument("-lang", "--lang", type=str)
parser.add_argument("-src", "--source", type=str, default='human')
parser.add_argument("-output", "--path_output", default='run.sample.txt', type=str)
args = parser.parse_args()

def search(args):
    # Lucuene initialization
    searcher = LuceneSearcher(args.dir_index)
    searcher.set_bm25(k1=args.k1, b=args.b)
    searcher.set_language(args.lang[:-1])

    # Load query text and query ids (support .jsonl only)
    query_file = []
    with open(args.path_qtext) as f:
        for line in f:
            data = json.loads(line.strip())
            if "+" in args.qvalue:
                qvalues = " ".join([data[v] for v in args.qvalue.split("+")])
            else:
                qvalues = data[args.qvalue]

            if args.lang in data['lang'] and args.source == data['src']:
                query_file.append((data['id'], qvalues))


    # Prepare the output file
    with open(args.path_output, 'w') as fout:

        # search for each q
        for qi, (index, text) in enumerate(query_file):
            hits = searcher.search(text.strip(), k=args.retrieve_k_docs)

            for i in range(len(hits)):
                fout.write(f'{index} Q0 {hits[i].docid:4} {i+1} {hits[i].score:.5f} pyserini\n')

            if qi % 100 == 0:
                print(f'{qi+1} query retrieved ...')
search(args)
print("DONE")
