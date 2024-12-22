# tinyCLAP: Distilling Contrastive Language-Audio Pretrained models

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-blue)](https://huggingface.co/fpaissan/tinyCLAP) [![arXiv](https://img.shields.io/badge/10.21437%2FInterspeech.2024-red?label=paper-pdf)](https://www.isca-archive.org/interspeech_2024/paissan24_interspeech.pdf) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/fpaissan/tinyCLAP/blob/main/LICENSE)

This repository contains the ~~official~~ modified implementation of [tinyCLAP](https://www.isca-archive.org/interspeech_2024/paissan24_interspeech.html).

![tinyCLAP overview](https://francescopaissan.it/tinyclapweb/assets/overview.png)

## Requirements

First of all, let's clone the repo and install the requirements:


> [!WARNING]  
> Ensure rustc (the rust compiler) is installed as it is needed for other dependencies.

for macos
```zsh
brew install rust
```

for ubuntu
```bash
apt install rust
```
then download the repo and move into it

```setup
git clone https://github.com/martinhofigueiredo/tinyCLAP & cd tinyCLAP
pip install -r extra_requirements.txt
```

## Evaluation

The command to evaluate the model on each dataset varies slightly among datasets.
Below are listed all the necessary commands.

### ESC50

```bash
python tinyclap.py hparams/distill_clap.yaml --experiment_name tinyCLAP_$MODEL_NAME --zs_eval True --esc_folder $PATH_TO_ESC
```

### UrbanSound8K

```bash
python tinyclap.py hparams/distill_clap.yaml --experiment_name tinyCLAP_$MODEL_NAME --zs_eval True --us8k_folder $PATH_TO_US8K
```

### TUT17

```bash
python tinyclap.py hparams/distill_clap.yaml --experiment_name tinyCLAP_$MODEL_NAME --zs_eval True --tut17_folder $PATH_TO_TUT17
```

## Pre-trained Models

You can download pretrained models from the [tinyCLAP HF](https://huggingface.co/fpaissan/tinyCLAP).

_Note_:  The checkpoints contain only the student model, so the text encoder will be downloaded separately.

`models` folder contains `Cnn14.ckpt` and `phinet_alpha_1.50_beta_0.75_t0_6_N_7.ckpt` which were available on the huggingface site (its also on the `getmodels.sh` script.



To run inference using the pretrained models, use:

```bash


python tinyclap.py hparams/distill_clap.yaml --pretrained_clap fpaissan/tinyCLAP/$MODEL_NAME.ckpt --zs_eval True --esc_folder $PATH_TO_ESC

```

This command will automatically download the checkpoint if present in the zoo of pretrained models. Make sure to change the dataset configuration file based on the evaluation.
Please refer to the HF repo for a list of available tinyCLAP models.

## Citing tinyCLAP

```
@inproceedings{paissan24_interspeech,
  title     = {tinyCLAP: Distilling Constrastive Language-Audio Pretrained Models},
  author    = {Francesco Paissan and Elisabetta Farella},
  year      = {2024},
  booktitle = {Interspeech 2024},
  pages     = {1685--1689},
  doi       = {10.21437/Interspeech.2024-193},
  issn      = {2958-1796},
}
```

## License

To promote reproducibility and follow-up research on the topic, we release all code and pretrained weights publicly (Apache 2.0 License).
Please be mindful that the Microsoft CLAP weights are released under a different license, the [MS-Public License](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/ms-pl.md). This can impact the license of the BERT weights that are used during inference (automatically downloaded from our code).
