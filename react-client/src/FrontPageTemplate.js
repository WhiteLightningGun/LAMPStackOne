import React, { useEffect, useState } from "react";
import io from "socket.io-client";
import { GetEntries, PostDelete, serverUrl } from "./ApiCallers";
import ToDoArea from "./ToDoArea";
import ToDoInput from "./ToDoInput";

function FrontPageTemplate() {
  const [todoList, setTodoList] = useState([]);
  useEffect(() => {
    GetEntries().then((data) => {
      setTodoList(data.entries);
    });
    console.log(`using serverUrl: ${serverUrl}`);
    const socket = io(serverUrl);
    socket.on("database_updated", (data) => {
      console.log("socket io reports database updated --");
      console.log(data);
      setTodoList(data.entries);
    });
    return () => socket.disconnect();
  }, []);

  const removeToDo = async (id) => {
    //setTodoList(todoList.filter((todo) => todo[0] !== id));
    //create api call here
    const res = await PostDelete(id);
    if (res.message === "New todo deleted") {
      alert("Successfully removed todo");
    } else {
      alert("Failed to add todo");
    }
  };

  return (
    <div className="App">
      <div>
        <div className="container">
          <h1 className="my-3">Todo List</h1>
          <ToDoInput />
          <ul className="list-group">
            {todoList.map((todo) => (
              <ToDoArea key={todo[0]} todoProp={todo} removeTodo={removeToDo} />
            ))}
          </ul>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
      </div>
    </div>
  );
}

export default FrontPageTemplate;
