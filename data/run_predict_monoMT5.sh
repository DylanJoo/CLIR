for ITER in {00..23}; do
  echo "Running iter: $ITER" >> process-t5m.out
  nohup t5_mesh_transformer \
    --tpu="${YOUR TPU}" \
    --gcp_project="${PRJ_NAME}" \
    --tpu_zone="europe-west4-a" \
    --model_dir="gs://${MODEL_DIR}" \
    --gin_file="gs://t5-data/pretrained_models/${MODEL_SIZE}/operative_config.gin" \
    --gin_file="infer.gin" \
    --gin_file="score_from_file.gin" \
    --gin_param="utils.tpu_mesh_shape.tpu_topology = 'v3-8'" \
    --gin_param="infer_checkpoint_step = ${CKPT}" \
    --gin_param="utils.run.sequence_length = {'inputs': 512, 'targets': 4}" \
    --gin_param="Bitransformer.decode.max_decode_length = 2" \
    --gin_param="inputs_filename = 'gs://${INPUT_FILE}'" \
    --gin_param="targets_filename = 'gs://${TARGET_FILE}'" \
    --gin_param="scores_filename = 'gs://${OUTPUT_FILE}'" \
    --gin_param="Bitransformer.decode.beam_size = 1" \
    --gin_param="Bitransformer.decode.temperature = 0.0" \
    --gin_param="Unitransformer.sample_autoregressive.sampling_keep_top_k = -1" 
