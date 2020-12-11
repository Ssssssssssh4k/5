

if __name__ == '__main__':

    file_name = 'C:\\Users\\dimaz\\Desktop\\Denis_Labs\\Lab2\\images\\icecream.pnm'
    result_file_name = 'C:\\Users\\dimaz\\Desktop\\Denis_Labs\\Lab2\\result\\icecream.pnm'

    # Opening pnm file data for read    
    image = open(file_name, 'r')
    image = image.read()
    image = image.split('\n')

    # Getting size of image
    size = image[1].split(' ')

    width = int(size[0])
    height = int(size[1])

    # Creating values for finding bounding box
    middle_value = 127

    max_x = 0
    min_x = width

    max_y = 0
    min_y = height

    avrg_x = 0
    avrg_y = 0

    count = 0

    # Finding values for finding bounding box
    for index in range(3, len(image) ):
        y = (index - 3) // width
        x = (index - 3) - (y * width)

        # Getting greyscale value of pixel
        greyscale = 0
        pixel = image[index].split(' ')

        for i in range( len(pixel) ):
            greyscale += int(pixel[i])

        greyscale /= len(pixel)

        # Is greyscale value darker than middle value?
        if (greyscale < middle_value):
            avrg_x += x
            avrg_y += y
            count += 1

            if (x > max_x):
                max_x = x

            if (x < min_x):
                min_x = x

            if (y > max_y):
                max_y = y

            if (y < min_y):
                min_y = y

    
    # Finding middle point
    avrg_x = avrg_x // count
    avrg_y = avrg_y // count

    print('Max x = ' + str(max_x))
    print('Min x = ' + str(min_x))

    print('Max y = ' + str(max_y))
    print('Min y = ' + str(min_y))

    print('Middle point x = ' + str(avrg_x))
    print('Middle point y = ' + str(avrg_y))


    # Creating result image
    result = open(result_file_name, 'w')

    # Writing header in pnm
    result.write(image[0] + '\n')
    result.write(image[1] + '\n')
    result.write(image[2])

    for h in range(height):
        for w in range(width):

            # Drawing top of bounding box
            if (h == min_y) and ((w >= min_x) and (w <= max_x)):
                result.write('\n{} {} {}'.format(255, 0, 0))

            # Drawing bottom of bounding box
            elif (h == max_y) and ((w >= min_x) and (w <= max_x)):
                result.write('\n{} {} {}'.format(255, 0, 0))

            # Drawing left of bounding box
            elif (w == min_x) and ((h >= min_y) and (h <= max_y)):
                result.write('\n{} {} {}'.format(255, 0, 0))

            # Drawing right of bounding box
            elif (w == max_x) and ((h >= min_y) and (h <= max_y)):
                result.write('\n{} {} {}'.format(255, 0, 0))

            else:
                result.write('\n{}'.format(image[(h * width + w) + 3]))



