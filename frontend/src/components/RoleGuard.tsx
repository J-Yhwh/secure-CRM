// Copyright (c) 2026. Jac LL
// ALL Rights Reserved.
// All unauthorized use or distribution is prohibited.


import { ReactNode } from 'react';
import { useAuth } from '../hooks/useAuth';

interface Props {
  roles: string[];
  children: ReactNode;
  fallback?: ReactNode;
}

export const RoleGuard = ({ roles, children, fallback = null }: Props) => {
  const { user } = useAuth();
  if (!user || !roles.some(r => user.roles.includes(r))) return <>{fallback}</>;
  return <>{children}</>;
};
