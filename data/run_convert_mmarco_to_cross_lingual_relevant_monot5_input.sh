# russian
if [ "$1" == "russian" ]
then
    python3 tools/convert_mmarco_psg_to_monot5.py \
      --lang russian \
      --output data/mmarco.train.clr.eng-rus.monot5.tsv \
      --cross-lingual-relevant
fi

# chincese
if [ "$1" == "chinese" ]
then
    python3 tools/convert_mmarco_psg_to_monot5.py \
      --lang chinese \
      --output data/mmarco.train.clr.eng-rus.monot5.tsv  \
      --cross-lingual-relevant
fi

# chincese russina persian
if [ "$1" = "all" ]
then
    python3 tools/convert_mmarco_psg_to_monot5.py \
      --lang chinese \
      --lang russian \
      --output data/mmarco.train.clr-eng-multi.monot5.tsv \
      --cross-lingual-relevant
fi
