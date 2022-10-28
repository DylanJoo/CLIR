import collections
import json

def load_queries(path, lang='eng', source='original'):

    queries_dict = {}
    with open(path, 'r') as f:
        for i, line in enumerate(f):
            try:
                qid, query = line.rstrip().split('\t')
                qid, qlang, qsource = qid.split('#')

                if qlang == lang and qsource == source:
                    queries_dict[qid] = query

            except:
                print("Invalid query (or tab within query)")
        
            if i % 10000 == 0:
                print('Loading queries...{}'.format(i))

    print('Loading queries...{}'.format(len(queries_dict)))

    return queries_dict

def load_collections(path=None, dir=None,):
    collection_dict = collections.defaultdict(str)

    if dir: # load if there are many jsonl files
        files = [os.path.join(dir, f) for f in os.listdir(dir) if ".json" in f]
    else:
        files = [path]

    for file in files:
        print(f"Loading from collection {file}...")
        with open(file, 'r') as f:
            for i, line in enumerate(f):
                example = json.loads(line.strip())
                collection_dict[example['id']] = example['contents'].strip()

                if i % 1000000 == 1:
                    print(f" # documents...{i}")

    print("DONE")
    return collection_dict

def load_runs(path, topk):
    candidate_docs = set()
    run = collections.OrderedDict()
    with open(path) as f:
        for i, line in enumerate(f):
            qid, _, docid, rank, _, _ = line.split(' ')
            if int(rank) <= topk:
                # log the candidate docs 
                candidate_docs.add(docid)
                if qid not in run:
                    run[qid] = []
                run[qid].append((docid, int(rank)))

    print('Sorting candidate docs by rank...')
    sorted_run = collections.OrderedDict()
    for i, (qid, doc_ids_ranks) in enumerate(run.items()):
        doc_ids_ranks = sorted(doc_ids_ranks, key=lambda x: x[1])
        docids = [docid for docid, _ in doc_ids_ranks]
        sorted_run[qid] = docids

    print('Loading run...{}'.format(i))
    print("================\nOverlapped Document in this run under top-{}: {}\n================".format(
        topk, len(candidate_docs)))
    return sorted_run, candidate_docs

def normalized(strings, strings_title="No Title"):
    if strings_title != "No Title":
        strings = strings_title + " " + strings 
    strings = re.sub(r"\n", " ", strings)
    # strings = re.sub(r"\s{2, }", " ", strings)
    return strings.strip()
