from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.install_dependencies")

default_task = "publish"

@init
def init (project):
    project.depends_on("plotly")
    project.build_depends_on("wordcloud")
    project.build_depends_on("matplotlib")
    project.build_depends_on("Pillow")
    project.build_depends_on("numpy")
    project.build_depends_on("scipy")

