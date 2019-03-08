import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','hospital.settings')

import timeit, winsound, random, django
django.setup()

from busqueda.models import Persona
#faker
from faker import Faker
fake = Faker()

tiposeguro = ['per', 'par', 'fam']
def addpersona(n=1):
    for _ in range(n):
        #p = Persona.objects.get_or_create(nombre=fake.first_name(), apellido_p=fake.last_name(), apellido_m = fake.last_name(), carnet =fake.msisdn(), tipo_seguro=random.choice(tiposeguro), region=fake.city())[0]
        p = Persona.objects.create(nombre=fake.first_name(), apellido_p=fake.last_name(), apellido_m = fake.last_name(), carnet =fake.msisdn(), tipo_seguro=random.choice(tiposeguro), region=fake.city())
        p.save()
    return 0

if __name__ == '__main__':
    print('ingresando datos , please wait')
    
    try:
        n = int(input('cuantos datos quiere ingresar ? \n ='))
        before=timeit.timeit()
        addpersona(n)
        after=timeit.timeit()
        print('finalizado en : ',after - before)
        winsound.Beep(2000,200)
        winsound.Beep(2000,200)
    except ValueError:
        print('error')