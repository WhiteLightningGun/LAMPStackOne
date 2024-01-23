import React from "react";
import { useForm } from "react-hook-form";
import { PostTodo } from "./ApiCallers";

function ToDoInput() {
  const { register, handleSubmit, reset } = useForm();

  const onSubmit = async (data) => {
    if (data.todoInput === "") {
      return;
    }
    const res = await PostTodo(data);
    if (res.message === "New todo created") {
      alert("Successfully added todo");
      reset();
    } else {
      alert("Failed to add todo");
    }
  };
  return (
    <div className="input-group mb-3">
      <form onSubmit={handleSubmit(onSubmit)} className="col">
        <input
          type="text"
          className="form-control"
          {...register("todoInput")}
        />

        <button className="btn btn-primary my-2" type="submit">
          Add
        </button>
      </form>
    </div>
  );
}

export default ToDoInput;
