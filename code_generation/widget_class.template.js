export class {ClassName}Model extends widgets.DOMWidgetModel {
    defaults = _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        _model_name : '{ClassName}Model',
        _view_name : '{ClassName}View',
        _model_module : '{ModuleName}',
        _view_module : '{ModuleName}',
        _model_module_version : '{ModuleVersion}',
        _view_module_version : '{ModuleVersion}',

        // Python state
{python_state_defaults}

        // JavaScript state
{javascript_state_defaults}        

    })
}


// Custom View. Renders the widget model.
export class {ClassName}View extends widgets.DOMWidgetView {
    render() {
        this.div=document.createElement('div');
        this.el.appendChild(this.div);

        ReactDOM.render(
            <{ClassName} jupyterModel={this.model} />,
            this.div
        );
    }
}