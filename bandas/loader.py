from bandas.models import *
import json

Band.objects.all().delete()
Album.objects.all().delete()
Song.objects.all().delete()

with open('bandas/bibliotecaJson/bandas.json') as f:
    bandas = json.load(f)

    for banda in bandas['bands']:
        num_members = banda.get('num_members', 1)  
        Band.objects.create(
            name=banda['name'],
            nationality=banda['nationality'],
            year_start=banda['year_created'],
            num_members=num_members
        )

with open('bandas/bibliotecaJson/discos.json') as f:
    discos = json.load(f)
    for album_info in discos['albums']:
        banda, _ = Band.objects.get_or_create(name=album_info['band'])
        album, _ = Album.objects.get_or_create(
            band=banda,
            title=album_info['title'],
            defaults={
                'number_of_songs': len(album_info['tracks']),
                'release_year': album_info['year'],
            }
        )
        for musica_info in album_info['tracks']:
            Song.objects.create(
                album=album,
                title=musica_info['title'],
                duration=musica_info['duration']
            )