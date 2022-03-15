import cv2
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
from Misc.CONSTANTS import BaseKernels

class Effect(BaseKernels):
    kernels = {
        "Identity": "identityEffect",
        "Blur": "blurEffect",
        "Sharpen": "sharpenEffect",
        "BoxBlur": "boxBlurEffect",
        "GaussianBlur": "gaussianBlurEffect",
        "GaussianBlurWith5x5Kernel": "gaussianBlur5x5Effect",
        "Unsharp": "unsharpMaskEffect",
        "EdgeOne": "edgeVariationOneEffect",
        "EdgeTwo": "edgeVariationTwoEffect",
        "EdgeThree": "edgeVariationThreeEffect",
        "EdgeFour": "edgeVariationFourEffect",
        "Edge": "edgeEnhanceEffect",
        "Emboss": "embossEffect",
        "Scharr": "scharrEffect",
        "Sobel": "sobelEffect",
        "Custom": "customizedEffect",
        "AhaEffect": "ahaEffect",
    }

    def identityEffect(self):
        normalizer, kernel = self.IDENTITY
        filteredFloat64Image = self.convolution(self.__frame, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def blurEffect(self):
        normalizer, kernel = self.BLUR
        filteredFloat64Image = self.convolution(self.__frame, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def sharpenEffect(self):
        normalizer, kernel = self.SHARPEN
        filteredFloat64Image = self.convolution(self.__frame, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def boxBlurEffect(self):
        normalizer, kernel = self.BOX_BLUR
        filteredFloat64Image = self.convolution(self.__frame, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def gaussianBlurEffect(self):
        normalizer, kernel = self.GAUSSIAN_BLUR
        filteredFloat64Image = self.convolution(self.__frame, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def gaussianBlur5x5Effect(self):
        normalizer, kernel = self.GAUSSIAN_BLUR_5X5
        filteredFloat64Image = self.convolution(self.__frame, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def unsharpMaskEffect(self):
        normalizer, kernel = self.UNSHARP_MASK
        filteredFloat64Image = self.convolution(self.__frame, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def edgeVariationOneEffect(self):
        grayScaled = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2GRAY)
        normalizer, kernel = self.EDGE_VARIATION_1
        filteredFloat64Image = self.convolution(grayScaled, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def edgeVariationTwoEffect(self):
        grayScaled = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2GRAY)
        normalizer, kernel = self.EDGE_VARIATION_2
        filteredFloat64Image = self.convolution(grayScaled, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def edgeVariationThreeEffect(self):
        grayScaled = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2GRAY)
        normalizer, kernel = self.EDGE_VARIATION_3
        filteredFloat64Image = self.convolution(grayScaled, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def edgeVariationFourEffect(self):
        normalizer, kernel = self.EDGE_VARIATION_4
        filteredFloat64Image = self.convolution(self.__frame, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def edgeEnhanceEffect(self):
        grayScaled = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2GRAY)
        normalizer, kernel = self.EDGE_ENHANCE
        filteredFloat64Image = self.convolution(grayScaled, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def embossEffect(self):
        normalizer, kernel = self.EMBOSS
        filteredFloat64Image = self.convolution(self.__frame, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def scharrEffect(self):
        normalizer, kernel = self.SCHARR
        filteredFloat64Image = self.convolution(self.__frame, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def sobelEffect(self):
        normalizer, kernel = self.SOBEL
        filteredFloat64Image = self.convolution(self.__frame, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def customizedEffect(self):
        normalizer, kernel = self.MY_FILTER
        filteredFloat64Image = self.convolution(self.__frame, kernel)
        normalizedFloat64Image = normalizer(filteredFloat64Image)
        filteredUint8 = self.anyDTypeToUnsignedInteger8(normalizedFloat64Image)
        self.newFrame = filteredUint8

    def ahaEffect(self, contrastAlpha=0.95, contrastBeta=0.8):
        grayScaled = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2GRAY)
        invertedGrayScaledImage = 255 - grayScaled
        contrastedFrame = cv2.convertScaleAbs(
            invertedGrayScaledImage, alpha=contrastAlpha, beta=contrastBeta
        )
        blurredFrame = cv2.GaussianBlur(contrastedFrame, (21, 21), 0)
        invertedBlurredFrame = 255 - blurredFrame
        ahaImage = cv2.divide(grayScaled, invertedBlurredFrame, scale=256.0)
        self.newFrame = cv2.cvtColor(ahaImage, cv2.COLOR_GRAY2RGB)

    @staticmethod
    def convolution(frame, kernel):
        if len(frame.shape) != 3:
            convolvedGrayScale = sig.convolve2d(frame, kernel, mode="same")
            return convolvedGrayScale

        redLayer = frame[:, :, 0]
        greenLayer = frame[:, :, 1]
        blueLayer = frame[:, :, 2]

        convolvedRed = sig.convolve2d(redLayer, kernel, mode="same")
        convolvedGreen = sig.convolve2d(greenLayer, kernel, mode="same")
        convolvedBlue = sig.convolve2d(blueLayer, kernel, mode="same")

        convolvedFloat64 = np.dstack((convolvedRed, convolvedGreen, convolvedBlue))
        return convolvedFloat64

    @staticmethod
    def anyDTypeToUnsignedInteger8(frame, channels=3):
        height, width = frame.shape[:2]
        proportion = width / 100., height / 100.
        figure = plt.figure(figsize=proportion)
        frameSubplotted = figure.add_subplot(111)
        frameSubplotted.imshow(frame.astype(np.uint8))
        frameSubplotted.axis('off')
        figure.canvas.draw()
        rawData = figure.canvas.tostring_rgb()
        array = np.frombuffer(rawData, dtype=np.uint8)
        return array.reshape(height, width, channels)

    @property
    def newName(self):
        return self.newFileName

    @newName.setter
    def newName(self, name):
        if self.validateFormat(name):
            self.newFileName = name
        else:
            raise self.ImageNotSupportedError(
                "That image is not supported by that program"
            )

    @property
    def name(self):
        return self.oldFileName

    @name.setter
    def name(self, name):
        if self.validateFormat(name):
            self.oldFileName = name
        else:
            raise self.ImageNotSupportedError(
                "That image is not supported by that program"
            )

    @property
    def matrixImage(self):
        return self.__frame

    @matrixImage.setter
    def matrixImage(self, newMatrix):
        self.__frame = newMatrix

    def display(self, millis=0, seconds=0):
        try:
            cv2.imshow("Filtered Image", self.newFrame)
            if millis == 0 and seconds == 0:
                cv2.waitKey(0)
            else:
                waitFor = millis or seconds * 1000
                cv2.waitKey(waitFor)
            cv2.destroyAllWindows()
        except AttributeError as error:
            raise self.ImageNotSettedError(
                "The frame was not converted yet! Please, run the convert method."
            )

    def validateFormat(self, name):
        validationList = [extension in name for extension in self.suportedFormats]
        return any(validationList)

    def apply(self, effectName="AhaEffect"):
        function = self.kernels[effectName]
        getattr(self, function)()

    def __init__(self, frame, effectName="AhaEffect"):
        self.__frame = frame
