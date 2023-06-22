import { useEffect, useState } from "react";
import TaskList from "../components/TaskList";
import { fetchTasks } from "../api/tasks";

function HomePage() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetchTasks()
      .then((res) => {
        setTasks(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  return <TaskList tasks={tasks} />;
}

export default HomePage;
