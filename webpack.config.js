var path = require('path');
var version = require('./package.json').version;

var rules = [
    {
        // JavaScript rules.
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
            loader: 'babel-loader',
            options: {
                presets: [
                    ["@babel/preset-env",
                        {
                            "targets": {
                                "chrome": "70"
                            }
                        }],
                    "@babel/preset-react"
                ],
                plugins: [
                    "@babel/plugin-proposal-class-properties"
                ]
            }
        }
    },
    {
        // CSS files
        test: /\.css$/,
        use: [
            { loader: 'style-loader' },
            { loader: 'css-loader' }
        ],
    },
    {
        // Some image formats so you can import images
        test: /\.(png|gif|jpg|svg)$/,
        use: {
            loader: 'url-loader',
            options: {
                limit: 50000,
            },
        },
    }
];

/*
The react alias below is needed because otherwise it could resolve to
the wrong one in a subdirectory. Then I get a react hooks error
because 2 different reacts are being used in the same app.
See:
https://reactjs.org/warnings/invalid-hook-call-warning.html
https://github.com/facebook/react/issues/13991
*/

const resolve = {
    extensions: ['.css', '.js', '.json', '.png', '.gif', '.jpg', '.svg'],
    alias: {
        'reactopya': __dirname + '/reactopya_gallery/reactopya/js',
        'react': __dirname + '/node_modules/react' // See above
    }
};


module.exports = [
    {// Notebook extension
        //
        // This bundle only contains the part of the JavaScript that is run on
        // load of the notebook. This section generally only performs
        // some configuration for requirejs, and provides the legacy
        // "load_ipython_extension" function which is required for any notebook
        // extension.
        //
        entry: ['./lib/extension.js'],
        output: {
            filename: 'extension.js',
            path: path.resolve(__dirname, 'reactopya_gallery_jupyter', 'static'),
            libraryTarget: 'amd'
        }
    },
    {// Bundle for the notebook containing the custom widget views and models
        //
        // This bundle contains the implementation for the custom widget views and
        // custom widget.
        // It must be an amd module
        //
        entry: ['./lib/index.js'],
        output: {
            filename: 'index.js',
            path: path.resolve(__dirname, 'reactopya_gallery_jupyter', 'static'),
            libraryTarget: 'amd'
        },
        devtool: 'source-map',
        module: {
            rules: rules
        },
        resolve: resolve,
        externals: ['@jupyter-widgets/base']
    },
    {// Embeddable bundle
        //
        // This bundle is generally almost identical to the notebook bundle
        // containing the custom widget views and models.
        //
        // The only difference is in the configuration of the webpack public path
        // for the static assets.
        //
        // It will be automatically distributed by unpkg to work with the static
        // widget embedder.
        //
        // The target bundle is always `dist/index.js`, which is the path required
        // by the custom widget embedder.
        //
        entry: ['./lib/embed.js'],
        output: {
            filename: 'index.js',
            path: path.resolve(__dirname, 'dist'),
            libraryTarget: 'amd',
            publicPath: 'https://unpkg.com/reactopya_gallery_jupyter@' + version + '/dist/'
        },
        devtool: 'source-map',
        module: {
            rules: rules
        },
        resolve: resolve,
        externals: ['@jupyter-widgets/base']
    }
];
