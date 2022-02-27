from django.http import HttpResponse

from lesson_5.models import Flower, Bouquet, Client
from uuid import uuid4
from decimal import Decimal

from django.contrib.auth.models import User

from django.core.files import File


def create_flower(request):
    rose = Flower()
    rose.count = 5
    rose.description = "Роза белая является представителем семейства Разноцветных," \
                       " рода Шиповник. Растение в большинстве случаев " \
                       "представляет собой разветвленный кустарник, стебли" \
                       " которого покрыты шипами, роза имеет зеленые листья" \
                       " и большие ароматные цветы самого разного окраса"
    rose.wiki_page = "https://ru.wikipedia.org/wiki/%D0%91%D0%B5%D0%BB%D0%B0%D1%8F_%D1%80%D0%BE%D0%B7%D0%B0"
    rose.name = "Роза белая"
    rose.save()
    return HttpResponse("Created!")


def create_client(request):
    client = Client.objects.create(**{
        # 'user': User.objects.get(pk=1),
        'second_email': 'Sasha@admin.com',
        'name': 'Sasha',
        'invoice': File(open('requirements.txt')),
        'user_uuid': uuid4(),
        'discount_size': Decimal("0.00052"),
        'client_ip': "192.0.0.1.",
    })
    print(client)
    price = Bouquet.shop.get(pk=1).price
    return HttpResponse(price)


def get_flower(request, pk):
    od = Bouquet.objects.all()
    price = Bouquet.shop.get(pk=pk).price
    print('dffffggdgd', od)
    return HttpResponse(price)
