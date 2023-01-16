import imageio.v3 as iio
import imageio.core as iioc
import numpy as np

def main():
    im = iio.imread('Data/images.jpg')
    reference_img = iioc.image_as_uint(im)
    print(im.shape)
    row, col, z = im.shape
    aspect_ratio = col / row
    find_closest_resolution(aspect_ratio,20)
    new_img = gradient_array(row,col,z)
    new_img = array_to_image(new_img)

    #print(len(iioc.image_as_uint(im)))
    iio.imwrite("jeff.png", new_img)
    #print(type(iioc.image_as_uint(im)))

def find_closest_resolution(aspect_ratio, num_of_images):
    compare = list(zip([x for x in range(1, num_of_images)],
                    [y for y in range(num_of_images-1, 0, -1)]))
    print(aspect_ratio)
    temp_ratio = compare[0]
    for x,y in compare:
        if abs(aspect_ratio - (x / y)) < abs(aspect_ratio - (temp_ratio[0] / temp_ratio[1])):
            temp_ratio = (x, y)

    print(temp_ratio)
    return temp_ratio

def gradient_array(row,col,z):
    new_img = []
    for oi in range(0,row):
        temp_row = []
        for ii in range(0,col):
            temp_row.append([ii, oi, oi*ii / 255])
        new_img.append(temp_row)
    return new_img

def array_to_image(array):
    array = iioc.asarray(array).astype(np.uint8)
    img = iioc.util.Array(array)
    return iioc.util.Array(img)

if __name__ == "__main__":
    main()
