//export let serverUrl = "http://127.0.0.1:5000";
export let serverUrl = window.location.href;

function GetHello() {
  return fetch(`${serverUrl}/api/hello`)
    .then((response) => response.text())
    .then((data) => {
      return data;
    });
}

function GetEntries() {
  return fetch(`${serverUrl}/api/entries`)
    .then((response) => response.json())
    .then((data) => {
      return data;
    });
}

async function PostTodo(todo) {
  const response = await fetch(`${serverUrl}/api/newtodo`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(todo),
  });

  // Await the JSON data from the response before returning
  const data = await response.json();
  return data;
}

async function PostDelete(todoID) {
  const response = await fetch(`${serverUrl}/api/deletetodo`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(todoID),
  });

  // Await the JSON data from the response before returning
  const data = await response.json();
  return data;
}

export { GetHello, GetEntries, PostTodo, PostDelete };
