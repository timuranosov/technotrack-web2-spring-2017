const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const path = require('path');

const NODE_ENV = process.env.NODE_ENV || 'development';

module.exports = {
    entry: {
        app: './app.jsx',
        indexBundle: './index.jsx',
        testBundle: './test.jsx',
    },
    context: path.resolve(__dirname, './static_src'),
    output: {
        filename: '[name]-[hash].js',
        path: path.resolve(path.dirname(__dirname), './static'),
        publicPath: '../static/',
    },

    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                loader: 'babel-loader?presets[]=react&presets[]=es2015&presets[]=stage-0',
            }, {
                test: /\.css$/,
                loaders: ['style-loader', 'css-loader'],
            }, {
                test: /\.scss$/,
                loaders: ['style-loader', 'css-loader', 'sass-loader?sourceMap'],
            }, {
                test: /\.(png|jpg|gif|svg|ttf|eot|woff|woff2)$/,
                loader: 'url-loader?limit=4096',
            },
        ],
    },

    resolve: {
        modules: [
            path.resolve(__dirname, './static_src'),
            'node_modules',
        ],
        extensions: ['.js', '.jsx'],
    },

    resolveLoader: {
        modules: ['node_modules'],
        extensions: ['loader.js', '.js'],
    },

    watch: NODE_ENV === 'development',
    watchOptions: {
        aggregateTimeout: 100,
    },

    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
    ],

    devtool: NODE_ENV === 'development'
        ? 'cheap-module-eval-source-map'
        : 'cheap-module-inline-source-map',
};
