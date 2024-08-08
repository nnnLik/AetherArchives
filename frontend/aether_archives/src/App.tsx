import type { Component } from 'solid-js';
import { useStore } from './store/Provider';

const App: Component = () => {
  const [state, actions] = useStore();

  const handleLogin = async () => {
    try {
      await actions.login('a@a.com', 'admin');
    } catch (err) {
      console.error('Login failed:', err);
    }
  };

  return (
    <div>
      <h1>JWT Authentication with SolidJS</h1>
      {state.user ? (
        <div>
          <p>Welcome, {state.user.username}</p>
        </div>
      ) : (
        <button onClick={handleLogin}>Login</button>
      )}
    </div>
  );
};

export default App;
