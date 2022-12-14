# hc4
for split in test;do
    echo '# HC4' ${split}
    echo '| Language | Source | Ranking |   R@100 | R@1K | nDCG@20 | mAP@20  | mAP@100 | mAP@1K |'
    echo '|----------|--------|---------|---------|------|---------|---------|---------|--------|'
    for lang in fas rus zho;do
        for source in human;do
            # monomt5 
            FILE=runs/hc4.${lang}.${source}.${split}.topics.spr.top1000.monomt5.large.trec
            echo  $lang '|' $source '| monomt5 |' 
            ./tools/trec_eval-9.0.7/trec_eval \
                -m ndcg_cut.20 \
                -m map_cut.20,100,1000 \
                -m recall.100,1000 \
                data/hc4/${lang}/${split}.qrels.v1-0.txt $FILE | cut -f3 | sed ':a; N; $!ba; s/\n/|/g'

            # monomt5 - dq
            FILE=runs/hc4.${lang}.${source}.${split}.topics.spr.top1000.monomt5.dq.trec
            echo  $lang '|' $source '| monomt5-dq |' 
            ./tools/trec_eval-9.0.7/trec_eval \
                -m ndcg_cut.20 \
                -m map_cut.20,100,1000 \
                -m recall.100,1000 \
                data/hc4/${lang}/${split}.qrels.v1-0.txt $FILE | cut -f3 | sed ':a; N; $!ba; s/\n/|/g'
            # monomt5 - clr
            FILE=runs/hc4.${lang}.${source}.${split}.topics.spr.top1000.monomt5.clr.trec
            echo  $lang '|' $source '| monomt5-clr |' 
            ./tools/trec_eval-9.0.7/trec_eval \
                -m ndcg_cut.20 \
                -m map_cut.20,100,1000 \
                -m recall.100,1000 \
                data/hc4/${lang}/${split}.qrels.v1-0.txt $FILE | cut -f3 | sed ':a; N; $!ba; s/\n/|/g'
        done
    done
    echo -e
done
