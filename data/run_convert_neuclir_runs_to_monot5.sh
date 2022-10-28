# cross-lingual relevant finetunning
for lang in fas zho rus;do
    for source in google nllb;do
        if [ -s ../spr/neuclir_runs/neuclir.$lang.$source.eval.topics.spr.rm3.top1000.trec ];then
            python3 tools/convert_runs_to_monot5.py \
              --run ../spr/neuclir_runs/neuclir.$lang.$source.eval.topics.spr.rm3.top1000.trec \
              --queries ../data/neuclir_topics/all_lang_source.tsv \
              --corpus ../data/$lang/docs_c.jsonl \
              --output_text_pair monoMT5-pairs/neuclir.$lang.$source.eval.topics.spr.rm3.top1000.cross-lingual.text_pair.txt \
              --output_id_pair monoMT5-pairs/neuclir.$lang.$source.eval.topics.spr.rm3.top1000.cross-lingual.id_pair.txt \
              --lang eng \
              --source original
        fi
    done
done




# # dual query ranking
# for lang in fas zho rus;do
#     for source in google nllb;do
#         if [ -s ../spr/neuclir_runs/neuclir.$lang.$source.eval.topics.spr.rm3.top1000.trec ];then
#             python3 tools/convert_runs_to_monot5.py \
#               --run ../spr/neuclir_runs/neuclir.$lang.$source.eval.topics.spr.rm3.top1000.trec \
#               --queries ../data/neuclir_topics/all_lang_source.tsv \
#               --corpus ../data/$lang/docs_c.jsonl \
#               --output_text_pair monoMT5-pairs/neuclir.$lang.$source.eval.topics.spr.rm3.top1000.dual_query.text_pair.txt \
#               --output_id_pair monoMT5-pairs/neuclir.$lang.$source.eval.topics.spr.rm3.top1000.dual_query.id_pair.txt \
#               --lang $lang \
#               --source $source \
#               --dual-lingual-ranking
#         fi
#     done
# done
#
# # stanrdard reranking
# for lang in rus zho fas;do
#     for source in nllb google;do
#         if [ -s ../spr/neuclir_runs/neuclir.$lang.$source.eval.topics.spr.rm3.top1000.trec ];then
#             python3 tools/convert_runs_to_monot5.py \
#               --run ../spr/neuclir_runs/neuclir.$lang.$source.eval.topics.spr.rm3.top1000.trec \
#               --queries ../data/neuclir_topics/all_lang_source.tsv \
#               --corpus ../data/$lang/docs_c.jsonl \
#               --output_text_pair monoMT5-pairs/neuclir.$lang.$source.eval.topics.spr.rm3.top1000.text_pair.txt \
#               --output_id_pair monoMT5-pairs/neuclir.$lang.$source.eval.topics.spr.rm3.top1000.id_pair.txt \
#               --lang $lang \
#               --source $source
#         fi
#     done
# done
