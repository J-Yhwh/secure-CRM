// Copyright (c) 2026. Jac LL
// ALL Rights Reserved.
// All unauthorized use or distribution is prohibited.


import { useEffect, useState } from 'react';
import { api } from '../services/api';
import { useApi } from '../hooks/useApi';

interface Customer {
  id: number;
  name: string;
  email: string;
}

export const Customers = () => {
  const [customers, setCustomers] = useState<Customer[]>([]);
  const { call, loading } = useApi();

  useEffect(() => {
    call(() => api.get('/customers')).then(res => {
      if (res) setCustomers(res.data);
    });
  }, [call]);

  if (loading) return <p>Loading…</p>;

  return (
    <div>
      <h2>Customers</h2>
      <ul>
        {customers.map(c => (
          <li key={c.id}>{c.name} — {c.email}</li>
        ))}
      </ul>
    </div>
  );
};
