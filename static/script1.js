window.onload = function () {
  var switched = false;
  var domSwitchMe = document.getElementById("switchme");
  setInterval(() => {
    if (switched) {
      domSwitchMe.className = "green-text";
      switched = false;
    } else {
      domSwitchMe.className = "red-text";
      switched = true;
    }
  }, 1000);
};
