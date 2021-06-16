import pandas as pd
import numpy as np


k400train = pd.read_csv('train.csv')
k200 = pd.read_csv('train_ytid_list.txt', 
                   header=None, names=['youtube_id'])
k200train = pd.merge(k400train, k200).sort_values(
    by=['label', 'youtube_id'], ignore_index=True)
k200train.to_csv('train_k200.csv', index=False)


k400val = pd.read_csv('val.csv')
k200 = pd.read_csv('val_ytid_list.txt', 
                   header=None, names=['youtube_id'])
k200val = pd.merge(k400val, k200).sort_values(
    by=['label', 'youtube_id'], ignore_index=True)
k200val.to_csv('val_k200.csv', index=False)




