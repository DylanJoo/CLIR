# Cross-linugal Information Retrieval

1. Prepare requirements


- Download topics & preprocessing
In this repo, I used HC4 for evaluation. The parsing procedure of HC4 please follow [HC4](https://github.com/hltcoe/HC4) for detail. The following are the parsed files, the detail processing codes please refer to [here](data/hc4/README.md)

- You will need to index the hc4 corpus (separately indexed for different languages)

```
train.topics.v1-0.jsonl
dev.topics.v1-0.jsonl
test.topics.v1-0.jsonl
```

2. Pre-proocessing datasets 

Processed the parsed topic queries (aggreagted into one files) by the following codes.:w
```
# change the 'dev' into split to get corresponding processed jsonl
python3 tools/extract_hc4_topics_to_tsv.py \
  --topic data/hc4/dev.topics.v1-0.jsonl \
  --output data/hc4/dev.jsonl
```

3. Sparse-retrieval

Used pre-build lucene index, and retrieved top1000 passages
We here regared *human* translated title + *human* translated description as queries.
```
bash run_spr.sh
```

4. Re-ranking

5. Fine-tuning point-wise ranking models for multi-lingual

- Fine-tuning with "dual-ligual queries" (abbreviated as dq)
- Fine-tuning with "cross-ligual relevance fine-tuning" (abbreviated as clf)

6. Convert the logits of ('true' and 'false') into probabilties.
```
bash run_rank_from_scores.sh
```
