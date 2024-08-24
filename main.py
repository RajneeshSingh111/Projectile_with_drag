import numpy as np
def main(args):

    from env.projectile_env import ProjectileEnv
    from projectile import Projectile
    env = ProjectileEnv(args)
    env.gravity_field(0,0,-9.81)
    env.ball_position(0,0,0.1)
    control = Projectile(env,args)
    control.project()
    for i in range(5000):
        control.drag_force()
        env.step()
    env.stop()

if __name__ == "__main__":
    args={}
    args['xml_file'] = 'projectile.xml'
    args['cam_azi']     = 90
    args['cam_ele']     = -10
    args['cam_dist']    =  5
    args['vx']          = 3
    args['vz']          = 4
    args['drag_coeff']  = 5
    main(args)


