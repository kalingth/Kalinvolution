from numpy import array, angle

IMAGE_SUPPORTED_FORMATS = [
    "bmp",
    "dib",
    "jpeg",
    "jpg",
    "jpe",
    "jp2",
    "png",
    "webp",
    "pbm",
    "pgm",
    "ppm",
    "pxm",
    "pnm",
    "pfm",
    "sr",
    "ras",
    "tiff",
    "tif",
    "exr",
    "hdr",
    "pic",
]

VIDEO_SUPPORTED_FORMATS = [
    "avi",
    "mp4",
    "m4v",
    "3gp",
    "3g2"
]


class BaseKernels:
    """BaseKernels:

    That class contains the sample of kernels with their respective normalize function.    
    """

    IDENTITY = lambda arr: arr * 1, array([
        [ 0, 0, 0],
        [ 0, 1, 0],
        [ 0, 0, 0]
    ])

    SHARPEN = lambda arr: arr * 1, array([
        [ 0,-1, 0],
        [-1, 5,-1],
        [ 0,-1, 0],
    ])

    BLUR = lambda arr: arr * 1, array([
        [ 0, 0, 0, 0, 0],
        [ 0, 1, 1, 1, 0],
        [ 0, 1, 1, 1, 0],
        [ 0, 1, 1, 1, 0],
        [ 0, 0, 0, 0, 0]
    ])

    BOX_BLUR = lambda arr: arr * 1/9, array([
        [ 1, 1, 1],
        [ 1, 1, 1],
        [ 1, 1, 1]
    ])

    GAUSSIAN_BLUR = lambda arr: arr * 1/16, array([
        [ 1, 2, 1],
        [ 2, 4, 2],
        [ 1, 2, 1]
    ])
    
    GAUSSIAN_BLUR_5X5 = lambda arr: arr * 1/256, array([
        [  1,  4,  6,  4,  1],
        [  4, 16, 24, 16,  4],
        [  6, 24, 36, 24,  6],
        [  4, 16, 24, 16,  4],
        [  1,  4,  6,  4,  1]
    ])

    UNSHARP_MASK = lambda arr: arr * 1/256, array([
        [ -1, -4, -6, -4, -1],
        [ -4,-16,-24,-16, -4],
        [ -6,-24,476,-24, -6],
        [ -4,-16,-24,-16, -4],
        [ -1, -4, -6, -4, -1]
    ])

    EDGE_VARIATION_1 = lambda arr: arr * 1, array([
        [ 1, 0,-1],
        [ 0, 0, 0],
        [-1, 0, 1]
    ])

    EDGE_VARIATION_2 = lambda arr: arr * 1, array([
        [ 0, 1, 0],
        [ 1,-4, 1],
        [ 0, 1, 0]
    ])

    EDGE_VARIATION_3 = lambda arr: arr * 1, array([
        [-1,-1,-1],
        [-1, 8,-1],
        [-1,-1,-1]
    ])

    EDGE_VARIATION_4 = lambda arr: arr * 1, array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ])

    EDGE_ENHANCE = lambda arr: arr * 1, array([
        [ 0, 0, 0],
        [-1, 1, 0],
        [ 0, 0, 0]
    ])

    EMBOSS = lambda arr: arr * 1, array([
        [-2,-1, 0],
        [-1, 1, 1],
        [ 0, 1, 2]
    ])

    SCHARR = lambda arr: angle(arr), array([
        [ -3-3j, 0-10j,  +3 -3j],
        [-10+0j, 0+ 0j, +10 +0j],
        [ -3+3j, 0+10j,  +3 +3j]
    ])

    SOBEL = lambda arr: arr * 1, array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])

    MY_BLUR = lambda arr: arr * 1/2, array([
        [ 1,-1, 1],
        [-1, 1,-1],
        [ 1,-1, 1]
    ])

    MY_EDGE = lambda arr: arr * 5, array([
        [ 1,-1, 1],
        [-1, 0,-1],
        [ 1,-1, 1]
    ])

    MY_FILTER = lambda arr: angle(arr), array([
        [1-3j,-2+1j,-3+1j],
        [2-2j, 5-1j,-2+2j],
        [3-1j,-2+1j,-1+3j]
    ])
