import numpy as np
class Projectile:
    def __init__(self,env,args):
        self.env    = env
        self.vx_0   = args['vx']
        self.vz_0   = args['vz']
        self.vx     = 0
        self.vz     = 0
        self.c      = args['drag_coeff']
    def project(self):
        self.env.ball_velocity(self.vx_0,0,self.vz_0)
    def drag_force(self):
        self.vx = self.env.xvel
        self.vy = self.env.yvel
        self.vz = self.env.zvel
        v = np.sqrt(self.vx**2 + self.vy**2 + self.vz**2)
        fx = -self.c*v*self.vx
        fy = -self.c*v*self.vy
        fz = -self.c*v*self.vz
        self.env.apply_force(fx,fy,fz)

        

