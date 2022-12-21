import torch
from dataclasses import dataclass, field
from typing import Optional, Union, List, Dict, Tuple, Any
from transformers.tokenization_utils_base import PreTrainedTokenizerBase
from transformers.tokenization_utils_base import PaddingStrategy, PreTrainedTokenizerBase


@dataclass
class DataCollatorFormonoT5:
    tokenizer: Union[PreTrainedTokenizerBase] = None
    padding: Union[bool, str, PaddingStrategy] = True
    truncation: Union[bool, str] = True
    max_length: Optional[int] = None
    pad_to_multiple_of: Optional[int] = None
    return_tensors: str = "pt"
    padding: Union[bool, str] = True
    # spec
    istrain: Union[bool] = False
    return_text: Union[bool] = False
    # CLIR
    dq: Union[bool] = False
    clr: Union[bool] = False
    """
    [TODO] Make the datacollator to support textline datasource for tpu. 
    (refer 'run_create_training_data.sh'
    """

    def __call__(self, features: List[Dict[str, Any]]) -> Dict[str, Any]:

        # input
        if self.dq:
            text_inputs = [
                    f"Query: {batch['query_en']} Query Translation: {batch['query']} Document: {batch['passage']} Relevant:" for batch in features
            ]
        elif self.clr:
            text_inputs = [
                    f"Query: {batch['query_en']} Document: {batch['passage']} Relevant:" \
                    for batch in features
            ]
        else:
            text_inputs = [
                    f"Query: {batch['query']} Document: {batch['passage']} Relevant:" \
                    for batch in features
            ]

        # qid-pid pairs 
        ids = [(batch['qid'], batch['pid']) for batch in features]


        if self.return_text:
            return text_inputs, ids
        else:
            inputs = self.tokenizer(
                    text_inputs,
                    max_length=self.max_length,
                    truncation=True,
                    padding=True,
                    return_tensors=self.return_tensors
            )

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

