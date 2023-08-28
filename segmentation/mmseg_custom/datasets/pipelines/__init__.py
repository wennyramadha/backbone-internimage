# Wenny add compose, loading, test_time_aug
# ---------------------------------------------------------------------
# Copyright (c) OpenMMLab. All rights reserved.
from .formatting import DefaultFormatBundle, ToMask, ToTensor, Transpose, ToDataContainer, Collect, to_tensor
from .transform import (MapillaryHack, PadShortSide, SETR_Resize, CLAHE, AdjustGamma, Normalize, Pad,
                         PhotoMetricDistortion, RandomCrop, RandomFlip,
                         RandomRotate, Rerange, Resize, RGB2Gray, SegRescale)
from .compose import Compose
from .loading import LoadAnnotations, LoadImageFromFile

__all__ = [
    'DefaultFormatBundle', 'ToMask', 'ToTensor', 'Transpose', 'ToDataContainer', 'Collect', 'to_tensor',
    'SETR_Resize', 'PadShortSide', 'MapillaryHack', 'CLAHE', 'AdjustGamma', 'Normalize', 'Pad',
    'PhotoMetricDistortion', 'RandomCrop', 'RandomFlip', 'RandomRotate', 'Rerange', 'Resize', 'RGB2Gray',
    'SegRescale',
    'Compose',
    'LoadAnnotations', 'LoadImageFromFile',
]
