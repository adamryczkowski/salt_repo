try:
    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gio, Gtk, GLib
    HAS_GTK = True
except ImportError:
    HAS_GTK = False


def __virtual__():
    '''
    only load if GTK is available
    '''
    if HAS_GTK:
        return True
    else:
        return False, 'The GSettings execution module cannot be loaded: GTK is unavailable.'



__author__ = "Adam Ryczkowski"
__credits__ = "Adam Ryczkowski"
__maintainer__ = "Adam Ryczkowski"
__email__ = "adam _at_ statystyka _dot_ net"



def get_single_value(schema: str, key: str):
    gsettings = Gio.Settings.new(schema)
    return(gsettings.get_value(key).unpack())

def does_value_exist(schema: str, key: str, value):
    gsettings = Gio.Settings.new(schema)
    return(gsettings.get_value(key).unpack() == value)

def set_value(schema: str, key: str, value):
    gsettings = Gio.Settings.new(schema)
    type_str = gsettings.get_default_value(key).get_type_string()
    new_val = GLib.Variant(type_str, value)
    gsettings.set_value(key, new_val)

def is_list_item_present(schema: str, key: str, value):
    current = get_single_value(schema, key)
    return(value in current)

def is_list_item_absent(schema: str, key: str, value):
    current = get_single_value(schema, key)
    return (not value in current)

def append_list_item(schema: str, key: str, value):
    current = get_single_value(schema, key)
    if(not value in current):
        current.append(value)
        set_value(schema, key, current)

def remove_list_item(schema: str, key: str, value):
    current = get_single_value(schema, key)
    if(value in current):
        current.remove(value)
        set_value(schema, key, current)

