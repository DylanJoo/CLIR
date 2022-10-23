PROJECT=trec-354700
ZONE=europe-west4-a
TPU=v3-8
MODEL_NAME=large
MODEL_DIR=gs://cfdaclip-tmp/cast/checkpoints/mt5-large-mmarco-v2-ch-en
TRAIN_FILE=gs://cfdaclip-tmp2/mmarco.train.dual-query/mmarco.train.chinese-english.monot5.tsv
PRETRAINED_STEPS=1000000
STEPS=1100000
PRETRAINED_DIR=gs://t5-data/pretrained_models/mt5/${MODEL_NAME}/model.ckpt-${PRETRAINED_STEPS}
TASK=mt5_xnli_zeroshot

# Run fine-tuning
python3 -m t5.models.mesh_transformer_main \
  --tpu="${TPU}" \
  --gcp_project="${PROJECT}" \
  --tpu_zone="${ZONE}" \
  --model_dir="${MODEL_DIR}" \
  --gin_param="utils.run.init_checkpoint = '${PRETRAINED_DIR}'" \
  --gin_file="dataset.gin" \
  --gin_file="gs://t5-data/pretrained_models/${MODEL_NAME}/operative_config.gin" \
  --gin_param="utils.tpu_mesh_shape.model_parallelism = 2" \
  --gin_param="MIXTURE_NAME = '${TASK}'" \
  --gin_param="utils.tpu_mesh_shape.tpu_topology = '${TPU}'" \
  --gin_param="utils.run.train_dataset_fn = @t5.models.mesh_transformer.tsv_dataset_fn" \
  --gin_param="tsv_dataset_fn.filename = '${TRAIN_FILE}'" \
  --gin_param="utils.run.sequence_length = {'inputs': 512, 'targets': 4}" \
  --gin_file="learning_rate_schedules/constant_0_001.gin" \
  --gin_param="utils.run.train_steps = ${STEPS}" \
  --gin_param="utils.run.save_checkpoints_steps = 10000" \
  --module_import="multilingual_t5.tasks" \
  --gin_param="utils.run.batch_size=('tokens_per_batch', 65536)" \
  --gin_location_prefix="multilingual_t5/gin/"


# seqio
# sentencepiece model
