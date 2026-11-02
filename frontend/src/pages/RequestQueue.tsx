// Copyright (c) 2026. Jac LL
// ALL Rights Reserved.
// All unauthorized use or distribution is prohibited.


import { useEffect, useState } from 'react';
import { api } from '../services/api';
import { useApi } from '../hooks/useApi';

interface RequestItem {
  id: number;
  action: string;
  status: string;
  created_by: string;
}

export const RequestQueue = () => {
  const [items, setItems] = useState<RequestItem[]>([]);
  const { call, loading } = useApi();

  useEffect(() => {
    call(() => api.get('/requests/pending')).then(res => {
      if (res) setItems(res.data);
    });
  }, [call]);

  const decide = async (id: number, approve: boolean) => {
    await call(() => api.post(`/requests/${id}/${approve ? 'approve' : 'reject'}`));
    setItems(prev => prev.filter(i => i.id !== id));
  };

  if (loading) return <p>Loading…</p>;

  return (
    <div>
      <h2>Pending Approvals</h2>
      {items.map(item => (
        <div key={item.id}>
          <span>{item.action} by {item.created_by}</span>
          <button onClick={() => decide(item.id, true)}>Approve</button>
          <button onClick={() => decide(item.id, false)}>Reject</button>
        </div>
      ))}
      {items.length === 0 && <p>No pending requests</p>}
    </div>
  );
};
