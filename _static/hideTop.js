(function () {
  if (typeof window === "undefined" || typeof document === "undefined") return;

  function hideTopHeader() {
    try {
      // candidate selectors for the top header used by various themes
      var selectors = [
        "#navbar-main",
        "header.bd-header",
        "header.pydata-navbar",
        "header.navbar",
        "header",
        ".pydata-navbar",
        ".navbar",
        ".bd-header",
        "pst-secondary-sidebar",
      ];

      // collect unique elements
      var candidates = [];
      selectors.forEach(function (sel) {
        var els = document.querySelectorAll(sel);
        els.forEach(function (el) {
          if (candidates.indexOf(el) === -1) candidates.push(el);
        });
      });

      // hide only elements at the very top of the page (avoid sidebars)
      candidates.forEach(function (el) {
        try {
          // skip element if it contains the class navbar-expand-lg
          // if (el.classList.contains("navbar-expand-lg")) return;
          var rect = el.getBoundingClientRect();
          if (rect && rect.top <= 10) {
            // avoid writing inline styles; add a class and control hiding from CSS
            el.classList.add("easier-hidden-top");
          }
        } catch (e) {
          // ignore per-element errors
        }
      });
    } catch (e) {
      console.warn("hideTop: error hiding top header", e);
    }
  }

  function removeBdHeaderArticles() {
    try {
      // remove any bd-header-article elements inside the main content
      var elems = document.querySelectorAll(".bd-header-article");
      elems.forEach(function (el) {
        // ensure we only remove header-like blocks (safety: check size or parent)
        try {
          el.remove();
        } catch (e) {
          // ignore removal errors
        }
      });
    } catch (e) {
      console.warn("hideTop: error removing bd-header-article elements", e);
    }
  }

  function removeSecondarySidebarOnHome() {
    try {
      var path = (window.location && window.location.pathname) || "/";
      // consider site root variants as home
      var isHome = path === "/" || path === "" || path.endsWith("/index.html");
      if (!isHome) return;

      // id used in markup: pst-secondary-sidebar
      var el =
        document.getElementById("pst-secondary-sidebar") ||
        document.querySelector(".pst-secondary-sidebar") ||
        document.querySelector("#pst-secondary-sidebar");
      if (el) {
        el.remove();
      }
    } catch (e) {
      console.warn("hideTop: error removing secondary sidebar on home", e);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      hideTopHeader();
      removeBdHeaderArticles();
      removeSecondarySidebarOnHome();
    });
  } else {
    hideTopHeader();
    removeBdHeaderArticles();
    removeSecondarySidebarOnHome();
  }

  window.addEventListener("resize", hideTopHeader);
})();
