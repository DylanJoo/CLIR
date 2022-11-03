# dq
for split in dev test;do
    for lang in fas rus zho;do
        for src in human;do
            python3 tools/convert_runs_to_monot5.py \
                --run runs/${lang}/hc4.${lang}.${split}.${src}.td.spr.top1000.trec \
                --topic data/hc4/${split}.jsonl \
                --collection /tmp2/trec/hc4/${lang}/hc4_docs_tc.jsonl \
                --qvalue desc \
                --output data/hc4/infer/${lang}/hc4.${lang}.${split}.${src}.monomT5.dq.infer.tsv \
                --batch_size 16 \
                --lang ${lang} \
                --source ${src} \
                --dq
        done
    done
done

# clf
for split in dev test;do
    for lang in fas rus zho;do
        for src in human;do
            python3 tools/convert_runs_to_monot5.py \
                --run runs/${lang}/hc4.${lang}.${split}.${src}.td.spr.top1000.trec \
                --topic data/hc4/${split}.jsonl \
                --collection /tmp2/trec/hc4/${lang}/hc4_docs_tc.jsonl \
                --qvalue desc \
                --output data/hc4/infer/${lang}/hc4.${lang}.${split}.${src}.monomT5.clf.infer.tsv \
                --batch_size 16 \
                --lang ${lang} \
                --source ${src} \
                --clf 
        done
    done
done
