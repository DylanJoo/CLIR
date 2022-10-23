# baseline reranking model unicamp-dl/mt5-base-mmarco-v2
for split in dev test;do
    for lang in fas rus zho;do
        for src in human;do
            python3 passage_reranking.py \
              --run runs/${lang}/hc4.${lang}.${split}.${src}.td.spr.top1000.trec \
              --topic data/hc4/${split}.jsonl \
              --collection /tmp2/trec/hc4/${lang}/hc4_docs_tc.jsonl \
              --topk 1000 \
              --output_trec runs/${lang}/hc4.${lang}.${split}.${src}.monoT5.trec \
              --model_name_or_path unicamp-dl/mt5-base-mmarco-v2 \
              --batch_size 4 \
              --max_length 512 \
              --gpu 2 \
              --prefix monomt5-base \
              --lang ${lang} \
              --src ${src}
        done
    done
done
