// import React, { useEffect, useState } from 'react';
// import api from './api';

// interface Project {
//     id: number;
//     title: string;
//     description: string;
//     technology: string;
//     summary: string;
//     image: string;
//     url: string;
//     github: string;
// }

// const App: React.FC = () => {
//     const [projects, setProjects] = useState<Project[]>([]);

//     useEffect(() => {
//         const fetchProjects = async () => {
//             try {
//                 console.log('Fetching projects...');
//                 const response = await api.get<Project[]>('/projects/');
//                 console.log('Projects fetched:', response.data);
//                 setProjects(response.data);
//             } catch (error) {
//                 console.error('Error fetching projects:', error);
//             }
//         };

//         fetchProjects();
//     }, []);

//     console.log('Rendering projects:', projects);

//     return (
//         <div>
//             <h1>Projects</h1>
//             <ul>
//                 {projects.map(project => (
//                     <li key={project.id}>
//                         <h2>{project.title}</h2>
//                         <p>{project.description}</p>
//                         <p><strong>Technology:</strong> {project.technology}</p>
//                         <p><strong>Summary:</strong> {project.summary}</p>
//                         <img src={project.image} alt={project.title} style={{ maxWidth: '100px', maxHeight: '100px' }} />
//                         <p><a href={project.url} target="_blank" rel="noopener noreferrer">Project URL</a></p>
//                         <p><a href={project.github} target="_blank" rel="noopener noreferrer">GitHub</a></p>
//                     </li>
//                 ))}
//             </ul>
//         </div>
//     );
// };

// export default App;

// src/App.tsx
// import React, { useEffect } from 'react';

// const App: React.FC = () => {
//     useEffect(() => {
//         console.log('Component mounted');
//     }, []);

//     return (
//         <div>
//             <h1>Hello, World!</h1>
//         </div>
//     );
// };

// export default App;

import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Project {
    id: number;
    title: string;
    description: string;
    technology: string;
    summary: string;
    image: string;
    url: string;
    github: string;
}

const App: React.FC = () => {
    const [projects, setProjects] = useState<Project[]>([]); // Initial state is an empty array

    useEffect(() => {
        const fetchProjects = async () => {
            try {
                console.log('Fetching projects...');
                const response = await axios.get<Project[]>('http://localhost:8000/api/projects/');
                console.log('Projects fetched:', response.data);
                setProjects(response.data); // Set the state with fetched data
            } catch (error) {
                console.error('Error fetching projects:', error);
            }
        };

        fetchProjects(); // Trigger the data fetch
    }, []); // Run only once on component mount

    console.log('Rendering projects:', projects);

    return (
        <div>
            <h1>Projects</h1>
            <ul>
                {projects.map(project => (
                    <li key={project.id}>
                        <h2>{project.title}</h2>
                        <p>{project.description}</p>
                        <p><strong>Technology:</strong> {project.technology}</p>
                        <p><strong>Summary:</strong> {project.summary}</p>
                        <img src={project.image} alt={project.title} style={{ maxWidth: '100px', maxHeight: '100px' }} />
                        <p><a href={project.url} target="_blank" rel="noopener noreferrer">Project URL</a></p>
                        <p><a href={project.github} target="_blank" rel="noopener noreferrer">GitHub</a></p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default App;
