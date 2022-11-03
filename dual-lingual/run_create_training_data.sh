python3 tools/convert_mmarco_psg_to_monot5.py \
    --lang chinese --lang russian \
    --output dual-lingual/dual-mmarco.train.dq.tsv \
    --dq

python3 tools/convert_mmarco_psg_to_monot5.py \
    --lang chinese --lang russian \
    --output cross-lingual-finetuning/mmarco.train.clf.tsv \
    --clf
