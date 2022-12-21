"""
Convert runs(.trec) into monot5 input
with the format: Query: <q> Document: <d> Relevant:
"""
import argparse
import collections
from torch.utils.data import DataLoader
from datasets import Dataset
from datacollator import DataCollatorFormonoT5
from utils import load_runs, load_collections, load_multilingual_topics, normalized


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    # Load triplet
    parser.add_argument("--run", type=str, required=True,)
    parser.add_argument("--topic", type=str, required=True, help='same as query')
    parser.add_argument("--qvalue", type=str, required=True, help='same as query')
    parser.add_argument("--collection", type=str, required=True,)
    # Reranking conditions
    parser.add_argument("--output", type=str, default="")
    parser.add_argument("--batch_size", type=int, default=16)
    # for CLIR
    parser.add_argument("--lang", type=str, required=True,)
    parser.add_argument("--source", type=str, required=True,)
    parser.add_argument("--dq", action='store_true', default=False)
    parser.add_argument("--clr", action='store_true', default=False)
    args = parser.parse_args()

    # load triplet
    queries = load_multilingual_topics(args.topic, lang=args.lang, src=args.source)
    passages = load_collections(path=args.collection)
    runs = load_runs(args.run)

    # prepare dataset
    data = collections.defaultdict(list)
    for qid in runs:
        if "+" in args.qvalue:
            query_text = " ".join([queries[v]] in args.qvalue.split("+"))
            query_en_text = " ".join([queries[f"orig_{v}"]] in args.qvalue.split("+"))
        else:
            query_text = queries[qid][args.qvalue]
            query_en_text = queries[qid][f"orig_{args.qvalue}"]
        for pid in runs[qid]:
            data['qid'].append(qid)
            data['pid'].append(pid)
            data['query'].append(query_text)
            data['query_en'].append(query_en_text)
            data['passage'].append(normalized(passages[pid]))

    dataset = Dataset.from_dict(data)

    # data loader
    datacollator = DataCollatorFormonoT5(
            return_text=True, 
            istrain=False,
            dq=args.dq,
            clr=args.clr
    )
    dataloader = DataLoader(
            dataset,
            batch_size=args.batch_size,
            shuffle=False, # cannot be shuffle
            collate_fn=datacollator
    )

    # output examples (to be inferenced)
    fout = open(args.output, 'w')
    for b, batch in enumerate(dataloader):
        batch_inputs, batch_ids = batch

        for example in batch_inputs:
            fout.write(example+'\n')

        if b % 1000 == 0:
            print(f"{b} batches qp pair written")

    fout.close()

