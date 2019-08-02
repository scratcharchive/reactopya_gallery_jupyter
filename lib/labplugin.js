var plugin = require('./index');
var base = require('@jupyter-widgets/base');

module.exports = {
  id: 'reactopya_gallery_jupyter',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
    // TODO: finish this
    //   widgets.registerWidget({
    //       name: 'mountainbrowser',
    //       version: plugin.version,
    //       exports: plugin
    //   });
  },
  autoStart: true
};

