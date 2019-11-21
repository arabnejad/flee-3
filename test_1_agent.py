import flee.flee as flee
import datamanager.handle_refugee_data as handle_refugee_data
import numpy as np
import outputanalysis.analysis as a

"""
Generation 1 code. Incorporates only distance, travel always takes one day.
"""

if __name__ == "__main__":
  print("Testing basic data handling and simulation kernel.")

  flee.SimulationSettings.MinMoveSpeed=5000.0
  flee.SimulationSettings.MaxMoveSpeed=5000.0

  end_time = 10
  e = flee.Ecosystem()

  l1 = e.addLocation("A", movechance=0.3)

  l2 = e.addLocation("B", movechance=0.0)
  l3 = e.addLocation("C", movechance=0.0)
  l4 = e.addLocation("D", movechance=0.0)

  e.linkUp("A","B","834.0")
  e.linkUp("A","C","1368.0")
  e.linkUp("A","D","536.0")

  d = handle_refugee_data.RefugeeTable(csvformat="generic", data_directory="test_data", start_date="2010-01-01", data_layout="data_layout.csv")
  
  new_refs = 1

  # Insert refugee agents
  for i in range(0, new_refs):
    e.addAgent(location=l1)

  for t in range(0,end_time):

    # Propagate the model by one time step.
    e.evolve()

    print(t, l1.numAgents+l2.numAgents+l3.numAgents+l4.numAgents, l1.numAgents, l2.numAgents, l3.numAgents, l4.numAgents)


  assert t==9
  assert l1.numAgents+l2.numAgents+l3.numAgents+l4.numAgents==1 

  print("Test successful!")

