#THIS IS NOT DONE

class Experiment(object):
    def __init__(self, listofimages, meanRGB, varianceRGB):
        self.listofimages = listofimages
        self.meanRGB = meanRGB
        self.varianceRGB = varianceRGB
        self.inputarray = [self.meanRGB, self.varianceRGB, self.listofimages]