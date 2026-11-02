




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
