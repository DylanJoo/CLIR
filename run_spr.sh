export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

mkdir -p runs

for split in dev test;do
    for lang in fas rus zho;do
        mkdir -p runs/$lang
        for src in human sockeye;do
          python3 tools/sparse_retrieval.py \
              -k 1000 -k1 0.82 -b 0.68 \
              -index /tmp2/trec/hc4/indexes/hc4_${lang}_tc_jsonl \
              -query data/hc4/${split}.jsonl \
              -qval title+desc \
              -lang $lang \
              -src human \
              -output runs/${lang}/hc4.${lang}.${split}.${src}.td.spr.top1000.trec
        done
    done
done
