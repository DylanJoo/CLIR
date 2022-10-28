# # stanrard
for lang in rus zho fas;do
    ID_FILE=monoMT5-pairs/hc4.${lang}.human.test.topics.spr.top1000.id_pair.txt
    TEXT_FILE=monoMT5-pairs/hc4.${lang}.human.test.topics.spr.top1000.text_pair.txt
    OUT_FILE=monoMT5-pairs/hc4.${lang}.human.test.topics.spr.top1000.monomt5.base.trec
    python3 rerank.py \
      --id_pair $ID_FILE \
      --text_pair $TEXT_FILE \
      --output_trec $OUT_FILE \
      --model_name_or_path unicamp-dl/mt5-base-mmarco-v2 \
      --batch_size 4 \
      --gpu 1
done

# stanrard

# for lang in rus zho fas;do
for lang in rus zho fas;do
    ID_FILE=monoMT5-pairs/hc4.${lang}.human.test.topics.spr.top1000.id_pair.txt
    TEXT_FILE=monoMT5-pairs/hc4.${lang}.human.test.topics.spr.top1000.text_pair.txt
    OUT_FILE=runs/hc4.${lang}.human.test.topics.spr.top1000.monomt5.large.trec
    python3 rerank.py \
      --id_pair $ID_FILE \
      --text_pair $TEXT_FILE \
      --output_trec $OUT_FILE \
      --model_name_or_path checkpoints/mt5-large-mmarco-v2 \
      --batch_size 2 \
      --gpu 0
done

# clr
for lang in rus zho fas;do
    ID_FILE=monoMT5-pairs/hc4.${lang}.original.test.topics.spr.top1000.cross-lingual.id_pair.txt
    TEXT_FILE=monoMT5-pairs/hc4.${lang}.original.test.topics.spr.top1000.cross-lingual.text_pair.txt
    OUT_FILE=runs/hc4.${lang}.human.test.topics.spr.top1000.monomt5.clf.trec
    python3 rerank.py \
      --id_pair $ID_FILE \
      --text_pair $TEXT_FILE \
      --output_trec $OUT_FILE \
      --model_name_or_path checkpoints/mt5-large-mmarco-v2-clr \
      --batch_size 2 \ 
      --gpu 0
done

# dq
for lang in rus zho fas;do
    ID_FILE=monoMT5-pairs/hc4.${lang}.original.test.topics.spr.top1000.dual_query.id_pair.txt
    TEXT_FILE=monoMT5-pairs/hc4.${lang}.original.test.topics.spr.top1000.dual_query.text_pair.txt
    OUT_FILE=runs/hc4.${lang}.human.test.topics.spr.top1000.monomt5.dq.trec
    python3 rerank.py \
      --id_pair $ID_FILE \
      --text_pair $TEXT_FILE \
      --output_trec $OUT_FILE \
      --model_name_or_path checkpoints/mt5-large-mmarco-v2-dual \
      --batch_size 2 \ 
      --gpu 0
done
