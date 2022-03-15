import os
import sys
import cv2
from scipy.misc import face
from Processors.FrameProcessor import Effect
from Misc.CONSTANTS import IMAGE_SUPPORTED_FORMATS

class ImageEffect(Effect):

    suportedFormats = IMAGE_SUPPORTED_FORMATS

    class ImageNotSettedError(AttributeError):
        pass

    class ImageNotSupportedError(Exception):
        pass

    def readImage(self):
        self.matrixImage = cv2.imread(self.oldFileName)
        return self.matrixImage

    def run(self, effect="AhaEffect"):
        self.apply(effect)
        self.display(2000)
        self.export()

    def export(self):
        cv2.imwrite(self.newFileName, self.newFrame)

    def __init__(self, imageName="sample.input", imageOutputName="output.png"):
        if not self.validateFormat(imageName) and imageName != "sample.input":
            raise self.ImageNotSupportedError(
                "The format of inputed image is not supported by that program!"
            )
        elif not self.validateFormat(imageName) and imageName != "sample.input":
            raise self.ImageNotSupportedError(
                "The format of output image name is not supported by that program!"
            )
        self.frame = cv2.imread(imageName) if imageName != "sample.input" else face()
        super().__init__(self.frame)
        self.oldFileName = imageName
        self.newFileName = imageOutputName



if __name__ == "__main__":
    truePath = os.path.abspath(".")
    image = ImageEffect(*sys.argv[1:])
    name, extension = image.newName.split('.')
    for effect in Effect.kernels.keys():
        image.newName = f"{name}_{effect}.{extension}"
        image.run(effect)
