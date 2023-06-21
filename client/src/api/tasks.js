import axios from "axios";

const url = "http://localhost:8000/api/tasks";

export const fetchTasks = () => axios.get(url);

export const fetchTask = (id) => axios.get(`${url}/${id}`);

export const createTask = (task) => axios.post(url, task);

export const updateTask = (id, task) => axios.put(`${url}/${id}`, task);

export const deleteTask = (id) => axios.delete(`${url}/${id}`);