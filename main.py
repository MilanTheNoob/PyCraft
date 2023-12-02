from settings import *
from shader_program import ShaderProgram
from scene import Scene

import moderngl as mgl
import pygame as pg 
import sys 

class PyCraft:
    def __init__(self): # Called when created
        pg.init()

        # Set general data
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

        # Create the window
        pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()

        # Garbage Collection & Misc Settings
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = 'auto'

        # Clock to monitor the game as it runs
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        self.is_running = True
        self.on_init()

    def on_init(self):
        self.shader_program = ShaderProgram(self)
        self.scene = Scene(self)

    def update(self): # Called like Update & FixedUpdate in Unity
        self.shader_program.update()
        self.scene.update()

        self.delta_time = self.clock.tick() # Update time values
        self.time = pg.time.get_ticks() * 0.001

        pg.display.set_caption(f'{self.clock.get_fps() : .0f}') # Show FPS in title bar

    def render(self):
        self.ctx.clear() # Clear current buffer
        self.scene.render()
        pg.display.flip() # Render new frame

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

    def run(self): # Actually calling all the functions
        while self.is_running: # Keep playing the game until an event quits it
            self.handle_events()
            self.update()
            self.render()

        # Exit
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    app = PyCraft()
    app.run()