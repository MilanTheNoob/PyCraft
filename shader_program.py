from settings import *

class ShaderProgram:
    def __init__(self, app):
        self.app = app 
        self.ctx = app.ctx

        self.quad = self.get_program(shader_name='quad') # The stored shader
        self.set_uniforms_on_init() # Update them

    def set_uniforms_on_init(self):
        pass 

    def update(self):
        pass 

    def get_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()
        
        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        return self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        