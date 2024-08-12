import { Component, createSignal } from 'solid-js';
import { useNavigate } from '@solidjs/router';
import style from './LoginPage.module.css';
import {useStore} from "../../store/Provider";

const LoginPage: Component = () => {
    const [email, setEmail] = createSignal('');
    const [password, setPassword] = createSignal('');
    const [state, actions] = useStore();
    const navigate = useNavigate();

    const handleLogin = async (e: Event) => {
        e.preventDefault();

        try {
            await actions.login(email(), password());
            navigate('/profile');
        } catch (err) {
            console.error('Login failed:', err);
        }
    };

    return (
        <div className={style['centered-container']}>
            <h2>Login</h2>
            <form onSubmit={handleLogin}>
                <input
                    type="email"
                    name="email"
                    placeholder="Email"
                    value={email()}
                    onInput={(e) => setEmail(e.currentTarget.value)}
                    required
                />
                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    value={password()}
                    onInput={(e) => setPassword(e.currentTarget.value)}
                    required
                />
                <button type="submit">Login</button>
            </form>
            <div className="separator"></div>
            <div className="register-link">
                <p>Don't have an account? <a href="/register">Sign up</a></p>
            </div>
        </div>
    );
};

export default LoginPage;
