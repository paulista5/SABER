from audtorch import datasets, transforms
from utils.config import max_audio_length_in_secs, sampling_rate, max_label_length, min_audio_length_in_secs, lmdb_airtel_root_path
from utils.lmdb import createDataset_parallel as createDataset
from utils.logger import logger
from datasets.librispeech import convert_to_mel, label_transform
import os
import pandas as pd
from functools import partial

def exclude_func(img, label):
    audio_size = img.squeeze(0).shape[0]
    label_size = len(label)
    return not ((min_audio_length_in_secs <= (audio_size / sampling_rate) <= max_audio_length_in_secs) and (label_size <= max_label_length))

if __name__ == '__main__':
    lmdb_root_path = lmdb_airtel_root_path
    commonvoice_dataset_root = "/tts_data/asrdata/AirtelAudioCorpus"
    language_codes = ["en"]

    for language in language_codes:
        trainPath = os.path.join(lmdb_root_path, f'train-labelled-{language}')
        testPath = os.path.join(lmdb_root_path, f'test-labelled-{language}')
        os.makedirs(lmdb_root_path, exist_ok=True)
        os.makedirs(trainPath, exist_ok=True)
        os.makedirs(testPath, exist_ok=True)
        logger.info('Loading datasets')

        convert_to_mel_val = partial(convert_to_mel, train=False)

        train_csv_path = os.path.join(commonvoice_dataset_root, "train.csv")
        labelled_df = pd.read_csv(train_csv_path).rename(columns={"audio_filepath": "audio_path", "text": "transcription"})
        data_labbeled = datasets.LibriSpeech(root=commonvoice_dataset_root, dataframe=labelled_df)
        logger.info('Labelled dataset loaded')
        createDataset(trainPath, data_labbeled, convert_to_mel, label_transform, exclude_func)
        logger.info(f"Num of labelled examples {len(data_labbeled)}")
        del data_labbeled

        test_csv_path = os.path.join(commonvoice_dataset_root, "test.csv")
        test_df = pd.read_csv(test_csv_path).rename(columns={"audio_filepath": "audio_path", "text": "transcription"})
        data_test = datasets.LibriSpeech(root=commonvoice_dataset_root, dataframe=test_df)
        logger.info('test dataset loaded')
        createDataset(testPath, data_test, convert_to_mel_val, label_transform, exclude_func)
        logger.info(f"Num of test examples {len(data_test)}")
        del data_test