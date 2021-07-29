document.addEventListener("DOMContentLoaded", function() {
    load_navpane();
});


// This function is a total hack to automatically expand the "Structures" navigation tab when on the home page.
// It bakes in some html details, and thus is likely to break with changes and updates
function load_navpane() {

    // Do nothing if in a mobile view. Doesn't work with that style of navigation.
    var width = window.innerWidth;
    if (width <= 1220) {
        return;
    }

    // First, test if we are on the home page.
    // We need a /py/ because python docs are hosted a polyscope.run/py (will not work in test serving)
    var pathname = window.location.pathname;
    var isOnHomePage = (pathname == "/py/")
  
    // If we are on the home page, find the nav element for "Structures" 
    // (which we happen to know will be "nav-6") and click it.
    if(isOnHomePage) {

      // Now go click the element
      var nav = document.getElementsByClassName("md-nav__link");
      for(var i = 0; i < nav.length; i++) {
          if (nav.item(i).htmlFor === "nav-6") {
              nav.item(i).click();
          }
      }
    }
}
