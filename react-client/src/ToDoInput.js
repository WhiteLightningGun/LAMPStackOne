import React from "react";
import { useForm } from "react-hook-form";

function ToDoInput() {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
    reset();
  };
  return (
    <div className="input-group mb-3">
      <form onSubmit={handleSubmit(onSubmit)} className="col">
        <input
          type="text"
          className="form-control"
          {...register("todoInput")}
        />

        <button className="btn btn-primary" type="submit">
          Add
        </button>
      </form>
    </div>
  );
}

export default ToDoInput;
