import { createSignal, createResource, batch } from "solid-js";

export default function createAuth(agent, actions, setState) {
  const [loggedIn, setLoggedIn] = createSignal(false);
  const [currentUser, { mutate }] = createResource(loggedIn, agent.Auth.current);

  const setTokens = (access: string, refresh: string): void => {
    localStorage.setItem("access", access);
    localStorage.setItem("refresh", refresh);
    setState("token", access);
  };

  Object.assign(actions, {
    pullUser: () => setLoggedIn(true),
    async login(email: string, password: string) {
      const { access, refresh, errors } = await agent.Auth.login(email, password);
      if (errors) throw errors;
      setTokens(access, refresh);
      setLoggedIn(true);
    },
  });

  return currentUser;
}
