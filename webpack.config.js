const path = require('path');

module.exports = {
  stats: 'errors-only',
  entry: './projects/js/main.jsx',
  output: {
    path: path.join(__dirname, '/projects/static/js/'),
    filename: 'bundle.js',
  },
  module: {
    loaders: [
      {
        // Test for js or jsx files
        test: /\.jsx?$/,
        loader: 'babel-loader',
        query: {
          // Convert ES6 syntax to ES5 for browser compatibility
          presets: ['env', 'react'],
        },
      },
      { 
        test: /\.css$/,
        loader: "style-loader!css-loader"
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx', '.css'],
  },
};
