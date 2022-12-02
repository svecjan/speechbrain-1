#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from speechbrain.dataio.dataio import load_htk

if __name__ == "__main__":
    pass
    # scp = "/Users/svec/workspace/speechbrain1/htk/Turkish.vB1.train.wav.scp"
    scp = "/mnt/matylda3/isvecjan/workspace/speechbrain1/htk/babel.scp"
    # mlf = "/Users/svec/workspace/speechbrain1/htk/align.state.hmm184.xwrd.mlf"
    # mlf = "/Users/svec/workspace/speechbrain1/htk/test.mlf"
    mlf = "/mnt/matylda3/isvecjan/workspace/speechbrain1/htk/babel.mlf"

    train_file = "/mnt/matylda3/isvecjan/workspace/speechbrain1/htk/train.json"
    dev_file = "/mnt/matylda3/isvecjan/workspace/speechbrain1/htk/valid.json"
    test_file = "/mnt/matylda3/isvecjan/workspace/speechbrain1/htk/test.json"

    load_htk(scp, mlf, train_file, dev_file, test_file)
