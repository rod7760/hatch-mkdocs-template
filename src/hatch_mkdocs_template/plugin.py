from hatch.template.plugin.interface import TemplateInterface
from hatch.template import find_template_files
from . import file_templates
class MkdocsTemplate(TemplateInterface):
    PLUGIN_NAME = 'mkdocs-template'

    def get_files(self, config):
        return list(find_template_files(file_templates))

