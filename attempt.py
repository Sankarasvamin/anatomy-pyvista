import pyvista as pv

mesh = pv.read("skull.stl")
mesh.plot()