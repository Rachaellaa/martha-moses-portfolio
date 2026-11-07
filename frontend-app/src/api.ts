
const API_BASE_URL = 'http://127.0.0.1:8000';

export interface Profile {
  full_name: string;
  professional_title: string;
  short_bio: string;
  location: string;
  email: string;
  linkedin_url: string;
  github_url: string;
  portfolio_url: string | null;
}

export interface Project {
  id?: number;
  title: string;
  category: string;
  industry: string;
  description: string;
  problem_statement: string;
  solution: string;
  technologies: string[];
  key_features: string[];
  github_url: string | null;
  live_url: string | null;
  featured: boolean;
}

export interface Experience {
  job_title: string;
  company: string;
  employment_type: string;
  location: string;
  start_date: string;
  end_date: string;
  is_current: boolean;
  responsibilities: string[];
  technologies: string[];
}


export interface Skill {
  category: string;
  skills: string[];
}

async function fetchAPI<T>(endpoint: string): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`);

  if (!response.ok) {
    throw new Error(
      `API request failed: ${response.status} ${response.statusText}`
    );
  }

  return response.json() as Promise<T>;
}

export const getProfile = () =>
  fetchAPI<Profile>('/api/profile/');

export const getProjects = () =>
  fetchAPI<Project[]>('/api/projects/');

export const getExperience = () =>
  fetchAPI<Experience[]>('/api/experience/');

export const getSkills = () =>
  fetchAPI<Skill[]>('/api/skills/');
export interface ContactRequest {
  name: string;
  email: string;
  subject: string;
  message: string;
}

export interface ContactResponse {
  message: string;
}

export const sendContactMessage = (data: ContactRequest) =>
  fetch(`${API_BASE_URL}/api/contact/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  }).then(async (response) => {
    const result = await response.json();

    if (!response.ok) {
      throw new Error(
        result.detail || 'Unable to send your message.'
      );
    }

    return result as ContactResponse;
  });