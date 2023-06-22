import TaskCard from "./TaskCard";

function TaskList({ tasks }) {
  return (
    <div className="grid grid-cols-3 gap-4">
      {tasks.map((task, i) => {
        return <TaskCard task={task} key={i} />;
      })}
    </div>
  );
}

export default TaskList;
