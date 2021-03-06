![alt text](icons/character+fat+game+hero+inkcontober+movie+icon-1320183878106104615_24.png) SABER - Semi-Supervised Audio Baseline for Easy Reproduction
=====
A PyTorch project currently under research can provide easily reproducible baselines for automatic speech recognition using semi-supervised learning.
Contributions are welcome.

## Overview
SABER consists of the following components

* Several SOTA models including an Mixnet based variant of QuartzNet by NVIDIA.
* Ranger (RAdam + Lookahead) optimizer to offset warmup used by SpecAugment (by Leslie Smith)
* Mish activation function
* Data Augmentions used are SpecNoise, SpecAugment, SpecSparkle a cutout inspired variant, SpecBlur (a novel approach). Augmentation parameters linearly increase in a curriculum based approach.
* Aggregated Cross Entropy loss instead of CTC loss for easier training
* Unsupervised Data Augmentation as means for Semi-Supervised Learning

## Requirements

* ariar2c
* python3.x
* libraries in requirements.txt

## Download & Setup

Librispeech & CommonVoice datasets using download scripts, change dir parameter as per your configuration
```
sh download_scripts/download_librispeech.sh
sh download_scripts/extract_librispeech_tars.sh
sh download_scripts/download_common_voice.sh
sh download_scripts/extract_common_voice_tars.sh
```

Setup sentencepeiece vocab & form LMDB dataset.
```
sh dataset_scripts/librispeech_all_lines.sh
sh dataset_scripts/librispeech_sentencepiece_model.sh
OMP_NUM_THREADS="1" OPENBLAS_NUM_THREADS="1" python3 -W ignore -m dataset_scripts.create_librispeech_lmdb
OMP_NUM_THREADS="1" OPENBLAS_NUM_THREADS="1" python3 -W ignore -m dataset_scripts.create_commonvoice_lmdb
OMP_NUM_THREADS="1" OPENBLAS_NUM_THREADS="1" python3 -W ignore -m dataset_scripts.create_airtel_lmdb
OMP_NUM_THREADS="1" OPENBLAS_NUM_THREADS="1" python3 -W ignore -m dataset_scripts.create_airtelpayments_lmdb
```

## Training
Modify `utils/config.py` as per your configuration and run
```
OMP_NUM_THREADS="1" CUDA_VISIBLE_DEVICES="0,1,2" python3.6 train.py
```


References
==========

## Papers

[Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](https://arxiv.org/abs/1512.02595)

[Jasper: An End-to-End Convolutional Neural Acoustic Model](https://arxiv.org/abs/1904.03288)

[SpecAugment: A Simple Data Augmentation Method for Automatic Speech Recognition](https://arxiv.org/pdf/1904.08779.pdf)

[Improved Regularization of Convolutional Neural Networks with Cutout](https://arxiv.org/abs/1708.04552)

[On the Variance of the Adaptive Learning Rate and Beyond](https://arxiv.org/abs/1908.03265)

[Aggregation Cross-Entropy for Sequence Recognition](https://arxiv.org/abs/1904.08364)

[MixMatch: A Holistic Approach to Semi-Supervised Learning](https://arxiv.org/abs/1905.02249)

[MixConv: Mixed Depthwise Convolutional Kernels](https://arxiv.org/abs/1907.09595)

[Unsupervised Data Augmentation for Consistency Training](https://arxiv.org/abs/1904.12848)

[Cyclical Learning Rates for Training Neural Networks](https://arxiv.org/pdf/1506.01186.pdf)

[Cycle-consistency training for end-to-end speech recognition](https://arxiv.org/abs/1811.01690)

[RandAugment: Practical data augmentation with no separate search](https://arxiv.org/abs/1909.13719)

[Self-Attention Networks For Connectionist Temporal Classification in Speech Recognition](https://arxiv.org/pdf/1901.10055.pdf)

## Codebases

[DeepSpeech2](https://github.com/PaddlePaddle/DeepSpeech)

[NVIDIA Neural Modules: NeMo](https://github.com/NVIDIA/NeMo)

[RAdam](https://github.com/LiyuanLucasLiu/RAdam)

[LR-Finder](https://github.com/davidtvs/pytorch-lr-finder)

[Cyclical Learning Rate Scheduler With Decay in Pytorch](https://github.com/bluesky314/Cyclical_LR_Scheduler_With_Decay_Pytorch)

[MixNet](https://github.com/romulus0914/MixNet-Pytorch)