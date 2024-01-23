function GetHello() {
  return fetch(`http://127.0.0.1:5000/api/hello`)
    .then((response) => response.text())
    .then((data) => {
      return data;
    });
}

function GetEntries() {
  return fetch(`http://127.0.0.1:5000/api/entries`)
    .then((response) => response.json())
    .then((data) => {
      return data;
    });
}

export { GetHello, GetEntries };

/*

function GetHello() {
  return fetch(`${window.location.origin}/api/hello`)
    .then((response) => response.json())
    .then((data) => {
      return data;
    });
}


*/
