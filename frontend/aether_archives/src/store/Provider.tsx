import { createContext, useContext, JSX } from "solid-js";
import { createStore, SetStoreFunction } from "solid-js/store";
import createAgent from "./createAgent";
import createAuth from "./createAuth";
import createUser from "./createUser";

type State = {
  user: any;
  token: string | null;
};

type Actions = {
  [key: string]: (...args: string[]) => any;
};

const StoreContext = createContext<[State, Actions]>();

export function Provider(props: { children: JSX.Element }): JSX.Element {
  let auth: any, user: any
  const [state, setState] = createStore<State>({
    get user() {
      return user();
    },
    get token() {
      return localStorage.getItem("access");
    }
  });

  const actions: Actions = {};
  const store: [State, Actions] = [state, actions];
  const agent = createAgent(store);

  auth = createAuth(agent, actions, setState as SetStoreFunction<State>);
  user = createUser(agent, actions, state, setState as SetStoreFunction<State>);  

  return (
    <StoreContext.Provider value={store}>
      {props.children}
    </StoreContext.Provider>
  );
}

export function useStore(): [State, Actions] {
  return useContext(StoreContext);
}
