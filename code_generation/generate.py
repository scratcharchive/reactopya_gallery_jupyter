#!/usr/bin/env python

import os
import json

def main():
    dirname = os.path.dirname(os.path.abspath(__file__))

    ################################################################################################################
    config = dict()
    config['moduleName'] = 'reactopya_gallery_jupyter'
    config['moduleVersion'] = '0.1.0'
    config['widgets'] = _load_widgets_config(os.path.join(dirname, '..', 'reactopya_gallery', 'reactopya_gallery'))
    all_widgets_js_output_fname = os.path.join(dirname, '..', 'lib', 'all_widgets.js')
    all_widgets_py_output_fname = os.path.join(dirname, '..', 'reactopya_gallery_jupyter', 'all_widgets.py')
    ################################################################################################################

    print('Reading code templates...')
    with open(os.path.join(dirname, 'all_widgets.template.py'), 'r') as f:
        all_widgets_template_py = f.read()

    with open(os.path.join(dirname, 'widget_class.template.py'), 'r') as f:
        widget_class_template_py = f.read()

    with open(os.path.join(dirname, 'all_widgets.template.js'), 'r') as f:
        all_widgets_template_js = f.read()

    with open(os.path.join(dirname, 'widget_class.template.js'), 'r') as f:
        widget_class_template_js = f.read()

    ##################################################################################################################
    ## all_widgets.py
    imports = []
    for W in config['widgets']:
        imports.append('from {} import {} as {}Orig'.format(W['pythonModuleName'], W['pythonComponentName'], W['pythonComponentName']))
    all_widgets_template_py = all_widgets_template_py.replace('{imports}', '\n'.join(imports))

    widget_classes = []
    for W in config['widgets']:
        txt = widget_class_template_py
        txt = txt.replace('{ClassName}', W['pythonComponentName'])
        txt = txt.replace('{Description}', W['description'])
        txt = txt.replace('{ModuleName}', config['moduleName'])
        txt = txt.replace('{ModuleVersion}', config['moduleVersion'])

        python_state_variables = []
        for a in W['pythonStateKeys']:
            python_state_variables.append("    {} = Unicode('').tag(sync=True)".format(a))
        txt = txt.replace('{python_state_variables}', '\n'.join(python_state_variables))

        javascript_state_variables = []
        for a in W['javaScriptStateKeys']:
            javascript_state_variables.append("    {} = Unicode('').tag(sync=True)".format(a))
        txt = txt.replace('{javascript_state_variables}', '\n'.join(javascript_state_variables))

        python_state_variable_list = ', '.join(["'{}'".format(a) for a in W['pythonStateKeys']])
        txt = txt.replace('{python_state_variable_list}', python_state_variable_list)

        javascript_state_variable_list = ', '.join(["'{}'".format(a) for a in W['javaScriptStateKeys']])
        txt = txt.replace('{javascript_state_variable_list}', javascript_state_variable_list)

        widget_classes.append(txt)
    
    all_widgets_template_py = all_widgets_template_py.replace('{widget_classes}', '\n\n'.join(widget_classes))

    _write_file(all_widgets_py_output_fname, all_widgets_template_py)

    ##################################################################################################################
    ## all_widgets.js

    imports = []
    import_template = "import { default as {ClassName} } from '../reactopya_gallery/reactopya_gallery/{ClassName}/{ClassName}';"
    for W in config['widgets']:
        imports.append(import_template.replace('{ClassName}', W['pythonComponentName']))
    all_widgets_template_js = all_widgets_template_js.replace('{imports}', '\n'.join(imports))

    widget_classes = []
    for W in config['widgets']:
        txt = widget_class_template_js
        txt = txt.replace('{ClassName}', W['pythonComponentName'])
        txt = txt.replace('{ModuleName}', config['moduleName'])
        txt = txt.replace('{ModuleVersion}', config['moduleVersion'])

        python_state_defaults = []
        for a in W['pythonStateKeys']:
            python_state_defaults.append("        {}: ''".format(a))
        if W['javaScriptStateKeys'] and W['pythonStateKeys']:
            python_state_defaults[-1] = python_state_defaults[-1] + ',' # An extra comma separator is needed in this case!
        txt = txt.replace('{python_state_defaults}', ',\n'.join(python_state_defaults))

        
        
        javascript_state_defaults = []
        for a in W['javaScriptStateKeys']:
            javascript_state_defaults.append("        {}: ''".format(a))
        txt = txt.replace('{javascript_state_defaults}', ',\n'.join(javascript_state_defaults))

        widget_classes.append(txt)
    
    all_widgets_template_js = all_widgets_template_js.replace('{widget_classes}', '\n\n'.join(widget_classes))

    _write_file(all_widgets_js_output_fname, all_widgets_template_js)

def _load_widgets_config(basedir):
    widgets = []
    for name in os.listdir(basedir):
        if os.path.isdir(os.path.join(basedir, name)):
            fname = os.path.join(basedir, name, name + '.json')
            if os.path.exists(fname):
                print('Widget: {}'.format(name))
                with open(fname, 'r') as f:
                    obj = json.load(f)
                widgets.append(obj)
    return widgets



def _write_file(fname, txt):
    print('WRITING TO: {}'.format(fname))
    with open(fname, 'w') as f:
        f.write(txt)

if __name__ == '__main__':
    main()