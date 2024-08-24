import mujoco as mj
import mujoco_viewer
import os    

class ProjectileEnv:

    class QPOS_ADR():

        BALL_POS_X = 0
        BALL_POS_Y = 1
        BALL_POS_Z = 2
    
    class QVEL_ADR():

        BALL_VEL_X = 0
        BALL_VEL_Y = 1
        BALL_VEL_Z = 2

    def __init__(self,args):
        self.xml_file = args['xml_file']
        xml_directory = os.getcwd() + "/env"
        self.xml_path = os.path.join(xml_directory,self.xml_file)
        self.cam_azi = args['cam_azi']
        self.cam_ele = args['cam_ele']
        self.cam_dist = args['cam_dist']
        self._mj_init()
        self.xpos = 0
        self.ypos = 0
        self.zpos = 0
        self.xvel = 0
        self.yvel = 0
        self.zvel = 0
        self.update_states()             

    def step(self):
        mj.mj_step(self.model,self.data)
        self.update_states()
        self.render()

    def _mj_init(self):
        self.model = mj.MjModel.from_xml_path(self.xml_path)    
        self.data = mj.MjData(self.model) 
        self.viewer = mujoco_viewer.MujocoViewer(self.model, self.data,hide_menus=True)
        self.viewer.cam.azimuth = self.cam_azi
        self.viewer.cam.elevation = self.cam_ele
        self.viewer.cam.distance =  self.cam_dist

    def render(self):
        self.viewer.render()

    def stop(self):
        if self.viewer.is_alive:
            self.viewer.close()

    def gravity_field(self,gx,gy,gz):
        self.model.opt.gravity[0] = gx
        self.model.opt.gravity[1] = gy
        self.model.opt.gravity[2] = gz

    def ball_position(self,posx,posy,posz):
        self.data.qpos[self.QPOS_ADR.BALL_POS_X] = posx
        self.data.qpos[self.QPOS_ADR.BALL_POS_Y] = posy
        self.data.qpos[self.QPOS_ADR.BALL_POS_Z] = posz

        self.update_states()
        mj.mj_forward(self.model,self.data)

    def ball_velocity(self,vx,vy,vz):
        self.data.qvel[self.QVEL_ADR.BALL_VEL_X] = vx
        self.data.qvel[self.QVEL_ADR.BALL_VEL_Y] = vy
        self.data.qvel[self.QVEL_ADR.BALL_VEL_Z] = vz
        self.update_states()

    def update_states(self):
        self.xpos = self.data.qpos[self.QPOS_ADR.BALL_POS_X]
        self.ypos = self.data.qpos[self.QPOS_ADR.BALL_POS_Y]
        self.zpos = self.data.qpos[self.QPOS_ADR.BALL_POS_Z]
        self.xvel = self.data.qvel[self.QVEL_ADR.BALL_VEL_X]
        self.yvel = self.data.qvel[self.QVEL_ADR.BALL_VEL_Y]
        self.zvel = self.data.qvel[self.QVEL_ADR.BALL_VEL_Z]

    def apply_force(self,fx,fy,fz):
        self.data.qfrc_applied[0] = fx
        self.data.qfrc_applied[1] = fy
        self.data.qfrc_applied[2] = fz




