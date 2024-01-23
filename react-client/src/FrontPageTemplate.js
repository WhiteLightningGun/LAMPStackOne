import React, { useEffect, useState } from "react";
import { GetEntries } from "./ApiCallers";
import ToDoArea from "./ToDoArea";
import ToDoInput from "./ToDoInput";

function FrontPageTemplate() {
  const [todoList, setTodoList] = useState([]);
  useEffect(() => {
    GetEntries().then((data) => {
      setTodoList(data.entries);
    });
  }, []);
  return (
    <div className="App">
      <div>
        <div className="container">
          <h1 className="my-3">Todo List</h1>
          <ToDoInput />
          <ul className="list-group">
            {todoList.map((todo) => (
              <ToDoArea key={todo[0]} todoProp={todo} />
            ))}
          </ul>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
      </div>
    </div>
  );
}

export default FrontPageTemplate;
