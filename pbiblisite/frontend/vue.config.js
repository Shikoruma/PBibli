module.exports = {
  publicPath: "/static/",
  configureWebpack: {
    optimization: {
      splitChunks: {
        minSize: 10000,
        maxSize: 250000,
        chunks: "all"
      }
    }
  },
  chainWebpack: config => {
    config.plugins.delete("prefetch");
  }
};
