class Image(object):
    def __init__(self, mass, pos, vel = None):
        # images also have red, green and blue
        # pickle. pickle a panda  
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.interactions = []
        