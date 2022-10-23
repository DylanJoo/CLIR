### HC4 

- Queries (topics)

The parsed tsv from original json files, 
```
Format: qid@lang#source<\tab>qtitle qdescription
```
    * Parsed tsv : {train/dev/test}.topics.v1-0.tsv

The following queries are machine translated or humna translated (already parsed), 

> Noted that the queries in qrels files didn't match topic file, 
the following queries are filtered based on qrels (judgement available)
```
Format: qid@lang#source<\tab>qtitle qdescription
```
    * Train tsv: {fas/rus/zho}/train.topics.v1-0.tsv
    * Dev tsv: {fas/rus/zho}/dev.topics.v1-0.tsv
    * Test tsv: {fas/rus/zho}/test.topics.v1-0.tsv

And in case you need to check the raw data collect form web: 
    * Raw jsonl: {tratin/dev/test}.v1-0.jsonl

- Collections
```
The parsed json format is {"id": <docid>, "contents": <doctext>}
```
    * raw: cfda4:/tmp2/trec/hc4/{fas/rus/zho}/hc4_docs.jsonl
    * parsed content: cfda4:/tmp2/trec/hc4/{fas/rus/zho}/hc4_docs_c.tsv

- Indexes (i've linked the indexed files on cfda4)
    * fas: cfda4:/tmp2/jhju/indexes/hc4_fas_{c/tc}_jsonl
    * rus: cfda4:/tmp2/jhju/indexes/hc4_rus_{c/tc}_jsonl
    * zho: cfda4:/tmp2/jhju/indexes/hc4_zho_{c/tc}_jsonl

- Qrels
    * Train: {fas/rus/zho}/train.qrels.v1-0.txt
    * Dev: {fas/rus/zho}/dev.qrels.v1-0.txt
    * Test: {fas/rus/zho}/test.qrels.v1-0.txt


