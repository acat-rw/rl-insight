#!/usr/bin/env bash

set -euo pipefail

NVTX_PROFILER_DATA_PATH="${NVTX_PROFILER_DATA_PATH:-}"
OUTPUT_PATH="${OUTPUT_PATH:-./output}"
VIS_TYPE="${VIS_TYPE:-html}"
RANK_LIST="${RANK_LIST:-all}"

echo "=========================================="
echo "Nvtx Profiler Cluster Analysis"
echo "=========================================="
echo "Input Path:    ${NVTX_PROFILER_DATA_PATH}"
echo "Output Path:   ${OUTPUT_PATH}"
echo "Vis Type:      ${VIS_TYPE}"
echo "Rank List:     ${RANK_LIST}"
echo "=========================================="

python -m rl_insight.main \
    input.input_path="${NVTX_PROFILER_DATA_PATH}" \
    input.profiler_type=nvtx \
    input.input_type=multi_json_nvtx \
    input.rank_list="${RANK_LIST}" \
    output.output_path="${OUTPUT_PATH}" \
    timeline.visualizer.vis_type="${VIS_TYPE}" 

echo "=========================================="
echo ">>> Analysis completed successfully!"
echo ">>> Output saved to: ${OUTPUT_PATH}"
echo "=========================================="
