class Image(object):
    def __init__(self, red, green, blue, meanred, meangreen, meanblue, variancered, variancegreen, varianceblue):
        # images also have red, green and blue
        # pickle. pickle a panda  
        self.red = red
        self.green = green
        self.blue = blue
        self.meanred = meanred
        self.meangreen = meangreen
        self. meanblue = meanblue
        self.variancered = variancered
        self.variancegreen = variancegreen
        self.varianceblue = varianceblue

        