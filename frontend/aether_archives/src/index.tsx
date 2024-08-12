import { render } from 'solid-js/web';
import { Provider } from './store/Provider';
import App from './App';
import './index.css';
import {Router} from "@solidjs/router";

const root = document.getElementById('root');

render(() => (
    <Provider>
      <Router root={App} />
    </Provider>
), root!);
