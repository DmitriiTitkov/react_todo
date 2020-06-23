const path = require("path");

module.exports = {
  mode: process.env.NODE_ENV || 'development',
  entry: [path.join(__dirname, 'todo_react/frontend/src/index.js')],
  output: {
    path: path.join(__dirname, 'todo_react/frontend/static'),
    filename: 'app.js'
  },
  resolve: {
    alias: {
      '~': path.join(__dirname, 'frontend/src')
    }
  },
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: [
          {
            loader: 'style-loader',
            options: { injectType: 'singletonStyleTag' }
          },
          'css-loader'
        ],
      },
      {
        test: /\.less$/i,
        use: [
          {
            loader: 'style-loader',
            options: { injectType: 'singletonStyleTag' }
          },
          'css-loader',
          'less-loader'
        ],
      },
      {
        test: /\.js$/,
        use: {
          loader: "babel-loader",
          options: {
            presets: [
              "@babel/preset-env",
              "@babel/preset-react"
            ],
            plugins: [
              "@babel/plugin-proposal-class-properties",
              ["@babel/plugin-proposal-decorators", { "decoratorsBeforeExport": true }],
              ["react-remove-properties", { "properties": ["data-test"] }]
            ],
          }
        },
      }]
  },
  optimization: {
    splitChunks: {
      chunks: 'async',
      maxInitialRequests: Infinity,
      minSize: 0,
      name(module) {
        // get the name. E.g. node_modules/packageName/not/this/part.js
        // or node_modules/packageName
        const packageName = module.context.match(/[\\/]node_modules[\\/](.*?)([\\/]|$)/)[1];

        // npm package names are URL-safe, but some servers don't like @ symbols
        return `npm.${packageName.replace('@', '')}`;
      },
      cacheGroups: {
        vendor: {
          test: /node_modules/,
        }
      }
    }
  }
};
