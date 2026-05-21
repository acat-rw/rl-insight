# Copyright (c) 2025 verl-project authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass, field
from typing import Optional

from omegaconf import MISSING


@dataclass
class InputConfig:
    """Input data configuration."""

    input_path: str = MISSING  # Path to profiling data (required)
    input_type: str = "multi_json_mstx"  # multi_json_mstx | multi_json_torch | multi_json_nvtx | gmm_data
    profiler_type: str = "mstx"  # mstx | torch | nvtx | gmm
    rank_list: str = "all"  # Rank id list, e.g. '0,1,2' or 'all'


@dataclass
class OutputConfig:
    """Output configuration."""

    output_path: str = "output"  # Output directory path


@dataclass
class TimelineParserConfig:
    """Timeline parser filter configuration."""


@dataclass
class TimelineVisualizerConfig:
    """Timeline visualizer configuration."""

    vis_type: str = "html"  # html | png
    width: int = 2000  # Image width in pixels (png only)
    scale: int = 2  # Image scale factor (png only)


@dataclass
class TimelineConfig:
    """Timeline configuration."""

    parser: TimelineParserConfig = field(default_factory=TimelineParserConfig)
    visualizer: TimelineVisualizerConfig = field(
        default_factory=TimelineVisualizerConfig
    )


@dataclass
class GmmParserConfig:
    """GMM parser filter configuration."""

    step: Optional[str] = None  # Step filter, e.g. '1' or '1,2'
    role: Optional[str] = None  # Role filter


@dataclass
class GmmVisualizerConfig:
    """GMM heatmap visualizer configuration."""

    vis_type: str = "gmm_heatmap"  # gmm_heatmap
    dpi: int = 200  # DPI for heatmap PNG output
    cmap: str = "viridis"  # Matplotlib colormap name
    gmm_per_layer: int = 3  # Grouped matmul count per MoE layer


@dataclass
class GmmConfig:
    """GMM configuration."""

    parser: GmmParserConfig = field(default_factory=GmmParserConfig)
    visualizer: GmmVisualizerConfig = field(default_factory=GmmVisualizerConfig)


@dataclass
class PipelineConfig:
    """Pipeline configuration."""

    pipeline_type: str = "OfflineInsightPipeline"  # OfflineInsightPipeline


@dataclass
class AppConfig:
    """RL Insight configuration."""

    pipeline: PipelineConfig = field(default_factory=PipelineConfig)
    input: InputConfig = field(default_factory=InputConfig)
    output: OutputConfig = field(default_factory=OutputConfig)
    timeline: TimelineConfig = field(default_factory=TimelineConfig)
    gmm: GmmConfig = field(default_factory=GmmConfig)
