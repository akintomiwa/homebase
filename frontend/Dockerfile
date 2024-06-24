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

# //

# Use an official Node.js runtime as a parent image
FROM node:16-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
# COPY package*.json ./
COPY package.json ./
COPY package-lock.json ./

# Install dependencies
RUN npm install

# Copy the remaining application code to the working directory
COPY . .

# Build the React app for production
RUN npm run build

# Set the command to run your production build
CMD ["npm", "start"]