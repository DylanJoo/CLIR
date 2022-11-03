# Here we only considered the chinese and russian (since these two languages are overlapped in NeuCLIR dataset and mmarco)

python3 tools/convert_mmarco_psg_to_monot5.py \
  --lang chinese \
  --lang russian \
  --output data/mmarco.train.clr.monomt5.tsv \
  --cross-lingual-relevant
