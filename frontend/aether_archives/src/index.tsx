import { render } from 'solid-js/web';
import { Provider } from './store/Provider';
import App from './App';
import './index.css';

const root = document.getElementById('root');

render(
  () => (
    <Provider>
      <App />
    </Provider>
  ),
  root!
);
