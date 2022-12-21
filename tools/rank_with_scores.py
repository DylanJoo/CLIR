import json
import argparse
import collections
import numpy as np
from utils import load_scores


def rerank_runs(args):

    scores_list = load_scores(args.scores)
    ranked_run = collections.defaultdict(list)

    # align the scores
    with open(args.run, "r") as baseline:

        for i, (scores, run_line) in enumerate(zip(scores_list, baseline)):
            true_prob = scores[0]
            qid, _, docid, rank, score, _ = run_line.strip().split()
            ranked_run[qid].append((docid, true_prob))

    # reranking
    with open(args.output, 'w') as fout:

        for qid in ranked_run:

            # Using true prob as score, so reverse the order.
            ranked_result = sorted(ranked_run[qid], key=lambda x: x[1], reverse=True)

            for idx, (docid, true_prob) in enumerate(ranked_result):
                example = f"{qid} Q0 {docid} {str(idx+1)} {true_prob} {args.prefix}\n"
                fout.write(example)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--run", type=str, required=True,)
    parser.add_argument("--scores", type=str, required=True,)
    parser.add_argument("--output", type=str, default="")
    parser.add_argument("--prefix", type=str, default="monomt5-dq")
    args = parser.parse_args()

    #
    rerank_runs(args)
    print('done')

