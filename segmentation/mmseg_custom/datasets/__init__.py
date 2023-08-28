# Wenny add cityscapes and gta dataset
# -------------------------------------------------------------------
# Copyright (c) OpenMMLab. All rights reserved.

from .builder import DATASETS, PIPELINES, build_dataloader, build_dataset
from .custom import CustomDataset
from .mapillary import MapillaryDataset  # noqa: F401,F403
from .nyu_depth_v2 import NYUDepthV2Dataset  # noqa: F401,F403
from .pipelines import *  # noqa: F401,F403
from .dataset_wrappers import ConcatDataset
from .cityscapes import CityscapesDataset
from .gta import GTADataset


__all__ = [
    'CustomDataset',
    'build_dataloader',
    'build_dataset',
    'DATASETS',
    'PIPELINES',
    'MapillaryDataset',
    'NYUDepthV2Dataset',
    'ConcatDataset',
    'CityscapesDataset',
    'GTADataset',
]