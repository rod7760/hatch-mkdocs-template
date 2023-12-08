from hatchling.plugin import hookimpl

from .plugin import MkdocsTemplate

@hookimpl
def hatch_register_template():
    print("Registering!")
    return MkdocsTemplate
