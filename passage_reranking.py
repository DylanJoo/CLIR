import argparse
import collections
from reranker import monoMT5
from torch.utils.data import DataLoader
from typing import Optional, Union, List, Dict, Any
from dataclasses import dataclass
from tools.utils import load_runs, load_collections, load_multilingual_topics
from datasets import Dataset
from datacollator import DataCollatorFormonoT5

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    # Load triplet 
    parser.add_argument("--run", type=str, required=True,)
    parser.add_argument("--topic", type=str, required=True,)
    parser.add_argument("--collection", type=str, required=True,)
    # Reranking conditions
    parser.add_argument("--topk", type=int, default=1000)
    parser.add_argument("--output_trec", type=str, required=True)
    parser.add_argument("--model_name_or_path", type=str, default='unicamp-dl/mt5-base-mmarco-v2')
    parser.add_argument("--batch_size", type=int, default=16)
    parser.add_argument("--max_length", type=int, default=512)
    parser.add_argument("--gpu", type=str, default='0')
    parser.add_argument("--prefix", type=str, default='monoMT5')
    # Multi-lingual specific settings
    parser.add_argument("--lang", type=str, required='zho')
    parser.add_argument("--src", type=str, required='human')
    args = parser.parse_args()

    fout = open(args.output_trec, 'w')

    # load model
    model = monoMT5.from_pretrained(args.model_name_or_path)
    model.set_tokenizer()
    model.set_targets(['yes', 'no'])
    model.to(f'cuda:{args.gpu}')
    model.eval()

    # load triplet
    queries = load_multilingual_topics(args.topic, lang=args.lang, src=args.src)
    passages = load_collections(path=args.collection)
    runs = load_runs(args.run)

    # prepare dataset 
    data = collections.defaultdict(list)
    # we use only desc for reranking (close to question)
    for qid in runs:
        query_text = queries[qid]
        for pid in runs[qid]:
            data['qid'].append(qid)
            data['pid'].append(pid)
            data['query'].append(query_text['desc']) 
            data['passage'].append(passages[pid])

    dataset = Dataset.from_dict(data)

    # data loader
    datacollator = DataCollatorFormonoT5(
            tokenizer=model.tokenizer,
            padding=True,
            max_length=args.max_length,
            truncation=True,
            return_tensors="pt"
    )
    dataloader = DataLoader(
            dataset,
            batch_size=args.batch_size,
            shuffle=False,
            collate_fn=datacollator
    )

    # prediction
    ranking_list = collections.defaultdict(list)
    for b, batch in enumerate(dataloader):
        batch_inputs, ids = batch
        output = model.predict(batch_inputs)

        true_prob = output[:, 0]
        false_prob = output[:, 1]

        for t_prob, (qid, docid) in zip(true_prob, ids):
            ranking_list[qid].append((docid, t_prob))

        if b % 1000 == 0:
            print(f"{b} qp pair inferencing")

    # output
    for i, (qid, candidate_passage_list) in enumerate(ranking_list.items()):
        # Using true prob as score, so reverse the order.
        candidate_passage_list = sorted(candidate_passage_list, key=lambda x: x[1], reverse=True)

        for idx, (docid, t_prob) in enumerate(candidate_passage_list[:1000]):
            example = f'{qid} Q0 {docid} {str(idx+1)} {t_prob} {args.prefix}\n'
            fout.write(example)

        if i % 10 == 0:
            print(f"{i} topics reranked")

    fout.close()


