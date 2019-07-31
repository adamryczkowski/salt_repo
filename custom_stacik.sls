custom_stacik:
  my_custom_state:              # The custom state module name.
    - enforce_custom_thing      # The function in the custom state module.
    - name: a_value             # Maps to the ``name`` parameter in the custom function.
    - foo: Foo                  # Specify the required ``foo`` parameter.
    - bar: False                # Override the default value for the ``bar`` parameter.

