import os
import json
import argparse


def get_source(string):
    if 'original' in string:
        return 'original'
    elif 'human' in string:
        return 'human'
    elif 'sockeye' in string:
        return 'sockeye'
    elif 'google translation' in string:
        return 'google'
                

def main(args):


    with open(args.topic, 'r') as f, open(args.output, 'w') as fout:

        for line in f:

            data = json.loads(line.strip())
            topic_id = data['topic_id']

            # Several translation within a topic (query)
            for i, example in enumerate(data['topics']):
                lang = example['lang']
                title = example['topic_title']
                desc = example['topic_description']
                src = get_source(example['source'])

                # filter empty
                if title == "" and desc == "":
                    pass
                    # print(f"Query title and descrption in {topic_id} {i} example are empty")
                else:
                    title = "no title" if title == "" else title
                    desc = "no description" if desc == "" else desc

                    fout.write(json.dumps({
                        "id": topic_id, "lang": lang, "src": src, "title": title, "desc": desc
                    }, ensure_ascii=False)+'\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--topic', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    main(args)
