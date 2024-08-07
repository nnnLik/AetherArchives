import { createSignal, createResource } from "solid-js";

export default function createUser(agent, actions, state, setState) {
  const [userId, setUserId] = createSignal();
  const [user] = createResource(userId, agent.User.get);

  Object.assign(actions, {
    loadUser: setUserId,
    async updateUser(newUser) {
      const { user, errors } = await agent.User.update(newUser);
      if (errors) throw errors;
      setState("user", user);
    }
  });

  return user;
}
