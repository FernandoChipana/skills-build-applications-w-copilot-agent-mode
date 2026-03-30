import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const url = codespace
    ? `https://${codespace}-8000.app.github.dev/api/workouts/`
    : 'http://localhost:8000/api/workouts/';
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch(url)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results);
        console.log('Workouts endpoint:', url);
        console.log('Fetched workouts:', results);
      });
  }, [url]);

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title display-6 mb-4">Workouts</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead className="table-dark">
              <tr>
                <th>#</th>
                <th>Name</th>
                <th>Description</th>
                <th>Difficulty</th>
              </tr>
            </thead>
            <tbody>
              {workouts.map((w, i) => (
                <tr key={i}>
                  <td>{i + 1}</td>
                  <td>{w.name}</td>
                  <td>{w.description}</td>
                  <td>{w.difficulty}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
export default Workouts;
