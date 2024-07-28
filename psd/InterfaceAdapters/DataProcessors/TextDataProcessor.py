import numpy as np
from typing import List
from ApplicationServices.IDataProcessors.IDataProcessor import IDataProcessor


class TextDataProcessor(IDataProcessor):

    def preprocess_text_data(self, text: list) -> np.ndarray:
        return None
