from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import BangliEmpathyException
import pandas as pd
import sys
from typing import Optional
import numpy as np



from datasets import load_dataset

class CSVDataLoader:
    """
    Responsible ONLY for loading datasets.
    Easily swappable with JSON / Parquet / HF datasets later.
    """

    def __init__(self, csv_path: str):
        self.csv_path = csv_path

    def load(self, split="train"):
        """
        Loads CSV into HuggingFace Dataset
        """
        return load_dataset(
            "csv",
            data_files=self.csv_path,
            split=split
        )

class BangaliEmpathyData:
    """
    Responsible ONLY for loading datasets.
    Easily swappable with JSON / Parquet / HF datasets later.
    """

    def __init__(self):
        """
        """
        try:
            self.csv_path = "/kaggle/input/bengali-empathetic-conversations-corpus/BengaliEmpatheticConversationsCorpus .csv"
        except Exception as e:
            raise BangliEmpathyException(e,sys)
        

    def load(self, split="train"):
        try:
            """
            export entire collectin as dataframe:
            return pd.DataFrame of collection
            """
            empathydata=load_dataset(
            "csv",
            data_files=self.csv_path,
            split=split
        )
            return empathydata
        except Exception as e:
            raise BangliEmpathyException(e,sys)