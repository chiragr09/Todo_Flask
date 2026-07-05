import { useState, useEffect } from 'react'
import axios from 'axios'
import { styles } from "./styles"

function App() {
  const [tasks, setTasks] = useState([])
  const [data, setdata] = useState({
    taskname: "",
    completed: false,
  })
  const [formData, setFormData] = useState({
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
    console.log("deleting:", id);
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
      return <>Completed</>
    }
    return <input
              type="button"
              style={styles.buttonStyle}
              onClick={() => handleButtonSubmit(taskid)}
              value={"Mark completed"}
            />
  }

  return (
    <>
    <div style={styles.container}>
      <div style={styles.header_cont}>
        <h1 style={styles.header}>To-do application</h1>
        <p style={styles.description}>Add your tasks, and mark them once completed!</p>
      </div>
      <table>
        <thead style={styles.tableHeader}>
          <tr>
            <th>Task</th>
            <th>Progress</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody style={styles.tableContent}>
          {tasks.length===0 ? (
            <tr>
              <td colSpan="4">No tasks found!</td>
            </tr>
          ) : (
            tasks.map((task) => (
              <tr>
                <td>{task.taskname}</td>
                <td>
                  <IsTaskCompleted
                    comp={task.completed}
                    taskid={task._id}
                  />
                </td>
                <td>
                  <input
                    type="button"
                    value="Delete Task"
                    style={styles.buttonStyle}
                    onClick={() => handleDelete(task._id)}
                  />
                </td>
              </tr>
            )))}
        </tbody>
      </table>
      <div style={styles.header}>
        <h2>Add a new task!</h2>
        <form onSubmit={handleSubmit} method="post">
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
      </div>
    </div>
    </>
  )
}

export default App
