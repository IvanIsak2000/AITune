import discogs_client
from config import token
import time

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
