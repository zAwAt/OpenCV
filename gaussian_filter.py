import numpy
import cv2,os

def To_GRGB(image,RGB_bool=False):
    if RGB_bool==True:
        print("RGB format is selected")
        converted = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    else:
        print("GRAY format is selected")
        converted = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return converted

def print_image_elements(image,pixelbool=False):
    print("converted image's shape=",image.shape,"type=",type(image),"pixelype=",type(image[0][0]))
    print(image.shape[0])
    if pixelbool==True:
        for i in range(image.shape[0]):
            for j  in range(image.shape[1]):
                print(image[i][j])
    else:
        pass

def gaussian_filter(image,kernel):
    center = (kernel.shape[0]-1)/2
    print(kernel.shape[0])
    print(center)
    copy_image=numpy.copy(image)
    for i in range(center,copy_image.shape[0]-center):
        for j in range(center,copy_image.shape[1]-center):
            copy_image[i][j]=numpy.sum(image[i-center:i+center+1,j-center:j+center+1]*kernel)
    return copy_image

def kernel_creater(size,default_bool=False):
    if default_bool==True:
        print("use default gaussian 3x3")
        kernel = numpy.array([[1/16.0,1/8.0,1/16.0],[1/8.0,1/4.0,1/8.0],[1/16.0,1/8.0,1/16.0]])
    else:
        print("use customized gaussian {0}x{0}").format(size)
        sigma=1.3
        kernel=numpy.zeros((size,size))
        center=size-size/2-1
        for i in range(size):
            for j in range(size):
                kernel[i][j]=(1/(2*3.14*sigma*sigma))*numpy.exp(-float((i-center)*(i-center)+(j-center)*(j-center))/(2*sigma*sigma))
        sum=0
        for i in range(size):
            for j in range(size):
                sum=kernel[i][j]+sum
        kernel=kernel/sum
    return kernel

def main_process():
    image_name=os.path.joim("hoge","hoge.png")
    image=cv2.imread(image_name)

    CONVERTED=To_GRGB(image)
    print_image_elements(CONVERTED,False)
    cv2.imshow("A",CONVERTED)

    CONVERTED=gaussian_filter(CONVERTED,kernel_creater(5))
    print_image_elements(CONVERTED,False)
    cv2.imshow("GAUSS",CONVERTED)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__== "__main__":
    main_process()
