import { Component, createSignal } from 'solid-js';
import { useNavigate } from '@solidjs/router';
import style from './RegisterPage.module.css';
import {useStore} from "../../store/Provider";

const RegisterPage: Component = () => {
    const [username, setUsername] = createSignal('');
    const [email, setEmail] = createSignal('');
    const [password, setPassword] = createSignal('');
    const [passwordConfirm, setPasswordConfirm] = createSignal('');
    const [state, actions] = useStore();
    const navigate = useNavigate();

    const handleLogin = async (e: Event) => {
        e.preventDefault();

        try {
            await actions.login(email(), password()); // TODO: implement register
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
                    type="text"
                    name="username"
                    placeholder="Username"
                    value={username()}
                    onInput={(e) => setUsername(e.currentTarget.value)}
                    required
                />
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
                <input
                    type="password"
                    name="passwordConf"
                    placeholder="Confirm password"
                    value={passwordConfirm()}
                    onInput={(e) => setPasswordConfirm(e.currentTarget.value)}
                    required
                />
                <button type="submit">Login</button>
            </form>
            <div className="separator"></div>
            <div className="register-link">
                <p>Do you already have an account?<a href="/login">Sign in</a></p>
            </div>
        </div>
    );
};

export default RegisterPage;
