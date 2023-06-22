import { useNavigate } from "react-router-dom";

function TaskCard({ task }) {
  const navigate = useNavigate();

  return (
    <div
      className="bg-zinc-950 p-4 hover:cursor-pointer hover:bg-gray-950"
      onClick={() => {
        navigate(`/tasks/${task._id}`);
      }}
    >
      <h1 className="font-bold text-2xl">{task.title}</h1>
      <p className="text-slate-400">{task.description}</p>
    </div>
  );
}

export default TaskCard;
