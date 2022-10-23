# Cross-linugal Information Retrieval

0. Download topics & preprocessing

In this repo, I used HC4 for evaluation. The parsing procedure of HC4 please follow [HC4](https://github.com/hltcoe/HC4) for detail. 

The following are the parsed files.
```
train.topics.v1-0.jsonl
dev.topics.v1-0.jsonl
test.topics.v1-0.jsonl
```

1. Requirements
    * Indexed collection

2. Pre-proocessing datasets 

```
python3 tools/extract_hc4_topics_to_tsv.py \
  --topic data/hc4/dev.topics.v1-0.jsonl \
  --output data/hc4/dev.jsonl

# processed train/dev/test
```

3. Sparse-retrieval

Used pre-build lucene index, and retrieved top1000 passages
We here regared *human* translated title + *human* translated description as queries.
```
bash run_spr.sh
```

4. Re-ranking
