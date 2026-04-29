import rebound
import numpy as np


def forced(T_total, n_points):
    # ---------- PARAMETERS ----------
    # Units: years, AU, solar mass
    output_interval = 1e3    # years between recording semimajor axes (adjust to control output size)
    integrator = "WHFast"    # "WHFast" or "IAS15"
    n_points = int(n_points)
    # dt = T_total / n_points
    # --------------------------------

    # Create simulation
    sim = rebound.Simulation()
    sim.units = ('yr', 'AU', 'Msun')
    sim.integrator = integrator
    sim.dt = 1.0e-4  # Integrator timestep
    
    # Properties of the planets
    M_earth = 3.003e-6
    P=np.array([ 8.249164, 12.401394, 24.140006, 48.677714])/365.25
    mass=np.array([ 4.7 , 6.0, 13.1, 15.3])*M_earth 
 
    sim.add(m = 1.26)  # central star
    sim.add(m = mass[0] , P = P[0] , e = 0e-3, inc = 0.0 , Omega=0.0, omega=0.0, M=0.0)
    sim.add(m = mass[1] , P = P[1] , e = 0e-3, inc = 0.0 , Omega=0.0, omega=0.0, M=10.0)
    sim.add(m = mass[2] , P = P[2] , e = 0e-3, inc = 0.0 , Omega=0.0, omega=0.0, M=180.0)
    sim.add(m = mass[3] , P = P[3] , e = 0e-3, inc = 0.0 , Omega=0.0, omega=0.0, M=270.0)


    # Add planets via orbital elements
    
    sim.move_to_com()  # move to center-of-momentum frame

    print("Integrator:", sim.integrator, "dt (yr):", sim.dt)
    print(f"Total integration time: {T_total:.2e} yr, output every {output_interval} yr")

    times = np.linspace(0,T_total,n_points+1)
    a = np.zeros([4,n_points+1])
    e = np.zeros([4,n_points+1])

    for i,time in enumerate(times):
        sim.integrate(time)#, exact_finish_time=0)
        orbits = sim.orbits(primary=sim.particles[0])
        
        for p, orbit in enumerate(orbits):
            a[p,i] = orbit.a
            e[p,i] = orbit.e
        
    return times , a , e

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################

def resonance(T_total, n_points,e0):
    # ---------- PARAMETERS ----------
    # Units: years, AU, solar mass
    integrator = "WHFast"    # "WHFast" 
    n_points = int(n_points)
    dt = T_total / n_points
    # --------------------------------

    # Create simulation
    sim = rebound.Simulation()
    sim.units = ('yr', 'AU', 'Msun')
    sim.integrator = integrator
    sim.dt = dt * 0.1
    
    # Properties of the planets
    M_earth = 3.003e-6
    P=np.array([ 8.249164, 12.401394, 24.140006, 48.677714])/365.25
    mass=np.array([ 4.7 , 6.0, 13.1, 15.3])*M_earth 

    sim.add(m = 1.26)  # central star
    sim.add(m = mass[0] , P = P[0] , e = e0[0], inc = np.random.rand()*2*np.pi/180 ,
                                                Omega=np.random.uniform(0, 2*np.pi), 
                                                omega=np.random.uniform(0, 2*np.pi), 
                                                M=np.random.uniform(0, 2*np.pi))
    sim.add(m = mass[1] , P = P[1] , e = e0[1], inc = np.random.rand()*2*np.pi/180  , 
                                                Omega=np.random.uniform(0, 2*np.pi), 
                                                omega=np.random.uniform(0, 2*np.pi), 
                                                M=np.random.uniform(0, 2*np.pi))
    sim.add(m = mass[2] , P = P[2] , e = e0[2], inc = np.random.rand()*2*np.pi/180  , 
                                                Omega=np.random.uniform(0, 2*np.pi), 
                                                omega=np.random.uniform(0, 2*np.pi), 
                                                M=np.random.uniform(0, 2*np.pi))
    sim.add(m = mass[3] , P = P[3] , e = e0[3], inc = np.random.rand()*2*np.pi/180  , 
                                                Omega=np.random.uniform(0, 2*np.pi), 
                                                omega=np.random.uniform(0, 2*np.pi), 
                                                M=np.random.uniform(0, 2*np.pi))


    # Add planets via orbital elements
    
    sim.move_to_com()  # move to center-of-momentum frame

    print("Integrator:", sim.integrator, "\ndt:", sim.dt, "(yr) \nTotal integration time:", T_total, "yr")

    times = np.linspace(0,T_total,n_points+1)
    a = np.zeros([4,n_points+1])
    e = np.zeros([4,n_points+1])
    n = np.zeros([4,n_points+1])
    l = np.zeros([4,n_points+1])
    w = np.zeros([4,n_points+1])
    Omega = np.zeros([4,n_points+1])

    for i,time in enumerate(times):
        sim.integrate(time)#, exact_finish_time=0)
        orbits = sim.orbits(primary=sim.particles[0])
        
        for p, orbit in enumerate(orbits):
            a[p,i] = orbit.a
            e[p,i] = orbit.e
            n[p,i] = orbit.n
            l[p,i] = orbit.l
            w[p,i] = orbit.pomega
            Omega[p,i] = orbit.Omega

    return times , a , e, n, l, w, Omega
   