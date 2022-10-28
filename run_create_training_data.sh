python3 tools/convert_mmarco_psg_to_monot5.py \
    --lang chinese --lang russian \
    --output mmarco.train.dq.tsv \
    --dq

python3 tools/convert_mmarco_psg_to_monot5.py \
    --lang chinese --lang russian \
    --output mmarco.train.clf.tsv \
    --clf
