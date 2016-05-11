
from pythonforandroid.toolchain import CythonRecipe, shprint, current_directory, ArchARM
from pythonforandroid.logger import info
from os.path import exists, join
import sh
import glob


class KiventCoreRecipe(CythonRecipe):
    # version = 'stable'
    version = '2.2-dev'
    url = 'https://github.com/kivy/kivent/archive/{version}.zip'
    name = 'kivent'
    subdir = "modules/core"

    depends = ['kivy', 'setuptools']
    

    
#    def get_recipe_env(self, arch=None):
#        env = super(KiventCoreRecipe, self).get_recipe_env(arch)
#
#        # TODO: fix hardcoded path
#        # This is required to prevent issue with _io.so import.
#        hostpython = self.get_recipe('hostpython2', self.ctx)
#        env['PYTHONPATH'] = (
#            join(hostpython.get_build_dir(arch.arch), 'build',
#                 'lib.linux-x86_64-2.7') + ':' + env.get('PYTHONPATH', '')
#        )
#        return env

recipe = KiventCoreRecipe()
