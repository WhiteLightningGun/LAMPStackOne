function ToDoArea(todoProp) {
  const handleDeleteClick = () => {
    console.log(`delete clicked.. ${todoProp.todoProp[0]}`);
  };
  return (
    <li className="list-group-item">
      {todoProp.todoProp[1]}{" "}
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
