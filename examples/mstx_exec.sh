#!/usr/bin/env bash

set -euo pipefail

MSTX_PROFILER_DATA_PATH="${MSTX_PROFILER_DATA_PATH:-}"
OUTPUT_PATH="${OUTPUT_PATH:-./output}"
VIS_TYPE="${VIS_TYPE:-html}"
RANK_LIST="${RANK_LIST:-all}"

echo "=========================================="
echo "MSTX Profiler Cluster Analysis"
echo "=========================================="
echo "Input Path:    ${MSTX_PROFILER_DATA_PATH}"
echo "Output Path:   ${OUTPUT_PATH}"
echo "Vis Type:      ${VIS_TYPE}"
echo "Rank List:     ${RANK_LIST}"
echo "=========================================="

# Preprocessing is optional: comment out below code if data is already preprocessed

echo ">>> Start mstx data preprocessing..."

python -m rl_insight.utils.mstx_preprocessing "${MSTX_PROFILER_DATA_PATH}"

echo ">>> Mstx data preprocessing completed."

python -m rl_insight.main \
    input.input_path="${MSTX_PROFILER_DATA_PATH}" \
    input.profiler_type=mstx \
    input.input_type=multi_json_mstx \
    input.rank_list="${RANK_LIST}" 
    output.output_path="${OUTPUT_PATH}" \
    timeline.visualizer.vis_type="${VIS_TYPE}"

echo "=========================================="
echo ">>> Analysis completed successfully!"
echo ">>> Output saved to: ${OUTPUT_PATH}"
echo "=========================================="
