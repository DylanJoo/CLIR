import torch
from dataclasses import dataclass, field
from typing import Optional, Union, List, Dict, Tuple, Any
from transformers.tokenization_utils_base import PreTrainedTokenizerBase
from transformers.tokenization_utils_base import PaddingStrategy, PreTrainedTokenizerBase


@dataclass
class DataCollatorFormonoT5:
    tokenizer: PreTrainedTokenizerBase
    padding: Union[bool, str, PaddingStrategy] = True
    truncation: Union[bool, str] = True
    max_length: Optional[int] = None
    pad_to_multiple_of: Optional[int] = None
    return_tensors: str = "pt"
    padding: Union[bool, str] = True
    istrain: Union[bool] = False

    def __call__(self, features: List[Dict[str, Any]]) -> Dict[str, Any]:

        # input
        text_inputs = [f"Query: {batch['query']} Document: {batch['passage']} Relevant:" \
                for batch in features]
        inputs = self.tokenizer(
                text_inputs,
                max_length=self.max_length,
                truncation=True,
                padding=True,
                return_tensors=self.return_tensors
        )

        # qid-pid pairs 
        ids = [(batch['qid'], batch['pid']) for batch in features]

        # labeling (if training)
        if self.istrain:
            # labels
            targets = self.tokenizer(
                    [text['label'] for text in features],
                    truncation=True,
                    return_tensors=self.return_tensors
            ).input_ids
            inputs['labels'] = target

        return inputs, ids

@dataclass
class monoT5DataCollator:
    tokenizer: PreTrainedTokenizerBase
    padding: Union[bool, str, PaddingStrategy] = True
    truncation: Union[bool, str] = True
    max_length: Optional[int] = None
    pad_to_multiple_of: Optional[int] = None
    return_tensors: str = "pt"
    padding: Union[bool, str] = True

    def __call__(self, features: List[Dict[str, Any]]) -> Dict[str, Any]:

        batch_text = self.tokenizer(
            [v['text'] for v in features],
            padding=self.padding,
            truncation=self.truncation,
            max_length=self.max_length,
            pad_to_multiple_of=self.pad_to_multiple_of,
            return_tensors=self.return_tensors,
        )

        batch_id = [(v['qid'], v['docid']) for v in features]

        return batch_text, batch_id
