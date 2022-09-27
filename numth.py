import numpy as np
class Num_meth():
    """ my numeric methods"""
    def __init__(self, edo,dt = 0.005,ti = 0.0, tf = 10.0) -> None:
        self.edo = edo
        self.dt = dt
        self.ti = ti
        self.tf = tf
    def RK4(self,Y_i,graf = False,name = "datos.dat"):
        t = self.ti
        Y = Y_i.copy() #pos,vel
        #1d vectors with 3 zeros
        K1 = np.zeros(Y_i.size) 
        K2 = np.zeros(Y_i.size)
        K3 = np.zeros(Y_i.size)
        K4 = np.zeros(Y_i.size)
        #create a file 
        file = open(name, "w+")
        while(t < self.tf):
            #set values.

            #ki vel,ac:
            K1 = self.edo(Y,t)
            K2 = self.edo(Y + K1*(self.dt/2.0), t + self.dt/2.0)
            K3 = self.edo(Y + K2*(self.dt/2.0), t + self.dt/2.0)
            K4 = self.edo(Y + K3*(self.dt), t + self.dt)
            #make the step:
            Y = Y + (K1 + 2*K2 + 2*K3 + K4)*(1/6.0)*self.dt 
            if graf:
                #  add the step to file:
                file.write("{0} {1} {2} \n".format(t,Y[0],Y[1]))
            else:
                pass
            t += self.dt
        print(name)
        file.close()
        #return 0