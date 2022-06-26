import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from '../dashboard';
import Login from '../login';

function RootView() {
    const [token, setToken] = useState();

    if(!token) {
        return <Login setToken={setToken} />
    
    }

    return (
        <Router>
            <h1>Application</h1>
            <Routes>
                {/* <Route path="/" exact element={<Login />} /> */}
                <Route path="/dashboard" exact element={<Dashboard />} />
            </Routes>
        </Router>
    );
}

export default RootView;