from hatch.template import File
from hatch.utils.fs import Path

class MkdocsYaml(File):
    TEMPLATE = """\
site_name: {project_name} Docs
nav:
    - Home: 'index.md'
theme: {theme}
"""
    def __init__(self, template_config: dict, plugin_config: dict):
        # defaults 
        theme = "readthedocs"

        if "theme" in plugin_config:
            theme = plugin_config["theme"]
        super().__init__(Path("mkdocs.yaml"), self.TEMPLATE.format(theme=theme,**template_config))

class IndexMd(File):
    TEMPLATE = """\
# {project_name}
{proj_description}

## Features 
- Awesome Feature!
"""
    def __init__(self, template_config: dict, plugin_config: dict):
        #defaults 
        proj_description = "This is a super cool project."

        if template_config["description"] != "":
            proj_description = template_config["description"]
        super().__init__(Path("docs/index.md"), self.TEMPLATE.format(proj_description=proj_description,**template_config))
