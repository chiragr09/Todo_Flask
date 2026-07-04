import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {
  const [tasks, setTasks] = useState([])
  const [data, setdata] = useState({
    taskId: 0,
    taskname: "",
    completed: false,
  })
  const [formData, setFormData] = useState({
    taskId: 0,
    taskname: "",
  });

  const fetchTasks = () => {
    fetch("/tasks")
      .then((res) => res.json())
      .then((data) => {
        setTasks(data);
      })
      .catch((err) => console.error(err));
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const payload = {
      ...formData,
      taskId: Number(formData.taskId),
      completed: false,
    };
    try{
      const response = await axios.post('http://localhost:5000/tasks', payload, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      fetchTasks();
      setFormData({
        taskId: 0,
        taskname: "",
      })
      console.log(response.data);
    } catch (error) {
      console.error('error', error);
    }
  };

  const handleButtonSubmit = async (id) => {
    try{
      const response = await axios.patch(`http://localhost:5000/tasks/${id}`, { completed: true }, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      fetchTasks();
    } catch(error) {
      console.error('error', error);
    }
  };

  const handleDelete = async (id) => {
    try{
      const response = await axios.delete(`http://localhost:5000/tasks/${id}`, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      fetchTasks();
    } catch(err) {
      console.error('error', err);
    }
  };

  function IsTaskCompleted({ comp, taskid }) {
    if(comp) {
      return <p>Status: Completed</p>
    }
    return <input type="button" onClick={() => handleButtonSubmit(taskid)} value={"Mark completed"}/>
  }

  return (
    <>
        {tasks.length === 0 ? (
          <p>No tasks found.</p>
        ) : (
          tasks.map((task) => (
            <div key={task.taskId}>
              <p>ID: {task.taskId}</p>
              <p>Task: {task.taskname}</p>
              <IsTaskCompleted comp = {task.completed} taskid = {task.taskId}/>
              <input type="button" onClick={() => handleDelete(task.taskId)} value="Delete this task"/>
              <hr/>
            </div>
          ))
        )}
        <form onSubmit={handleSubmit} method="post">
          <label for="taskId">Task ID:</label><br/>
          <input
            type="number"
            id="taskId"
            name="taskId"
            value={formData.taskId}
            onChange={handleChange}
          /><br/>
          <label for="taskname">Task Name:</label><br/>
          <input
            type="text"
            id="taskname"
            name="taskname"
            value={formData.taskname}
            onChange={handleChange}
          /><br/>
          <input type="submit" value="Submit"/>
        </form>
    </>
  )
}

export default App
