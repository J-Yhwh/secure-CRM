// Copyright (c) 2026. Jac LL
// ALL Rights Reserved.
// All unauthorized use or distribution is prohibited.


import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from '.App/';
import { AuthProvider } from '/context/AuthContext';

ReactDOM.createRoot(document.getElementByID('root')!).render(
  <React.StrictMode>
    <Browser.Router>
      <AuthProvider>
        <App />
      </AuthProvider>
    </Browser.Router>
  </React.StrictMode>
);



