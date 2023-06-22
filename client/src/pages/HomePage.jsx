import { useEffect, useState } from "react";
import TaskList from "../components/TaskList";
import { fetchTasks } from "../api/tasks";

function HomePage() {
  const [completedTasks, setCompletedTasks] = useState([]);
  const [pendingTasks, setPendingTasks] = useState([]);

  useEffect(() => {
    fetchTasks()
      .then((res) => {
        setCompletedTasks(res.data.filter((task) => task.completed));
        setPendingTasks(res.data.filter((task) => !task.completed));
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <>
      <h3 className="text-xl font-bold text-gray-400 mb-7">Pending Tasks</h3>
      <TaskList tasks={pendingTasks} />

      <h3 className="text-xl font-bold text-gray-400 mb-7">Completed Task</h3>
      <TaskList tasks={completedTasks} />
    </>
  );
}

export default HomePage;
