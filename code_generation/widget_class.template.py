@widgets.register
class {ClassName}(widgets.DOMWidget):
    """{Description}"""
    _view_name = Unicode('{ClassName}View').tag(sync=True)
    _model_name = Unicode('{ClassName}Model').tag(sync=True)
    _view_module = Unicode('{ModuleName}').tag(sync=True)
    _model_module = Unicode('{ModuleName}').tag(sync=True)
    _view_module_version = Unicode('^{ModuleVersion}').tag(sync=True)
    _model_module_version = Unicode('^{ModuleVersion}').tag(sync=True)

    # python state
{python_state_variables}

    # javascript state
{javascript_state_variables}

    def __init__(self):
        super().__init__()
        self._X = {ClassName}Orig()
        self._X.on_python_state_changed(self._handle_python_state_changed)
        self.observe(self._on_change)
        self._X.init_jupyter()

    def _handle_python_state_changed(self):
        for key in [{python_state_variable_list}]:
            val = self._X.get_python_state(key, None)
            self.set_trait(key, _json_stringify(val))

    def _on_change(self, change):
        if change.type == 'change':
            if change.name in [{javascript_state_variable_list}]:
                state0 = dict()
                state0[change.name] = _json_parse(change.new)
                self._X._handle_javascript_state_changed(state0)