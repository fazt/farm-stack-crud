import { useNavigate } from "react-router-dom";
import { updateTask } from "../api/tasks";

function TaskCard({ task }) {
  const navigate = useNavigate();

  return (
    <div
      className="bg-zinc-950 p-4 hover:cursor-pointer hover:bg-gray-950"
      onClick={() => {
        navigate(`/tasks/${task._id}`);
      }}
    >
      <div className="flex justify-between">
        <h1 className="font-bold text-2xl">{task.title}</h1>
        <button
          onClick={async (e) => {
            e.stopPropagation();
            const res = await updateTask(task._id, {
              completed: !task.completed,
            });
            if (res.status === 200) {
              window.location.reload();
            }
          }}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.5"
            className={`w-6 h-6 ${task.completed ? "text-green-500" : ""}`}
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M4.5 12.75l6 6 9-13.5"
            ></path>
          </svg>
        </button>
      </div>

      <p className="text-slate-400">{task.description}</p>
    </div>
  );
}

export default TaskCard;
