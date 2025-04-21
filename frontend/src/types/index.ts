export interface User {
  id: number;
  username: string;
  email: string;
}

export interface UserProfile {
  id: number;
  user: User;
  bio?: string;
  profile_picture?: string;
}

export type TaskStatus = 'PENDING' | 'IN_PROGRESS' | 'COMPLETED';

export interface Task {
  id?: number
  title: string
  description: string
  status: string
  due_date: string
  assigned_to: string
}

export interface Profile {
  id: number
  username: string
}