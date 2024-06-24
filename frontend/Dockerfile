# frontend/Dockerfile

FROM node:20

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . /app/

# CMD ["npm", "start"]

# Build the React app
RUN npm run build

# Expose port and start application
EXPOSE 3000
CMD ["npm", "start"]