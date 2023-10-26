# -*- coding: utf-8 -*-
import random

# Datos sobre el cuidado de los gatos
info_cuidados = [
    'Recuerda que los gatos necesitan un lugar tranquilo para descansar.',
    'Es importante cepillar a tu gato regularmente para evitar la formación de bolas de pelo.',
    'Los gatos son animales muy limpios; asegúrate de mantener su caja de arena limpia.',
    'La alimentación de tu gato debe ser equilibrada y adecuada a su edad y nivel de actividad.',
    'Asegúrate de llevar a tu gato al veterinario para chequeos regulares.',
    'Los gatos son propensos a la deshidratación; siempre proporciona agua fresca.',
    'Los gatos son cazadores naturales; los juguetes interactivos pueden ayudar a estimular este instinto.',
    'Los gatos son sensibles a los cambios en su entorno; trata de mantener una rutina estable.',
    'Los gatos pueden ser sensibles a ciertos alimentos; siempre consulta con el veterinario antes de cambiar su dieta.',
    'Los gatos necesitan un lugar seguro y alto donde puedan observar su entorno.',
    'Los gatos son animales sociales; dedica tiempo cada día para jugar e interactuar con ellos.',
    'Los gatos pueden ser entrenados para usar un rascador en lugar de tus muebles.',
    'Los gatos son más activos durante el amanecer y el atardecer; considera esto al planificar su rutina.',
    'Los gatos pueden sufrir de estrés; un ambiente tranquilo y seguro es crucial para su bienestar.'
]

# Frases de amor para gatos
frases_amor = [
    'Eres el rey de la casa.',
    'Te amo más que a las siestas.',
    'Eres purr-fecto para mí.',
    'Tu ronroneo es mi melodía favorita.',
    'Eres mi pequeño tesoro peludo.',
    'Contigo, todos los días son días de ronroneo.',
    'Eres la estrella que ilumina mi vida.',
    'Tu amor es mejor que nueve vidas.',
    'Eres mi compañero perfecto para las siestas.',
    'Tu amor es la purr-fección.',
    'Eres la razón de mi sonrisa diaria.',
    'Tu amor es tan suave como tu pelaje.',
    'Eres mi pequeño rayo de sol.',
    'Tu amor es el mejor regalo que he recibido.'
]

# Chistes sobre gatos
chistes = [
    '¿Qué hace un gato cuando quiere tomar decisiones importantes? Consulta su miau-nual de vida.',
    '¿Qué dijo el gato cuando perdió todos sus juguetes? ¡Esto es un des-purr-cio!',
    '¿Cómo se llama un gato que hace yoga? Un miau-ditador.',
    '¿Qué tipo de música escuchan los gatos? Heavy miau-tal.',
    '¿Cómo se llama un gato que vive en un iglú? Un es-kimo-miau.',
    '¿Qué hace un gato cuando se convierte en abogado? Practica la ley de miau-tigación.',
    '¿Cómo se llama un gato que trabaja en un hotel? Un miau-ordomo.',
    '¿Cómo se llama un gato que ha tragado una pelota de lana? Un ovillo de misterio.',
    '¿Qué hace un gato cuando quiere ser romántico? Le da a su pareja un ramo de miau-garitas.',
    '¿Qué hace un gato cuando quiere relajarse? Se toma un miau-tini.'
]

def main():
    print('¿Quieres que te presente 1 Info sobre cuidados, 2 Frases de amor o 3 Risas?')
    eleccion = str(input('Elige una opción: ')).strip()
    
    if eleccion in ['1', '1 Info sobre cuidados']:
        print(random.choice(info_cuidados))
    elif eleccion in ['2', '2 Frases de amor']:
        print(random.choice(frases_amor))
    elif eleccion in ['3', '3 Risas']:
        print(random.choice(chistes))
    else:
        print('Opción no válida. Por favor, elige 1, 2, 3 o el texto completo de la opción.')

if __name__ == '__main__':
    main()
