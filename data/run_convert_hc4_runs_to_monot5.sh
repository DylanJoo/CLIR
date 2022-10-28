# dual query ranking
for lang in rus zho fas;do
    python3 tools/convert_runs_to_monot5.py \
      --run ../spr/runs/hc4.$lang.human.test.topics.spr.top1000.trec \
      --queries ../hc4/test.topics.v1-0.tsv \
      --corpus ../hc4/$lang/hc4_docs_c.jsonl \
      --output_text_pair hc4.$lang.human.test.topics.spr.top1000.dual_query.text_pair.txt \
      --output_id_pair hc4.$lang.human.test.topics.spr.top1000.dual_query.id_pair.txt \
      --lang $lang \
      --source human \
      --dual-lingual-ranking
done

# cross-lingual relevant finetunning
for lang in rus zho fas;do
    python3 tools/convert_runs_to_monot5.py \
      --run ../spr/runs/hc4.$lang.human.test.topics.spr.top1000.trec \
      --queries ../hc4/test.topics.v1-0.tsv \
      --corpus ../hc4/$lang/hc4_docs_c.jsonl \
      --output_text_pair hc4.$lang.original.test.topics.spr.top1000.cross-lingual.text_pair.txt \
      --output_id_pair hc4.$lang.original.test.topics.spr.top1000.cross-lingual.id_pair.txt \
      --lang eng \
      --source original
done

# stanrdard reranking
for lang in rus zho fas;do
    python3 tools/convert_runs_to_monot5.py \
      --run ../spr/runs/hc4.$lang.human.test.topics.spr.top1000.trec \
      --queries ../hc4/test.topics.v1-0.tsv \
      --corpus ../hc4/$lang/hc4_docs_c.jsonl \
      --output_text_pair hc4.$lang.human.test.topics.spr.top1000.text_pair.txt \
      --output_id_pair hc4.$lang.human.test.topics.spr.top1000.id_pair.txt \
      --lang $lang \
      --source human
done
