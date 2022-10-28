# russian
if [ "$1" == "russian" ]
then
    python3 tools/convert_mmarco_psg_to_monot5.py \
      --lang russian \
      --output data/mmarco.train.russian-english.monot5.tsv \
      --dual-lingual-ranking
fi

# chincese
if [ "$1" == "chinese" ]
then
    python3 tools/convert_mmarco_psg_to_monot5.py \
      --lang chinese \
      --output data/mmarco.train.chinese-english.monot5.tsv \
      --cross-lingual-ranking
fi

# chincese russina persian
if [ "$1" = "all" ]
then
    python3 tools/convert_mmarco_psg_to_monot5.py \
      --lang chinese \
      --lang russian \
      --output data/mmarco.train.dual.lang.monot5.tsv  \
      --cross-lingual-ranking
fi
