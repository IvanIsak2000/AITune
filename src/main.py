import discogs_client
from discogs_client import exceptions
from config import token
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler


def get_songs():
    d = discogs_client.Client('ExampleApplication/0.1', user_token=token)

    res = d.search(genre='Rock')
    songs_on_page = res.page(1)
    for song in songs_on_page:
        try:
            year = d.release(song.id).year
            print(f'Id: <{song.id}> Name: <{song.title}> Year: <{year}>')
            time.sleep(0.5)

        except discogs_client.exceptions.HTTPError:
            print(f'Id: <{song.id}> Name: <{song.title}> Year: <Not found>')

        except KeyboardInterrupt:
            exit('Goodbye!')


def learning():
    cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
    df = pd.read_csv('magic04.data', names=cols)
    df["class"] = (df["class"] == "g").astype(int)
    for label in cols[:-1]:
        plt.hist(df[df["class"] == 1][label], color='blue', label='gamma', alpha=0.7, density=True)
        plt.hist(df[df["class"] == 0][label], color='red', label='hadron', alpha=0.7, density=True)
        plt.title(label)
        plt.ylabel("Probability")
        plt.xlabel(label)
        plt.legend()
        plt.show()


if __name__ == '__main__':
    learning()
