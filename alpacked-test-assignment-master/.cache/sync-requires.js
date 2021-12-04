const { hot } = require("react-hot-loader/root")

// prefer default export if available
const preferDefault = m => m && m.default || m


exports.components = {
  "component---cache-dev-404-page-js": hot(preferDefault(require("/home/yehor/Alpacka/static-website/alpacked-test-assignment-master/.cache/dev-404-page.js"))),
  "component---src-pages-404-js": hot(preferDefault(require("/home/yehor/Alpacka/static-website/alpacked-test-assignment-master/src/pages/404.js"))),
  "component---src-pages-about-js": hot(preferDefault(require("/home/yehor/Alpacka/static-website/alpacked-test-assignment-master/src/pages/about.js"))),
  "component---src-pages-index-js": hot(preferDefault(require("/home/yehor/Alpacka/static-website/alpacked-test-assignment-master/src/pages/index.js"))),
  "component---src-templates-portfolio-item-jsx": hot(preferDefault(require("/home/yehor/Alpacka/static-website/alpacked-test-assignment-master/src/templates/portfolio-item.jsx")))
}

