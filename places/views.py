from django.http import JsonResponse
from places.models import Place
from django.shortcuts import get_object_or_404, render, reverse


def get_geo_object(place):
    geo_object = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
          },
          "properties": {
            "title": place.title,
            "detailsUrl": reverse('show_place', kwargs={'place_id': place.id}),
          }
        },

    return geo_object


def show_index(request):
    features = [get_geo_object(place) for place in Place.objects.all()]
    geo_spots = {
        'type': 'FeatureCollection',
        'features': features,
    }
    context = {'geo_spots': geo_spots}

    return render(request, 'index.html', context)


def show_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images = [image.imgs.url for image in place.images.all()]
    response = {
        'title': place.title,
        'imgs': images,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng,
        },
    }

    return JsonResponse(
        response,
        json_dumps_params={
            'indent': 2,
            'ensure_ascii': False,
        },
    )
