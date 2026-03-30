
import { BrowserRouter as Router, Routes, Route, Link, NavLink } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';


function App() {
  return (
    <Router>
      <div className="container mt-4">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-4 rounded">
          <div className="container-fluid d-flex align-items-center">
            <img src={process.env.PUBLIC_URL + '/octofitapp-small.png'} alt="OctoFit Logo" className="octofit-logo me-2" />
            <Link className="navbar-brand fw-bold d-flex align-items-center" to="/">OctoFit Tracker</Link>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item"><NavLink className={({isActive}) => 'nav-link' + (isActive ? ' active' : '')} to="/activities">Activities</NavLink></li>
                <li className="nav-item"><NavLink className={({isActive}) => 'nav-link' + (isActive ? ' active' : '')} to="/leaderboard">Leaderboard</NavLink></li>
                <li className="nav-item"><NavLink className={({isActive}) => 'nav-link' + (isActive ? ' active' : '')} to="/teams">Teams</NavLink></li>
                <li className="nav-item"><NavLink className={({isActive}) => 'nav-link' + (isActive ? ' active' : '')} to="/users">Users</NavLink></li>
                <li className="nav-item"><NavLink className={({isActive}) => 'nav-link' + (isActive ? ' active' : '')} to="/workouts">Workouts</NavLink></li>
              </ul>
            </div>
          </div>
        </nav>
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={<div className="card p-4"><h2 className="display-5 mb-3">Welcome to OctoFit Tracker!</h2><p className="lead">Track your fitness activities, teams, and more.</p></div>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
