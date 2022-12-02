#!/bin/bash

python train.py hparams/train.yaml \
                --device 'cuda:6' \
                --data_folder /mnt/scratch/tmp/isvecjan/VAD_data/LibriParty/dataset \
                --open_rir_folder /mnt/scratch/tmp/isvecjan/VAD_data/RIRs \
                --musan_folder /mnt/scratch/tmp/isvecjan/VAD_data/musan \
                --commonlanguage_folder /mnt/scratch/tmp/isvecjan/VAD_data/common_voice_kpd

exit 0
