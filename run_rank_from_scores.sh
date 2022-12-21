# dq
for split in dev test;do
    for lang in zho rus fas;do
        python3 tools/rank_with_scores.py \
            --run runs/${lang}/hc4.${lang}.${split}.human.td.spr.top1000.trec \
            --scores dual-lingual/scores/infer_hc4_${lang}_${split}_dq-score.jsonl-00000-of-00001 \
            --output runs/${lang}/hc4.${lang}.${split}.human.monomT5.dq.trec \
            --prefix monomt5-dq
    done
done

# clr
for split in dev test;do
    for lang in zho rus fas;do
        python3 tools/rank_with_scores.py \
            --run runs/${lang}/hc4.${lang}.${split}.human.td.spr.top1000.trec \
            --scores cross-lingual-finetuning/scores/infer_hc4_${lang}_${split}_clr-score.jsonl-00000-of-00001 \
            --output runs/${lang}/hc4.${lang}.${split}.human.monomT5.clr.trec
    done
done
