// Copyright (c) 2026. Jac LL
// ALL Rights Reserved.
// All unauthorized use or distribution is prohibited.

import { useState, useCallback } from 'react';
import { api } from '../services/api';

export function useApi() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const call = useCallback(async <T>(fn: () => Promise<T>): Promise<T | null> => {
    setLoading(true);
    setError(null);
    try {
      const result = await fn();
      return result;
    } catch (e: any) {
      setError(e.response?.data?.detail || e.message);
      return null;
    } finally {
      setLoading(false);
    }
  }, []);

  return { loading, error, call };
}
