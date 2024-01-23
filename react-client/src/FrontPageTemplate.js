import React, { useEffect, useState } from "react";
import { GetEntries, PostDelete } from "./ApiCallers";
import ToDoArea from "./ToDoArea";
import ToDoInput from "./ToDoInput";

function FrontPageTemplate() {
  const [todoList, setTodoList] = useState([]);
  useEffect(() => {
    GetEntries().then((data) => {
      setTodoList(data.entries);
    });
  }, []);

  const removeToDo = async (id) => {
    //setTodoList(todoList.filter((todo) => todo[0] !== id));
    //create api call here
    const res = await PostDelete(id);
    if (res.message === "New todo deleted") {
      alert("Successfully removed todo");
      refreshToDos();
    } else {
      alert("Failed to add todo");
    }
  };

  const refreshToDos = () => {
    GetEntries().then((data) => {
      setTodoList(data.entries);
    });
  };
  return (
    <div className="App">
      <div>
        <div className="container">
          <h1 className="my-3">Todo List</h1>
          <ToDoInput refreshToDos={refreshToDos} />
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
