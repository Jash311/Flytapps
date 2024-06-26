#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation class

# at least 3sec sleep time for the drone interface to initialize properly
time.sleep(5)

print 'taking off'
drone.take_off(5.0)

#tried these two commands to change the mode to Guided/Hold, but didn't work
#drone.access_request() 
#drone.position_hold() 

print ' going along the setpoints'
drone.position_set(6.5, 0, 0, tolerance=0.25, relative=True)
drone.position_set(0, 6.5, 0, tolerance=0.25, relative=True)
drone.position_set(-6.5, 0, 0, tolerance=0.25, relative=True)
drone.position_set(0, -6.5, 0, tolerance=0.25, relative=True)

print 'Landing'
drone.land(async=True) #true to force landing

# shutdown the instance
drone.disconnect()

