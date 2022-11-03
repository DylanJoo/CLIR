# baseline reranking model unicamp-dl/mt5-base-mmarco-v2
for split in test dev;do
    for lang in fas rus zho;do
        for src in human;do
            python3 passage_reranking.py \
              --run runs/${lang}/hc4.${lang}.${split}.${src}.td.spr.top1000.trec \
              --topic data/hc4/${split}.jsonl \
              --collection /tmp2/trec/hc4/${lang}/hc4_docs_tc.jsonl \
              --topk 1000 \
              --output_trec runs/${lang}/hc4.${lang}.${split}.${src}.monomT5L-dq.trec \
              --output_trec runs/cast20.canard.train.rewrite.rerank.top1000.trec \
              --model_name_or_path checkpoints/mt5-large-mmarco-v2-dq \
              --batch_size 4 \
              --max_length 512 \
              --gpu 1 \
              --prefix monomt5-L-dq \
              --lang ${lang} \
              --src ${src}
        done
    done
done
              # --model_name_or_path unicamp-dl/mt5-base-mmarco-v2 \
              # --model_name_or_path DylanJHJ/mt5-large-mmarco-v2-dq \
