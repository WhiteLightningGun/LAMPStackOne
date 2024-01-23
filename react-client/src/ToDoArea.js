import React from "react";

function ToDoArea({ todoProp, removeTodo }) {
  const handleDeleteClick = () => {
    removeTodo(todoProp[0]);
  };
  return (
    <li className="list-group-item fs-4">
      {todoProp[1]}{" "}
      <button
        className="btn btn-sm btn-danger float-end"
        onClick={handleDeleteClick}
      >
        Delete
      </button>
    </li>
  );
}

export default ToDoArea;
