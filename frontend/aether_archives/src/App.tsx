import type { Component } from 'solid-js';
import { createEffect } from "solid-js";
import { Route, Router, useNavigate } from '@solidjs/router';
import { useStore } from './store/Provider';
import LoginPage from "./pages/LoginPage/LoginPage";
import UserPage from "./pages/UserPage/UserPage";
import RegisterPage from "./pages/RegisterPage/RegisterPage";

const App: Component = () => {
    const [state, _] = useStore();
    const navigate = useNavigate();

    createEffect(() => {
        if (state.token) {
            if (window.location.pathname === '/login' || window.location.pathname === '/register') {
                navigate('/');
            }
        } else {
            if (window.location.pathname !== '/login' && window.location.pathname !== '/register') {
                navigate('/login');
            }
        }
    });

    return (
        <Router>
            <Route path="/" component={UserPage} />
            <Route path="/login" component={LoginPage} />
            <Route path="/register" component={RegisterPage} />
        </Router>
    );
};

export default App;
