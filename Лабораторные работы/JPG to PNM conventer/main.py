from PIL import Image

if __name__ == '__main__':
    
    # Opening jpg file
    file_name = input('Input jpg absolute file name: ')
    print(file_name)

    image = Image.open(file_name)

    # Getting size and pixels of jpg file
    img_width = image.size[0]
    img_height = image.size[1]

    print('Width: {}'.format(img_width))
    print('Height: {}'.format(img_height))

    pixels = image.load()

    # Creating new pnm image
    pnm_file_name = input('Input new pnm absolute file name: ')
    print(pnm_file_name)

    pnm = open(pnm_file_name, 'w')

    # Writing header in pnm
    pnm.write('P3\n')
    pnm.write('{} {}\n'.format(img_width, img_height))
    pnm.write('255')
    
    # Writing pixels data in pnm
    for h in range(img_height):
        for w in range(img_width):
            r = pixels[w, h][0]
            g = pixels[w, h][1]
            b = pixels[w, h][2]
            pnm.write('\n{} {} {}'.format(r, g, b))
        



