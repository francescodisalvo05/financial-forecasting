from typing import Text, Dict

from constants.config import MOVIE_DATASET, FINANCIAL_DATASET, TWITTER_DATASET, SST_DATASET, YAHOO_DATASET, NN_DATASET
from core.decorators.time_decorator import timing
from scripts.datasets.dataset import NN_Dataset
from scripts.datasets.financial_dataset import FinancialPhraseBankDataset
from scripts.datasets.movie_dataset import MovieDataset
from scripts.datasets.sst_dataset import SSTDataset
from scripts.datasets.twitter_dataset import TwitterDataset
from scripts.datasets.yahoo_dataset import YahooDataset


def init_dataset(dataset_type: Text):

    if dataset_type == MOVIE_DATASET:
        return MovieDataset
    elif dataset_type == FINANCIAL_DATASET:
        return FinancialPhraseBankDataset
    elif dataset_type == TWITTER_DATASET:
        return TwitterDataset
    elif dataset_type == SST_DATASET:
        return SSTDataset
    elif dataset_type == YAHOO_DATASET:
        return YahooDataset
    elif dataset_type == NN_DATASET:
        return NN_Dataset
    else:
        raise AttributeError(f'Dataset type not found: {dataset_type}')


@timing
def dataset_generation(params: Dict):
    data_path = params['data_path']
    dataset_type = params['dataset_type']

    dataset_class = init_dataset(dataset_type)
    dataset = dataset_class(data_path)

    return dataset
