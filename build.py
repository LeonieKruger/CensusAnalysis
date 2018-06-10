from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.install_dependencies")

default_task = "publish"

@init
def initialize(project):
    project.build_depends_on('plotly','wordcloud')
    # project.build_depends_on('matplotlib')
    # project.build_depends_on('random')
    # project.build_depends_on('PIL')
    # project.build_depends_on('numpy')
    # project.build_depends_on('scipy')

# @init
# def initialize(project):
#     # Nothing happens here yet, but notice the `project` argument which is automatically injected.
#     pass
