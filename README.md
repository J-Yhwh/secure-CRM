## Secure-CRM-Fullstack
**A fullstack web application using React, FastAPI, and MariaDB. Includes Session Management, RBAC, and additional security perimeters like maker-checker approval workflow.**

```
secure-customer-system/
├── .github/                # GitHub Actions for CI/CD (optional)
├── backend/                # Python FastAPI project
│   ├── app/
│   │   ├── main.py         # Entry point
│   │   ├── api/            # Route handlers (auth, customers, requests)
│   │   ├── core/           # Security, JWT, config
│   │   ├── db/             # MariaDB connection and models
│   │   └── schemas/        # Pydantic models for validation
│   ├── tests/              # Pytest suite
│   ├── .env.example        # Template for DB_URL, SECRET_KEY
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Backend containerization
├── frontend/               # React TypeScript project
│   ├── src/
│   │   ├── components/     # Reusable UI (Buttons, Inputs, RoleGuard)
│   │   ├── context/        # AuthContext, State management
│   │   ├── hooks/          # useAuth, useApi
│   │   ├── pages/          # Login, Dashboard, RequestQueue
│   │   └── services/       # API call definitions (Axios)
│   ├── public/
│   ├── package.json
│   ├── tsconfig.json
│   └── Dockerfile          # Frontend containerization
├── docker-compose.yml      # Orchestrates Backend, Frontend, and MariaDB
├── .gitignore              # Ignore node_modules, __pycache__, .env
└── README.md               # Project documentation
```

<img width="1340" height="2030" alt="Maker-checker-approval-root-2" src="https://github.com/user-attachments/assets/c0c307e3-9ffe-4f55-915d-645a5002b27c" />

