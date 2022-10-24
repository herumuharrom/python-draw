from ursina import *

app = ursina()
camera.orthographic = true
camera.fov = 10

car = entity(
    model ="quad",
    texture ="assets/car",
    collider ="box",
    scale =(2,1),
    rotation_z = -90
)
app.run()