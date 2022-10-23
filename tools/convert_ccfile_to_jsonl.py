import re
import json
import os
import argparse

def convert_cc_collection(args):
    output_jsonl_file = open(args.output_path, 'w')

    print('Converting collection...')
    with open(args.collection_path, encoding='utf-8') as f:
        for i, line in enumerate(f):
            doc_dict = json.loads(line.strip())

            # components in a dict
            doc_id = doc_dict['id']
            doc_title = re.sub('\s+', ' ', doc_dict['title'])
            doc_content = re.sub('\s+', ' ', doc_dict['text'])
            
            if args.title_append:
                doc_text = f"{doc_title} {doc_content}"
            # title append
            else: 
                doc_text = doc_content

            output_dict = {'id': doc_id, 'contents': doc_text}
            output_jsonl_file.write(json.dumps(output_dict, ensure_ascii=False) + '\n')

            if i % 100000 == 0:
                print(f'Converted {i:,} docs, writing into file {args.output_path}')

    output_jsonl_file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert CC files jsonl to pyserini's format")
    parser.add_argument('--collection-path', required=True,)
    parser.add_argument('--output-path', type=str)
    parser.add_argument('--title-append', action='store_true', default=False)

    args = parser.parse_args()

    convert_cc_collection(args)
    print('Done!')
