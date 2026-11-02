// Copyright (c) 2026. Jac LL
// ALL Rights Reserved.
// All unauthorized use or distribution is prohibited.


import { useAuth } from '../hooks/useAuth';
import { RoleGuard } from '../components/RoleGuard';

export const Dashboard = () => {
  const { user, logout } = useAuth();

  return (
    <div>
      <h1>Welcome, {user?.username}</h1>
      <p>Roles: {user?.roles.join(', ')}</p>
      <button onClick={logout}>Logout</button>

      <RoleGuard roles={['maker']}>
        <a href="/customers">Manage Customers</a>
      </RoleGuard>
      <RoleGuard roles={['checker']}>
        <a href="/queue">Approval Queue</a>
      </RoleGuard>
    </div>
  );
};
