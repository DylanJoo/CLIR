# rus and gas
for lang in zho fas rus;do
    # clr
    # ID_FILE=monoMT5-pairs/hc4.${lang}.human.test.topics.spr.top1000.cross-lingual.id_pair.txt
    # TEXT_FILE=monoMT5-pairs/hc4.${lang}.human.test.topics.spr.top1000.cross-lingual.text_pair.txt
    # OUT_FILE=runs/hc4.${lang}.human.test.topics.spr.top1000.monomt5.clr.trec
    #
    # python3 rerank.py \
    #   --id_pair $ID_FILE --text_pair $TEXT_FILE --output_trec $OUT_FILE \
    #   --model_name_or_path checkpoints/mt5-large-mmarco-v2-clr \
    #   --batch_size 2 --gpu 2

    # standard
    ID_FILE=monoMT5-pairs/hc4.${lang}.human.test.topics.spr.top1000.id_pair.txt
    TEXT_FILE=monoMT5-pairs/hc4.${lang}.human.test.topics.spr.top1000.text_pair.txt
    OUT_FILE=runs/hc4.${lang}.human.test.topics.spr.top1000.monomt5.large.trec

    python3 rerank.py \
      --id_pair $ID_FILE --text_pair $TEXT_FILE --output_trec $OUT_FILE \
      --model_name_or_path checkpoints/mt5-large-mmarco-v2 \
      --batch_size 3 --gpu 0

    # dual query
    ID_FILE=monoMT5-pairs/hc4.${lang}.human.test.topics.spr.top1000.dual_query.id_pair.txt
    TEXT_FILE=monoMT5-pairs/hc4.${lang}.human.test.topics.spr.top1000.dual_query.text_pair.txt
    OUT_FILE=runs/hc4.${lang}.human.test.topics.spr.top1000.monomt5.dq.trec

    python3 rerank.py \
      --id_pair $ID_FILE --text_pair $TEXT_FILE --output_trec $OUT_FILE \
      --model_name_or_path checkpoints/mt5-large-mmarco-v2-dual\
      --batch_size 3 --gpu 0
done
