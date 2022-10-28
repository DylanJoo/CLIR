from datasets import load_dataset

dataset_en = load_dataset("unicamp-dl/mmarco", cache_dir='/tmp2/jhju/hf_datasets')
dataset_ch = load_dataset("unicamp-dl/mmarco", "chinese", cache_dir='/tmp2/jhju/hf_datasets')
dataset_ru = load_dataset("unicamp-dl/mmarco", "russian", cache_dir='/tmp2/jhju/hf_datasets')

print(dataset_en)
print(dataset_ch)
print(dataset_ru)

print(dataset_en['train'][7777])
print(dataset_ch['train'][7777])
print(dataset_ru['train'][7777])
