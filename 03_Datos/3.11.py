camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]

from collections import Counter
total_cajones = Counter ()
for nombre, n_cajones, precio in camion:
    total_cajones[nombre] += n_cajones

print(total_cajones['Naranja'])
