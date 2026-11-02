#  Copyright (c) 2026. Jac LL
#  ALL Rights Reserved.
#  All unauthorized use or distribution is prohibited.


# ---------- build stage ----------
FROM node:20-alpine AS build

WORKDIR /app

# install deps first (better layer caching)
COPY package.json package-lock.json* ./
RUN npm ci

# copy source and build
COPY . .
RUN npm run build

# ---------- production stage ----------
FROM nginx:alpine

# copy the built static files
COPY --from=build /app/dist /usr/share/nginx/html

# optional: custom nginx config if you need SPA routing or API proxying
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
