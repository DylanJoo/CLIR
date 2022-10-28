## Requirements

1. Setup TPU and GCP VM
```
tensorflow==2.3.0
tensorflow-text==2.3.0
sentencepiece==0.1.96
mesh_tensorflow==0.1.21
gin-config==0.5.0
```

2. Change type of multilingual-t5 repo
```
mv multilingual-t5/multilingual-t5 multilingual_t5
```

3. Find the target tokens (with sentencepiece model)
```
import sentencepiece as spm
# path: gs://t5-data/vocabs/mc4.250000.100extra/sentencepiece.model
s = spm.SentencePieceProcessor(model_file='spm.model')
s.encode('yes no')
>>> [36339, 375]
```
