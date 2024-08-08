interface LoginResponse {
    access: string;
    refresh: string
}

export default function createAgent(store) {
    const [state] = store;

    const Auth = {
        login: async (email: string, password: string): Promise<LoginResponse> => {
            const response = await fetch('http://localhost:6969/api/auth/jwt/create/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, password }),
            });
            return await response.json();
        },
        current: async () => {
            const response = await fetch('http://localhost:6969/me', {
                headers: {
                    'Authorization': `Bearer ${state.token}`,
                },
            });
            return await response.json();
        }
    };

    const User = {
        get: async (id: number) => {
            const response = await fetch(`http://localhost:6969/users/${id}`, {
                headers: {
                    'Authorization': `Bearer ${state.token}`,
                },
            });
            return await response.json();
        },
        update: async (newUser) => {
            const response = await fetch('http://localhost:6969/users', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${state.token}`,
                },
                body: JSON.stringify(newUser),
            });
            return await response.json();
        }
    };

    return { Auth, User };
}
