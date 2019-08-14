import barcode
from barcode.writer import ImageWriter as IW

for n in range(1, 11):
    barcode.generate('code128',
                     '{:012d}'.format(n),
                     writer=IW(),
                     output='barcode128_{:03d}'.format(n))
